#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
from pymongo import MongoClient
from bson.objectid import ObjectId


#animal shelter class to insantiate the environment
class AnimalShelter(object):
    def __init__(self, username, password, host, port, db, collection):

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, host, port)) #environment variables for MongoClient
        self.database = self.client['%s' % (db)]
        self.collection = self.database['%s' % (collection)]
        
        
    #create function    
    def create(self, data):
        #if the data is not null, continue:
        if data is not None:
            insertion = self.database.animals.insert_one(data)
            
            #checks if the insert_one method correctly inserted the data (if not 0, return True)
            if insertion != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    #read function
    def read(self, data):
        
        try:
            #result = self.database.animals.find(data) #using .find() method to search through database
            #return list(result)
            results = self.database.animals.find(data)
            return [document for document in results]
        except Exception as e:
            print(e)
            return []
    
    
    
    #update function
    def update(self, search, updateInfo):
        #if search is not null, continue:
        if search is not None:
            outcome = self.database.animals.update_many(search, {"$set": updateInfo}) #update method
        else:
            return "{}"
        
        return outcome.raw_result #returns the outcome as a raw result with information about the process
    
    #delete function
    def delete(self, deleteData):
        if deleteData is not None:
            outcome = self.database.animals.delete_many(deleteData) #delete method
        else:
            return "{}"
        
        return outcome.raw_result #returns the outcome as a raw result with information about the process
    
    


# In[ ]:




