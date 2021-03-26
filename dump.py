import sys
import requests

s = sys.argv[1]
r = requests.get(s)
for k in r.json()['keys']:
    rd = requests.get(s+'/'+k)
    print(rd.text)
