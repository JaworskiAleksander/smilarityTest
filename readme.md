### Hello world
+ plagiarism texts
+ input - 2 documents, strings or other sources of data
+ compare how similar is the second document to the first one

| Resources | URLs | Method | Params | Status Code |
| :-------- | :--- | :---: | :--- | :--- |
| Register a new user | /register | POST | username<br>password | 200 ok<br>301 invalid user credentials |
| Detect similarity of a doc | /detect | POST | username<br>password<br>text1<br>text2 | 200 ok, return how similar are 2 inputs<br>301 invalid user credentials<br>302 invalid password<br>303 out of tokens|s
| Refill | /refill | POST | username<br>admin_password<br>refill_amount | 200 ok<br>301 invalid username<br>304 invalid admin_password<br>305 invalid refill amount|


Refill - allow increase of tokens for users
