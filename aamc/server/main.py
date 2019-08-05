# Main python script that crawls AAMC page and saves verification data to Firebase

import firebase_admin
from firebase_admin import credentials, firestore

import requests, urllib.request, time, calendar, csv
from bs4 import BeautifulSoup

# Variables
creds = '../../../secure/aamc-verification-firebase-adminsdk.json' # Credentials location
url = 'https://students-residents.aamc.org/applying-medical-school/applying-medical-school-process/applying-medical-school-amcas/' # URL with verification status
save_location = './verification.tsv' # Location of where to save backup data


# Create Firebase instance
cred = credentials.Certificate(creds)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Access database
coll = db.collection(u'2020-cycle')


# Get page data
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")
raw_content = soup.find_all(attrs={"class": "plugin-content"})[0]

epoch = calendar.timegm(time.gmtime())
marked = next(raw_content.find_all('div')[2].find('strong').children)
recieved = next(raw_content.find_all('div')[3].find('b').children)
verified = next(raw_content.find_all('div')[4].find('strong').children)[:-2]
transcript = next(raw_content.find_all('div')[5].find('strong').children)[:-2]

print("Spider results: marked={}, recieved={}, verified={}, transcript={}".format(marked, recieved, verified, transcript))

# Save results to firebase
coll.document(str(epoch)).set({
	u'marked':str(marked),
	u'recieved':str(recieved),
	u'verified':str(verified),
	u'trnascript':str(transcript),
})


# Save backup to file
with open(save_location, 'a') as f:
	writer = csv.writer(f, delimiter='\t')    
	writer.writerow([marked, recieved, verified, transcript])