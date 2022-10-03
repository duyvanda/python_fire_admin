from heapq import merge
from http.client import responses
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
# data = {'name':'Duy', 'age':40}
# db.collection('persons').add({'name':'Duy', 'age':40})

# db.collection('persons').document('notautoid').set(data)

# for auto generate id
# db.collection('persons').document().set(data)

# MERGING
# merge_data = {'job': 'IT'}
# db.collection('persons').document('notautoid').set(merge_data, merge=True)

# data={'movie':'Avenger'}
# db.collection('persons').document('notautoid').collection('movies').add(data)


# res = db.collection('persons').document('notautoid').get()
# print(res.to_dict())


responses = db.collection('persons').where('age','>',30).get()
for res in responses:
    print(res.to_dict())
print("Done")

# https://firebase.google.com/docs/firestore/query-data/queries#python_28

