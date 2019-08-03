# AAMC Verification Tracker

This project is designed to track the AAMC verification, transcript and "Academic Change Request" section on their [website](https://students-residents.aamc.org/applying-medical-school/applying-medical-school-process/applying-medical-school-amcas/).  There are two main pieces of code: the [server](/server) and [client](/client) code.  The server code is a python script that looks at the AAMC URL that contains this data (https://students-residents.aamc.org/applying-medical-school/applying-medical-school-process/applying-medical-school-amcas/), parses this data and saves it to a [Firebase database](https://firebase.google.com/).  The client code is a web page, written in HTML, JavaScript and CSS, that grabs the data from the database and displays it.

The Firebase firestore database has three collections in it: `verification`, `transcript` and `change`.  Each  collection is made up of a document for each data point.

## Install

### Firebase firestore database

Create a [Firebase project](https://console.firebase.google.com/u/0/) with some name.  Then create a new Firestore database in locked mode.  Add the three collections: `verification`, `transcript` and `change`.  Next create a web app by going clicking on `Project overview` and the web icon (</>).  Give it a name and record the firebaseConfig json object for the client data.

The idea of this application is to have the python, server, script read and write data while only allowing the web, client, page to read data.  These are the rules used to achieve this.

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read: if true; allow write: if false;
    }
  }
}
```


### Server

The packages required are `firebase-admin`.

Instal them by running:
```
sudo pip install firebase-admin
```

Test the code by running `test.py` in the server file.

## Client

Not much needs to be done to set the client up.  Simply test it by opening `test.html`, in the client folder, and ensure you see data in the console.



