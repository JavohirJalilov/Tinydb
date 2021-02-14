from tinydb import TinyDB
db = TinyDB('db.json')

user1 = {'Name':'Javohir','Age':21,'City':'Samarqand','Job':'Developer'}
user2 = {'Name':'Jamshid','Age':19,'City':'Jizzax','Job':'Coding'}
user3 = {'Name':'Diyor','Age':19,'City':'Jizzax','Job':'Software engeener'}

db.insert(user1)
db.insert(user2)
db.insert(user3)
