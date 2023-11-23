import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancesystem-10ca7-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "194011":
        {
            "name": "Pranav Deshpande",
            "major": "Ai-ds",
            "starting_year": 2019,
            "total_attendance": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "194012":
        {
            "name": "Shahid",
            "major": "Arts",
            "starting_year": 2010,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
},
    "194013":
        {
            "name": "Tom",
            "major": "Science",
            "starting_year": 2018,
            "total_attendance": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)