#!/usr/bin/env python3

import sys
import logging.config
import requests
import uuid

import bottle
from bottle import get, post, request, response, template, redirect


# Set up app and logging
app = bottle.default_app()
app.config.load_config('./etc/app.ini')

logging.config.fileConfig(app.config['logging.config'])

KV_URL = app.config['sessions.kv_url']

# Disable Resource warnings produced by Bottle 0.12.19 when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    warnings.simplefilter('ignore', ResourceWarning)


@get('/')
def show_form():
    sid = request.get_cookie('sid', default='nil')
    if sid == 'nil':        
        new_id = uuid.uuid4()
        sid = str(new_id)
        r = requests.put('http://localhost:5100/', json = {sid : [0, 0]})

    r = requests.get('http://localhost:5100/'+sid)
    count1 = r.json()[sid][0]
    count2 = r.json()[sid][1]
    
    count1 = int(count1) + 1

    r = requests.put('http://localhost:5100/', json = {sid : [count1, count2]})
    response.set_cookie('sid', sid)

    return template('counter.tpl', counter1=count1, counter2=count2)


@post('/increment')
def increment_count2():
    sid = request.get_cookie('sid', default='nil')
    if sid == 'nil':        
        new_id = uuid.uuid4()
        sid = str(new_id)
        r = requests.put('http://localhost:5100/', json = {sid : [0, 0]})
    
    r = requests.get('http://localhost:5100/'+sid)
    count1 = r.json()[sid][0]
    count2 = r.json()[sid][1]
    count2 = int(count2) + 1

    r = requests.put('http://localhost:5100/', json = {sid : [count1, count2]})
    response.set_cookie('sid', sid)

    return redirect('/')


@post('/reset')
def reset_counts(): 
    sid = request.get_cookie('sid', default='nil')
    r = requests.delete('http://localhost:5100/'+sid)
    response.delete_cookie('sid') 

    return redirect('/')
