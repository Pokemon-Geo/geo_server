import os
import datetime
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './upload/photos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_photo(file, uuid):    
    
    print(os.path.join(app.config['UPLOAD_FOLDER'], uuid))
    # check if the folder with uuid exists
    if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], uuid)):        
        os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], uuid))        
    timestamp = str(int(round(datetime.datetime.now().timestamp())))   

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], uuid + "/" + timestamp + ".jpg"))

    return timestamp