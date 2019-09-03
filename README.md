# Data-centric Development Milestone Project – 'Banarama' 

# Context

This project focuses on the data-centric development for a mobile-responsive web-based photo album application called ‘Banarama’. From the get-go, users can create albums, upload their photos on this application and then share their albums with anyone. 

The application does not require users to create an account. Users can choose to upload their photos into a default album called ‘Uploads’ or create their own albums.

# Demo
A live website of the application can be found here: https://tsw-photogallery.herokuapp.com/

# Index
1. UX
2. Technologies Used
3. Future Features To Implement
4. Testing
5. Known Bugs
6. Deployment
7. Credits and Acknoledgement

# 1. User Experience (UX)
#### (i) Project Strategy
Following closely the objectives of an online photo album application (i.e. upload, store and organise photos online), these user goals were identified and served as guidelines for the features that were implemented.

| User Stories| Features|
| ------ | ------ |
| User wants to upload photo to application.| Form to facilitate uploading of files. (Create)|
| User wants to give uploaded photo a caption and hashtags.| Form to capture user input and process to update database. (Create)|
| User wants to view uploaded photo with relevant fields.| Display photos back to user in an organised manner. (Read)|
| User wants to edit photo name, photo caption and hashtags.| Form to capture user edits to photo fields and process to update database. (Update)|
| User wants to delete an uploaded photo.| Process to soft delete photo from database. (Delete)|
| User accidentally deletes uploaded photo.| Deletion confirmation form to double check if user wants to continue with delete.|
| User wants to create an album.| Form to capture user input for album name and description. (Create)|
|User wants to see all the created albums.| Display all albums in the database to user in a organised manner. (Read)|
| User wants to upload photo to album.| Form to allow user to select album to upload to.|
| User wants to edit album name and description.| Form to capture user edits to album fields and process to update database. (Update)|
| User wants to delete album.| Process to soft delete album from database. (Delete)|
| User accidentally deletes album.| Deletion confirmation form to double check if user wants to continue with delete.|

#### (ii) Project Scope
The project skeleton and structure (wireframes) can be found [here.](https://drive.google.com/open?id=1z7Cf3UGuxz3GL1wLHVTblkmvMhVvZSTd) 

#### (iii) Design
The bootstrap framework was used in for the front-end development of the website as it allows for mobile responsive design and easy grid layout. 

As the name of the web application suggests, 'Banarama', the colour palette and general design of the website takes after the colours of a banana (i.e. yellow, brown, black and green). As the focus of the project is a data-centric one, the layout of the webpage is not overly complex. Animated gifs were added to the website to enhance the visual experience of users.   

![#ffe261](https://placehold.it/15/ffe261/000000?text=+) `#ffe261` ![#733214](https://placehold.it/15/733214/000000?text=+) `#733214` ![#363531](https://placehold.it/15/363531/000000?text=+) `#363531` ![#10913f](https://placehold.it/15/10913f/000000?text=+) `#10913f` ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15`

# 2. Technologies Used
* [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
<br> The project uses HTML5 to structure the content of the website.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
<br> The project uses CSS to add stylistic touches to the website.
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
<br> The project uses Bootstrap to structure the layout of the website (i.e. Navbar, Footer) and ensure website is mobile responsiveness.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
<br> The project uses the Flask web framework to develop the web application (i.e. Set up connection to MongoDB Atlas, process and validate forms and handle the uploading of files)  
* [Jinja 2](https://jinja.palletsprojects.com/en/2.10.x/)
<br> The project uses Jinja2 to write conditional statements to display content blocks when  certain conditions are met. Additionally, Jinja2 was used to set up template inherritance and extension of html/css files for the project.
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
<br> The project uses MongoDB Atlas as a cloud database to store user data and file uploads.
* [GoogleFonts](https://fonts.google.com/)
<br> The project uses GoogleFonts to style the typography on the website to enhance the visual experience of users.  
* [FontAwesome 4.7](https://fontawesome.com/v4.7.0/)
<br> The project uses the icons provided by FontAwesome 4.7 alongside call-to-action buttons to enhance the user experience by making user interaction with the application more intuitive. 
* [Heroku](https://www.heroku.com/) 
<br> The project uses Heroku for the deployment and management of the web application. As Heroku provides timelogs, when an error occurs, it makes easier to identity and remedy bugs.  

# 3. Future Features To Implement
- A feature for users to drag and drop files for uploads
- Bulk uploading of files
- Drag and drop files between albums

# 4. Testing
#### (i) HTML and CSS Validation
- Code from style.css was validated on http://csslint.net/ (Pass)
- Codes from the .html files were validated on https://www.freeformatter.com/html-validator.html (Pass)

#### (ii) Manual Testing 
| Test Case Number| Test Case Description| Results|
| ------ | ------ | ------ |
| 1 | On the landing page (https://tsw-photogallery.herokuapp.com), user should see 3 buttons on the landing page (i.e. 'Create an Album', 'Upload photos', and 'View Albums'). | Pass |
| 2 | When user clicks on 'Create an Album' on the landing page, the URL should route to https://tsw-photogallery.herokuapp.com/albums/create_album_form | Pass |
| 3 | On https://tsw-photogallery.herokuapp.com/albums/create_album_form, a form should be generated in the lower half of the screen and has 2 user input fields ('album name' and 'album description') and 2 buttons ('Create' and 'Back'). | Pass |
| 4 | On https://tsw-photogallery.herokuapp.com/albums/create_album_form, user inputs 'Test' as the album name and 'Test uploads' as the album description and clicks 'Create'. The URL should route to https://tsw-photogallery.herokuapp.com/albums. User should see a flash message 'Album successfully created.' at the upper section of screen. User should also see the 'Test' album being added displayed. | Pass |
| 5 | On https://tsw-photogallery.herokuapp.com/albums/create_album_form, user clicks on 'Back'. The URL should route to https://tsw-photogallery.herokuapp.com/albums. | Pass |
| 6 | When user clicks on 'Upload Photos' on the landing page, the URL should route to https://tsw-photogallery.herokuapp.com/uploads | Pass |
| 7 | On https://tsw-photogallery.herokuapp.com/uploads, a form should be generated in the lower half of the screen and has 4 user input fields ('choose file', 'image caption', 'tags', and 'select upload destination') and 1 buttons ('Upload'). | Pass |
| 8 | On the upload form, when user clicks on 'Browse', a file-directory should pop up and prompts the user to select a file for uploading.| Pass |
| 9 | On the upload form, when user clicks on 'Select Upload Destination', a dropdown list of albums names should appear and is selectable.| Pass |
| 10 | On the upload form, when user selects a test image "Capture.PNG" from his local directory, inputs "Test photo" as the image caption, "#test" as the tag and selects 'Test' as the album upload destination. User clicks 'Upload'. Page refreshes and user should see a flash message 'Image has been uploaded successfully' if image upload has been successful.| Pass |
| 11 | On the upload form, user selects a test image "Shepherd.jpg" from his local directory, inputs "Test photo" as the image caption, "#test" as the tag and selects 'Test' as the album upload destination. User clicks 'Upload'. Page refreshes and user should see a flash message 'Image has been uploaded successfully' if image upload has been successful.| Pass |
| 12 | On the upload form, when user clicks 'Upload' without any file selected for uploading, user should see a pop-up prompting 'Please select a file'. | Pass |
| 13 | When user clicks on 'View Albums' on the landing page, the URL should route to https://tsw-photogallery.herokuapp.com/albums. | Pass |
| 14 | On https://tsw-photogallery.herokuapp.com/albums, user should see several albums cards being displayed in the lower-half of the screen. Each album card should have an album name, the album description, the last edited date & time, the date & time of album creation and 3 buttons ('View', 'Edit' and 'Delete').| Pass |
| 15 | On https://tsw-photogallery.herokuapp.com/albums, user should see the only the 'Uploads' album have the 1 button - 'View'.| Pass |
| 16 | On https://tsw-photogallery.herokuapp.com/albums, when user clicks on 'View' on the 'Test' album, the URL should route to https://tsw-photogallery.herokuapp.com/albums/5d6e567368755f885f7abe97. User should also see in the lower half of the screen, a 'Back' button, a image card with the name 'Shepherd', a caption - 'Test photo', a tag - '#Test', the upload time & date, the file extension and file size, and 2 buttons ('Edit' and 'Delete').| Pass |
| 17 | On https://tsw-photogallery.herokuapp.com/albums/5d6e567368755f885f7abe97, when user clicks 'Back', the URL should route to https://tsw-photogallery.herokuapp.com/albums?albumid=5d6e567368755f885f7abe97 .| Pass |
| 18 | On the 'Test' album page, when user clicks on 'Edit' on the image card - 'Shepherd', the URL should route to https://tsw-photogallery.herokuapp.com/photo/edit_form/5d6e80669098df04bb085968. User should also see in the lower half of the screen a form with 3 user inputs already filled up - 'Shepherd', 'Test photo', '#Test', and 2 buttons ('Update' and 'Back').| Pass |
| 19 | On the edit form for the photo 'Shepherd' (in the 'Test' album), user edits image caption to 'Smart Shepherd' and clicks 'Update'. The URL reoutes to https://tsw-photogallery.herokuapp.com/photo/edit_form/5d6e80669098df04bb085968. User should see a flash message 'Successfully edited' at the top of the page. User should see the updated photo fields on the 'Test' album.| Pass |
| 20 | On the 'Test' album page, when user clicks on 'Delete' on the image card - 'Shepherd', the URL should route to https://tsw-photogallery.herokuapp.com/photo/confirm_delete/5d6e80669098df04bb085968. User should also see in the lower half of the screen a deletion confirmation box with the prompt 'Are you sure you want to delete the file 'Shepherd' and 2 buttons ('Yes' and 'No').| Pass |
| 21 | On the deletion conformation page for the file 'Shepherd', user clicks 'No', the URL should route back to 'https://tsw-photogallery.herokuapp.com/albums' .| Pass |
| 22 | On the deletion conformation page for the file 'Shepherd', user clicks 'Yes', the URL should route back to https://tsw-photogallery.herokuapp.com/albums . User should see a flash message 'File: Shepherd has been deleted' and the photo card removed from the 'Test' album.| Pass |
| 23 | On https://tsw-photogallery.herokuapp.com/albums, when user clicks on 'Edit' on the 'Test' album, the URL should route to https://tsw-photogallery.herokuapp.com/albums/5d6e567368755f885f7abe97/edit_form. User should also see a form being generated in the lower half of the screen with 2 user inputs already filled up - 'Test' and 'Test uploads', and 2 buttons ('Update' and 'Back').| Pass |
| 24 | On the edit form for album fields, when user clicks 'Back', the URL should route to https://tsw-photogallery.herokuapp.com/albums?albumid=5d6e567368755f885f7abe97 .| Pass |
| 25 | On the edit form for album fields, when user edits album description to 'Editing album description' and clicks 'Update', the URL should route to https://tsw-photogallery.herokuapp.com/albums?albumid=5d6e567368755f885f7abe97. User should see a flash message 'Successfully edited.' at the top of the screen and also find the updated album fields being displayed.| Pass |
| 26 | On https://tsw-photogallery.herokuapp.com/albums, when user clicks on 'Delete' on the 'Test' album, the URL should route to https://tsw-photogallery.herokuapp.com/albums/5d6e567368755f885f7abe97/confirm_delete. User should also see in the lower half of the screen a deletion confirmation box with the prompt 'Are you sure you want to delete the album 'Test' and 2 buttons ('Yes' and 'No').| Pass |
| 25 | On the deletion conformation page, user clicks 'No', the URL should route back to 'https://tsw-photogallery.herokuapp.com/albums?albumid=5d6e567368755f885f7abe97' .| Pass |
| 26 | On the deletion conformation page, user clicks 'Yes', the URL should route back to 'https://tsw-photogallery.herokuapp.com/albums?albumid=5d6e567368755f885f7abe97' . User should see a flash message 'Album: Test has been deleted' and the album card removed from the 'View albums' page.| Pass |

#### (iii) Cross Browser Compatibility
- A cross browser compatability test was conducted using http://browsershots.org/https://tsw-photogallery.herokuapp.com/.
- The website was tested on 54 web browsers.
- Screenshots of the test can be found [here.](https://drive.google.com/file/d/1l8FWJ41MJbqagcnafS677GS9hKvUtq3g/view?usp=sharing)
- Not compatible with Lynx 2.8.8 Ubuntu 12.04 LTS, Rekonq 1.1 Ubuntu 9.10 and Dillo 3.0.2 Ubuntu 9.10

#### (iv) Mobile Responsiveness
- The test results can be found [here.](https://search.google.com/test/mobile-friendly?id=xg6pnaXTpSjm908GkfInDQ)
- The web application is mobile responsive

# 5. Known Bugs
- Changing an album name in the application will cause the existing photos in the album to not be displayed when the album is selected. 
- As such it is recommended that users not edit an album's name after images have been uploaded into it.
- As the database is a non-relational one, a change to the album name (i.e. User editing the album name) will only update the 'album' collection on MongoDB Atlas. - There is another collection called 'images' where the image's field 'uploaded_to' need to be updated as with new album's name as well.
- This bug is currently not fixed yet.

# 6. Deployment
#### (i) Development Process
- All codes was written on AWS Cloud9 and codes were saved and tested locally. 
- Regular committing and pushing of codes to GitHub ensured that changes to codes can be tracked and allows for version control maintainence.
- Heroku was set up first before embarking on code development.   

#### (ii) Heroku Deployment Steps
- Login to Heroku on your command-line interface 
<br>`$ heroku login`
- On your command-line interface create the Heroku application 
<br>`$ heroku create tsw-photogallery` 
- Once application has been created, Heroku automatically sets up a remote git repository
<br>`Creating app... done` 
- Next, create a local git repository on your command-line interface
<br>`$ git init`
<br>`$ git add .`
<br>`$ git commit -m "first commit"`
- Then, connect this local git repository to the remote git repository set up on Heroku
<br>`$ heroku git:remote -a tsw-photogallery`
- Check if the remote repository has been linked properly
`<br>$ git remote -v`
- Prepare the following application files for deployment in the application root directory
<br>1. Procfile
<br> Copy and paste this line of `web: gunicorn run:app` into the Procfile. 
<br>2. requirements.txt
<br>`pip freeze --local > requirement.txt` 
- Then, add the new configuration files to your local repository:
<br>`$ git add . `
<br>`$ git commit -a -m "Add configuration files"` 
- Last, make an initial deployment of the application to Heroku
<br>`$ git push heroku master`

#### (iii) How to deploying the project locally
- The repository can be cloned using the following command on your terminal
<br> `$ git clone https://github.com/SamLookingGlass/DataCentric-Development` 
- To run the application, type in the following command on your terminal
<br> `python3 app.py`

# 7. Credits and Acknowledgement
- Credited to Pexel.com for the photos used for uploading
- Credits to [Smiling Banana photo](https://www.msn.com/en-in/health/nutrition/why-you-should-never-eat-bananas-for-breakfast/ar-BBOoNFc) 
- Credits to Giphy.com for the .gifs used for on the website
