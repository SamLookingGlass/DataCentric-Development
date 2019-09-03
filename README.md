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

# 1. UX 
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
The project skeleton and wireframes can be found [here](https://drive.google.com/open?id=1z7Cf3UGuxz3GL1wLHVTblkmvMhVvZSTd) 

#### (iii) Design
The bootstrap framework was used in for the front-end development of the website as it allows for mobile responsive design and easy grid layout. 

As the name of the web application suggests, 'Banarama', the colour palette and general design of the website takes after the colours of a banana (i.e. yellow, brown, black and green). As the focus of the project is a data-centric one, the layout of the webpage is not overly complex. Animated gifs were added to the website to enhance the visual experience of users.   

![#ffe261](https://placehold.it/15/ffe261/000000?text=+) `#ffe261` ![#733214](https://placehold.it/15/733214/000000?text=+) `#733214` ![#363531](https://placehold.it/15/363531/000000?text=+) `#363531` ![#10913f](https://placehold.it/15/10913f/000000?text=+) `#10913f` ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15`

# 2. Technologies Used
* [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
The project uses HTML5 to structure the content of the website.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
The project uses CSS to add stylistic touches to the website.
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
The project uses Bootstrap to structure the layout of the website (i.e. Navbar, Footer) and ensure website is mobile responsiveness.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
The project uses the Flask web framework to develop the web application (i.e. Set up connection to MongoDB Atlas, process and validate forms and handle the uploading of files)  
* [Jinja 2](https://jinja.palletsprojects.com/en/2.10.x/)
The project uses Jinja2 to write conditional statements to display content blocks when  certain conditions are met. Additionally, Jinja2 was used to set up template inherritance and extension of html/css files for the project.
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
The project uses MongoDB Atlas as a cloud database to store user data and file uploads.
* [GoogleFonts](https://fonts.google.com/)
The project uses GoogleFonts to style the typography on the website to enhance the visual experience of users.  
* [FontAwesome 4.7](https://fontawesome.com/v4.7.0/)
The project uses the icons provided by FontAwesome 4.7 alongside call-to-action buttons to enhance the user experience by making user interaction with the application more intuitive. 
* [Heroku](https://www.heroku.com/) 
The project uses Heroku for the deployment and management of the web application. As Heroku provides timelogs, when an error occurs, it makes easier to identity and remedy bugs.  

# 3. Future Features To Implement
- A feature for users to drag and drop files for uploads
- Bulk uploading of files
- Drag and drop files between albums

# 4. Testing

# 5. Known Bugs
- Changing an album name in the application will cause the existing photos in the album to not be displayed when the album is selected. 
- As such it is recommended that users not edit an album's name after images have been uploaded into it.
- As the database is a non-relational one, a change to the album name (i.e. User editing the album name) will only update the 'album' collection on MongoDB Atlas. - There is another collection called 'images' where the image's field 'uploaded_to' need to be updated as with new album's name as well.
- This bug is currently not fixed yet.

# 6. Deployment


# 7. Credits and Acknowledgement
- Credited to Pexel.com for the photo used for uploading
- Credits to [Smiling Banana photo](https://www.msn.com/en-in/health/nutrition/why-you-should-never-eat-bananas-for-breakfast/ar-BBOoNFc) 
- Credits to Giphy.com for the .gifs used for on the website
