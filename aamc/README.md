# AAMC Verification Tracker

This project is designed to track the AAMC verification, transcript and "Academic Change Request" section on their [website](https://students-residents.aamc.org/applying-medical-school/applying-medical-school-process/applying-medical-school-amcas/).  There are two main pieces of code: the [server](/server) and [client](/client) code.  The server code is a python script that looks at the AAMC URL that contains this data (https://students-residents.aamc.org/applying-medical-school/applying-medical-school-process/applying-medical-school-amcas/), parses this data and saves it to a [Firebase database](https://firebase.google.com/).  The client code is a web page, written in HTML, JavaScript and CSS, that grabs the data from the database and displays it.

## Install

### Server
The packages required are `firebase-admin`.

Instal them by running:
```
sudo pip install firebase-admin
```

## Client

