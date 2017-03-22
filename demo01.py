import pymongo

conn = pymongo.Connection("127.0.0.1",27017)
db = conn.tutorial

db.posts.count()