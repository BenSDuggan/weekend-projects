# Script that checks to see if Firebase works

import firebase_admin
from firebase_admin import credentials, firestore


# Create Firebase instance
cred = credentials.Certificate('../../../secure/aamc-verification-firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

coll = db.collection(u'verification')

coll.document(u'test').set({
	u'today':u"8/20/19",
	u'makred':u'8/1/19'
})

docs = coll.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))