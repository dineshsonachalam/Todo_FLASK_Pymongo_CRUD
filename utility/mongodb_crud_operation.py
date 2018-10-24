from pymongo import MongoClient
from bson.json_util import dumps
# Here dumps used to convert the pymongo cursor to json.

class crud_operation:

    def __init__(self, host, port, database):
        self.collection = 'tasks'
        self.database = database
        # mongodb://localhost:27017/_todo
        self.client = MongoClient('mongodb://' + str(host) + ':' +str(port) + '/' + str(database))

    # create new tasks
    def create(self,task_name):
        self.client[self.database][self.collection].insert_one(
            {
                "task_name": task_name,
                "status": "not completed",

            })
        return "Created new records!"

    # read all tasks
    def read_All(self):
        return dumps(self.client[self.database][self.collection].find())

    # read specific tasks
    def read(self,task_name):
        return dumps( self.client[self.database][self.collection].find({"task_name": task_name}))

    # update specific tasks
    def update(self,task_name,new_task_name,new_status):
        myquery = {"task_name": task_name}
        newvalues ={"$set":{"task_name": new_task_name,"status":new_status}}
        #print("myquery: ",myquery)
        #print("newvalues: ",newvalues)
        #self.client[self.database][self.collection].update_one(myquery,newvalues)
        self.client[self.database][self.collection].update_one({"task_name": "Rock"},{ "$set": { "task_name": "johnson" }})
        return dumps(self.client[self.database][self.collection].find())

    # delete specific taksname records
    def delete(self,task_name):
        myquery = {"task_name": task_name}
        self.client[self.database][self.collection].delete_one(myquery)
        return "Records deleted successfully!"