
from pymongo import MongoClient
#Replace URL with MongoDB connection string
url = "mongodb+srv://Amod:Guwani@cluster0.aky8unc.mongodb.net/"
Client = MongoClient(url)

#Replace the Data Base name with the name of your database
db = Client['Test']

#Replace collection Name with the name of your collection
collection = db['Test']

#Check the connection
try:
    Client.admin.command ('ping')
    print ('Pinged your deployment. You successfully connected to MongoDB!')
except Exception as e :
    print (e)

document = {'name':"Danial",'age': 36}

#Instert the document into the collection
insert_result = collection.insert_one(document)

#Print the ID of the inserted document 
print ('Inserted Document ID:',insert_result.inserted_id)

Client.close()