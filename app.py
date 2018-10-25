from flask import Flask
import os
app = Flask(__name__)
# __name__ is set to the name of the current class, function, method, descriptor, or generator instance.`
# Import blueprint defined in the route

from routes.todo import todo_blueprint

# Register a blueprint
app.register_blueprint(todo_blueprint)

if __name__ ==  '__main__':
    app_host =  os.environ.get('APP_HOST') or 'localhost'
    app_port =  os.environ.get('APP_PORT') or 8026
    app.run(host=app_host, port=app_port, debug=True, threaded=True)
    app.run(debug=True)

