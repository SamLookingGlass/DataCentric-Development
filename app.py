from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages, jsonify
import os
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps

from flask_uploads import UploadSet, IMAGES, configure_uploads
# from bson.json_util import dumpsb

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
#MONGO_URI = os.getenv('MONGO_URI')
MONGO_URI = os.environ['MONGO_URI']
DATABASE_NAME = 'project_photogallery'
ALBUMS = 'albums'
PHOTOS = 'images'
# Create connection
conn = pymongo.MongoClient(MONGO_URI)
db = conn[DATABASE_NAME]

@app.route('/')
def index():
    results = db[ALBUMS].find({})
    # print(dumps(results))
    return render_template("index.html", data = results)

@app.route('/photos')
def photos():
    results = db[PHOTOS].find({})
    return render_template("photos.html", data = results)    

@app.route('/photos/upload', methods=['POST'])
def upload():
    image = request.files.get('image')
    filename = images_upload_set.save(image)
    filename_raw, file_extension = os.path.splitext(TOP_LEVEL_DIR + upload_dir + filename)
    filesize = os.path.getsize(TOP_LEVEL_DIR + upload_dir + filename)
    caption = request.form.get('caption')
    tags = request.form.get('tags')
    db[PHOTOS].insert({
        'image_url' : images_upload_set.url(filename),
        'image_name' : filename, 
        'image_caption' : caption,
        'image_tags' : tags,
        # 'uploaded_on' : new Timestamp(),
        'deleted': 0,
        'deleted_on' : "null",
        'file_size' : filesize,
        'file_type' : file_extension,
        })
    return redirect(url_for('photos'))
    
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
