import json
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.twitterdb

valid = False
while not valid:
	filename = raw_input("Enter JSON filename: ")
	try:
		#Remove blank lines in file
		data = filter(None, (line.rstrip() for line in open(filename+'.json','r')))
		collection = db[filename]
		valid = True
	except IOError:
		print 'Not a valid file. Try again.'

for line in data:
	jsonobj = json.loads(line)
	post_id = collection.insert_one(jsonobj).inserted_id

print collection.find_one()['text']