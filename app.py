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
    return render_template("index.html", data = results)

# Function to display albums (Working)
@app.route('/albums')
def display_albums():
    albums = db[ALBUMS].find({})
    return render_template('display_albums.html',data = albums)

# Route to show the page for uploading (Working)
@app.route('/uploads')
def display_uploads_page():
    results = db[ALBUMS].find({})
    results1 = db[PHOTOS].find({})
    return render_template("uploads.html", data = results, photos = results1)    

# Function to form to edit album (Working)
@app.route('/albums/<albumid>/edit_form')
def edit_selected_album(albumid):
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})
    return render_template("edit_album.html", data = selected_album)

# Function to process edits (Working) 
@app.route('/albums/<albumid>/edit_form', methods=['POST'])
def process_edit_selected_album(albumid):
    album_name = request.form.get('Album_Name')
    album_description = request.form.get('Album_Description')
    
    # original = db[ALBUMS].find({'album_name'})
    
    # db[ALBUMS].find({"vec.4" : {$exists : true}})
    
    # db[PHOTOS].update(
    #     {'album_uploaded_to': original},
    #     { '$set':
    #         {
    #             'album_uploaded_to': album_name,
    #             'edited_on': timestamp(),
    #         }
    #     })
        
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
    return redirect(url_for('display_albums', albumid = albumid))
    
# Function to form to edit photo fields (Working)
@app.route('/photo/edit_form/<photoid>')
def edit_selected_photo(photoid):
    selected_photo = db[PHOTOS].find_one({"_id": ObjectId(photoid)})
    return render_template("edit_photo.html", data = selected_photo)

# Function to process edit of photo fields (Working) 
@app.route('/photo/edit_form/<photoid>', methods=['POST'])
def process_edit_selected_photo(photoid):
    image_name = request.form.get('Image_Name')
    image_caption = request.form.get('Image_Caption')
    image_tag = request.form.get('Image_Tag')
    
    selected_photo = db[PHOTOS].find_one({"_id": ObjectId(photoid)})
    db[PHOTOS].update(
        {'_id':ObjectId(photoid)},
        { '$set':
            {
                'image_name': image_name,
                'image_caption': image_caption,
                'image_tag': image_tag,
                'edited_on': timestamp(),
            }
        })

    flash("Successfully edited.")
    results = db[ALBUMS].find({})
    return render_template("display_albums.html", data = results) 
    
# Function to create album (Working)
@app.route('/albums/create_album_form')
def create_album():
    return render_template("create_album.html")

# Function to process creation of album (Working) 
@app.route('/albums/create_album_form', methods=['POST'])
def process_create_album():
    album_name = str(request.form.get('Album_Name'))
    album_description = str(request.form.get('Album_Description'))
    db[ALBUMS].insert({
                'created_on': timestamp(),
                'album_name' : str(album_name),
                'album_description' : album_description,
                'edited_on' : "Null",
                'deleted': '0',
                'deleted_on' : "Null",
                })
    flash("Album successfully created.")
    return redirect(url_for('display_albums'))


# Function to show contents of selected album (Working)
@app.route('/albums/<albumid>')
def display_selected_album(albumid):
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})
    results = db[PHOTOS].find({})
    return render_template("display_selected_album.html", data = selected_album, photos = results)    
    

# Function to show delete confirmation page for album (Working)
@app.route('/albums/<albumid>/confirm_delete')
def display_delete_confirmation(albumid):
    selected_album = db[ALBUMS].find_one({"_id": ObjectId(albumid)})
    return render_template("delete_album.html", data = selected_album)
    
    
# Route to process the soft delete of album (Working)
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

# Function to show delete confirmation page for photo (Working)
@app.route('/photo/confirm_delete/<photoid>')
def display_delete_confirmation_photo(photoid):
    selected_photo = db[PHOTOS].find_one({"_id": ObjectId(photoid)})
    return render_template("delete_file.html", data = selected_photo)
    
    
# Route to process the soft delete of photo (Working)
@app.route('/photos/delete/<photoid>')
def process_delete_photo(photoid):
    selected_photo = db[PHOTOS].find_one({"_id": ObjectId(photoid)})
    db[PHOTOS].update(
        {'_id':ObjectId(photoid)},
        { '$set':
            {
                'deleted':'1',
                'deleted_on': timestamp(),        
            }
        })
    flash("Photo: {} has been deleted".format(selected_photo['image_name']))
    results = db[ALBUMS].find({})
    return render_template("display_albums.html", data = results)
    

# Route to process the upload (Working)
@app.route('/uploads/uploading', methods=['POST'])
def process_upload_photos():
    # Extract fields from upload form
    image = request.files.get('image')
    filename = images_upload_set.save(image)
    # Get file name and file extension
    filename_raw, file_extension = os.path.splitext(TOP_LEVEL_DIR + upload_dir + filename)
    filesize = os.path.getsize(TOP_LEVEL_DIR + upload_dir + filename)
    caption = request.form.get('caption')
    tags = request.form.get('tags')
    select = str(request.form.get('album_selected'))
    db[PHOTOS].insert({
        'image_url' : images_upload_set.url(filename),
        'image_name' : filename, 
        'image_caption' : caption,
        'image_tags' : tags,
        'uploaded_on' : timestamp(),
        'deleted': '0',
        'deleted_on' : "null",
        # Converts filesize to mb 3sf
        'file_size' : round((filesize/1000000),3),
        'file_type' : file_extension,
        'album_uploaded_to' : select,
        })
    flash("Image have been uploaded successfully.")    
    return redirect(url_for('display_uploads_page'))
    
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)



