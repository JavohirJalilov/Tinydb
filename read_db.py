from tinydb import TinyDB,Query
db = TinyDB('db.json')

x = db.search(Query().Age==21)
print(x)