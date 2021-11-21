import pyrebase
from pyrebase.pyrebase import Storage
config = {
    "apiKey": "AIzaSyDcbFiLUHlY6qLHhYZHBbBMiPqdoVc1owQ",
    "authDomain": "ithankespeechtotext-d4d85.firebaseapp.com",
    "projectId": "ithankespeechtotext-d4d85",
    "storageBucket": "ithankespeechtotext-d4d85.appspot.com",
    "messagingSenderId": "229969828380",
    "appId": "1:229969828380:web:b617e70a06058b87055dd9",
    "measurementId": "G-3QMW2RRFD7"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path = "ITHANKe_Python/Files/lion.jpg"
pathLocal = "Files/lion.jpg"
storage.child(path).put(pathLocal)