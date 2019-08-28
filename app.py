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

# Function to display landing page (Working)
@app.route('/')
def index():
    messages = get_flashed_messages()
    print(messages)
    results = db[ALBUMS].find({})
    # print(dumps(results))
    return render_template("index.html", data = results)

# Function to display albums (Working)
@app.route('/albums')
def display_albums():
    albums = db[ALBUMS].find({})
    return render_template('layout1.html',data = albums)

# Route to show the page for uploading (Working)
@app.route('/photos')
def photos():
    results = db[PHOTOS].find({})
    return render_template("photos.html", data = results)    

# Function to form to edit album (Working)
@app.route('/albums/<albumid>/edit_form')
def edit_selected_album(albumid):
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})

    return render_template("layout1edit.html", data = selected_album)

# Function to process edits (Working) 
@app.route('/albums/<albumid>/edit_form', methods=['POST'])
def process_edit_selected_album(albumid):
    album_name = request.form.get('Album_Name')
    album_description = request.form.get('Album_Description')
    
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})
    db[ALBUMS].update(
        {'_id':ObjectId(albumid)},
        { '$set':
            {
                'album_name': album_name,
                'album_description': album_description,
                'edited_on': timestamp(),
            }
        })

    flash("Successfully edited.")
    return redirect(url_for('display_selected_album', albumid = albumid))

# Function to create album (Working)
@app.route('/albums/create_album_form')
def create_album():
    return render_template("layout1create.html")

# Function to process creation of album (Currently) 
@app.route('/albums/create_album_form', methods=['POST'])
def process_create_album():
    album_name = request.form.get('Album_Name')
    album_description = request.form.get('Album_Description')
    db[ALBUMS].insert({
                'created_on': timestamp(),
                'album_name' : album_name,
                'album_description' : album_description,
                'edited_on' : "Null",
                'deleted': '0',
                'deleted_on' : "Null",
                'images' : "Array",
                })
    flash("Album successfully created.")
    return redirect(url_for('display_albums'))



# Function to show contents of selected album (Working)
@app.route('/albums/<albumid>')
def display_selected_album(albumid):
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})
    results = db[PHOTOS].find({})
    return render_template("layout1display.html", data = selected_album, photos = results)    
    

# Function to show delete confirmation page (Working)
@app.route('/albums/<albumid>/confirm_delete')
def display_delete_confirmation(albumid):
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})
    return render_template("layout1delete.html", data = selected_album)
    
    
# Route to process the soft delete (Working)
@app.route('/albums/<albumid>/delete')
def process_delete_album(albumid):
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})
    db[ALBUMS].update(
        {'_id':ObjectId(albumid)},
        { '$set':
            {
                'deleted':'1',
                'deleted_on': timestamp(),        
            }
        })
    flash("Album: {} has been deleted".format(selected_album['album_name']))
    return redirect(url_for('display_albums'))


# Route to process the upload (Working)
@app.route('/photos/upload', methods=['POST'])
def process_upload_photos():
    # Extract fields from upload form
    image = request.files.get('image')
    filename = images_upload_set.save(image)
    # Get file name and file extension
    filename_raw, file_extension = os.path.splitext(TOP_LEVEL_DIR + upload_dir + filename)
    filesize = os.path.getsize(TOP_LEVEL_DIR + upload_dir + filename)
    caption = request.form.get('caption')
    tags = request.form.get('tags')
    # Validation check to see if any file has been uploaded before POSTing to database
    if filename is not None:
        db[PHOTOS].insert({
            'image_url' : images_upload_set.url(filename),
            'image_name' : filename, 
            'image_caption' : caption,
            'image_tags' : tags,
            'uploaded_on' : timestamp(),
            'deleted': 0,
            'deleted_on' : "null",
            # Converts filesize to mb 3sf
            'file_size' : round((filesize/1000000),3),
            'file_type' : file_extension,
            })
        flash("Images have been uploaded successfully.")    
        return redirect(url_for('photos'))
    else:
        flash("Please upload a photo before submitting.")
        return redirect(url_for('photos'))

    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)



