from tinydb import TinyDB
db = TinyDB('db.json',indent=4)

user = {'Name':'Javohir','Age':21,'Phone_number':998941234567}

db.insert(user)