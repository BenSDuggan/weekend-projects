# Main python script that crawls AAMC page and saves verification data to Firebase

import firebase_admin

# Create Firebase instance
cred = credentials.RefreshToken('path/to/refreshToken.json')
default_app = firebase_admin.initialize_app(cred)