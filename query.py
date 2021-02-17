from tinydb import TinyDB,Query
User = Query()
import tinydb
db = TinyDB('db.json')

x = db.search(User.Age == 21)
print(x)
