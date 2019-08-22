from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages, jsonify
import os
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
import time

from flask_uploads import UploadSet, IMAGES, configure_uploads
# from bson.json_util import dumpsb


# Timestamp function
def timestamp():
  now = int(round(time.time()*1000))
  time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now/1000))
  return time_now
  
app = Flask(__name__)
# create app route and test it
TOP_LEVEL_DIR = os.path.abspath(os.curdir) 
upload_dir = '/static/uploads/images/'
app.config["UPLOADS_DEFAULT_DEST"] = TOP_LEVEL_DIR + upload_dir
app.config["UPLOADED_IMAGES_DEST"] = TOP_LEVEL_DIR + upload_dir
app.config["UPLOADED_IMAGES_URL"] = upload_dir

# create an upload set and name it as images
images_upload_set = UploadSet("images", IMAGES) 
configure_uploads(app, images_upload_set)

# Retrieve environment environment
MONGO_URI = os.getenv('MONGO_URI')
#MONGO_URI = os.environ['MONGOLAB_URI']
DATABASE_NAME = 'project_photogallery'
ALBUMS = 'albums'
PHOTOS = 'images'
# Create connection
conn = pymongo.MongoClient(MONGO_URI)
db = conn[DATABASE_NAME]



@app.route('/photos')
def photos():
    results = db[PHOTOS].find({})
    return render_template("photos.html", data = results)    



# Funtion to render mainpage
@app.route('/')
def index():
    results = db[ALBUMS].find({})
    # print(dumps(results))
    return render_template("index.html", data = results)

# Function to view photos in selected album
@app.route('/albums/<album name>')
def create_album():
    results = db[ALBUMS].find({})
    results1 = db[PHOTOS].find({})
    return render_template("create_album.html", data = results)  

# Function to upload photos to album
@app.route('/albums/<album name>/upload')
def upload_photo():
    image = request.files.get('image')
    filename = images_upload_set.save(image)
    # Get file name and file extension
    filename_raw, file_extension = os.path.splitext(TOP_LEVEL_DIR + upload_dir + filename)
    filesize = os.path.getsize(TOP_LEVEL_DIR + upload_dir + filename)
    caption = request.form.get('caption')
    tags = request.form.get('tags')
    user_selected_file = str(request.form.getlist('selection'))
    db[PHOTOS].insert({
        'image_url' : images_upload_set.url(filename),
        'image_name' : filename, 
        'image_caption' : caption,
        'image_tags' : tags,
        'uploaded_on' : timestamp(),
        'deleted': user_selected_file,
        'deleted_on' : "null",
        # Converts filesize to mb 3sf
        'file_size' : round((filesize/1000000),3),
        'file_type' : file_extension,
        })
    return redirect(url_for('photos'))

# Function to delete album 
# Soft Delete (0 = not deleted, 1 = deleted)
@app.route('/albums/delete/')
def delete_album():
    return

# Function to delete photos from album
# Soft Delete (0 = not deleted, 1 = deleted)
@app.route('/albums/<album name>/delete/')
def delete_photo():
    return

# Function to edit album fields
@app.route('/albums/<album name>/edit/')
def edit_album_field():
    return

# Funtion to move photo between album
@app.route('/albums/<album name>/move/')
def move_photo():
    return

# Function to edit photo fields
@app.route('/albums/<album name>/<photo id>edit/')
def edit_photo_field():
    return


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
