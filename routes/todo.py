from flask import Blueprint,request
import os
from utility.mongodb_crud_operation import crud_operation


mongo_host =  'localhost'
mongo_port =  27017
mongo_database = 'todo'

todo_crud = crud_operation(mongo_host,mongo_port,mongo_database)
todo_blueprint = Blueprint('todo',__name__,template_folder='templates')

@todo_blueprint.route('/',methods=['GET','POST'],endpoint='read_all')
def read_all():
    return todo_crud.read_All()

@todo_blueprint.route('/<task_name>',methods=['GET','POST'],endpoint='read')
def read(task_name):
    return todo_crud.read(task_name)

@todo_blueprint.route('/new',methods=['GET','POST'],endpoint='new_tasks')
def new_tasks():
    if request.method == 'POST':
        content = request.json
        print("Content: ",content)
        # [{'task_name': 'dinesh'}]
        task_name = content[0]['task_name']
        return todo_crud.create(task_name)

@todo_blueprint.route('/update',methods=['GET','POST'],endpoint='update_tasks')
def update_tasks():
    if request.method == 'POST':
        content = request.json
        task_name = content[0]['task_name']
        new_task_name = content[0]['new_task_name']
        new_status = content[0]['new_status']
        #print("task_name: ",task_name)
        return todo_crud.update(task_name,new_task_name,new_status)

#
@todo_blueprint.route('/delete',methods=['DELETE'],endpoint='delete_tasks')
def delete_tasks():
    content = request.json
    task_name = content[0]['task_name']
    return todo_crud.delete(task_name)



