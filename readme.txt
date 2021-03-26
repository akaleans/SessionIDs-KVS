Name:	Khalen Stensby
Class:	CPSC-449 Friday
Assn:	Project 3

Server Side Sessions

This project is intended to show how to use a key value source database as a way to store session ids instead of storing cookies directly. All methods are working properly and running the tests provided in the Project Documentation provided to us will yield perfect results.

app.py updates:
	Changed show_form() to first check if there is a session id (SID) in a cookie. If there is not SID present, it will create a new random UUID and send a PUT request to the key value store along with 0,0 for the counts. It will then increment count1 and send another PUT request updating the key value store.
	Changed increment() to work almost exactly the same as show_form except that it works on count2.
	Changed reset() to first get the SID from the cookie and then send a delete request to the key value store with the SID as the key to delete. Then delete the cookie SID after this.

dump.py creation:
	dump.py is a simple script that will grab all current keys as well as their values from the key value store.
	
	***NOTE***
	In order to run the dump.py script, do the following:
	1) Open a terminal at the dump.py location
	2) Ensure that both services have been started using 'foreman start' in another terminal
	3) Open at least 1 browser and go to 'localhost:5000'
	4) Type 'python3 dump.py http://localhost:5100'
