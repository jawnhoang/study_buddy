# uses the app object from __init__.py
from app import app
from app import socketio
from app import manager
from flask_socketio import SocketIO, send, join_room, leave_room
"""
if you wish to add another column. add it to User class in models.py
then run the manager.run() below.
then run these commands in the shell
python .\study_buddy.py db init ( do this once)
python .\study_buddy.py db migrate
 python .\study_buddy.py db upgrade
"""
#if __name__ == "__main__":
#     manager.run()


# if you want to run the server, use the command below
socketio.run(app, debug=True)
app.run(debug=True)
