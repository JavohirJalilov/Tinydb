from tinydb import TinyDB,Query
db = TinyDB('db.json',indent=4)
User = Query() 
user = {'Phone_number':123}

x = db.update(user,User.Name=='Javohir')
print(x)

