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

### debug results
/usr/src/app/app.py:28: DeprecationWarning: count is deprecated. Use Collection.count_documents instead.
web_1  |   return bool(users.find({

/usr/src/app/app.py:77: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
web_1  |   insertResult = users.insert({

/usr/src/app/app.py:146: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
web_1  |   users.update(

 /usr/src/app/app.py:141: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
web_1  |   ratio = text1.similarity(text2)

verify keywords in postedData before assigning them to variables