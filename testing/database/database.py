import sqlite3
from flask import Flask

app = Flask(__name__)

DATABASE = './database/database.db'

def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE, check_same_thread=False)    
        db.row_factory = sqlite3.Row
    
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(Flask, '_database', None)
    if db is not None:
        db.close()