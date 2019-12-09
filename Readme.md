# study_buddy 
[![Build Status](https://travis-ci.com/dailesjsu/study_buddy.svg?branch=master)](https://travis-ci.com/dailesjsu/study_buddy)

#Link to our web-applocation:
http://studybuddy-sjsu.herokuapp.com

#Unit tets is updated under the app folder. They are named with _test.py under the app folder. Anytime, we push the local repo to remote repo, travis will automatically run the test  

## How to use the application:
 Have **flask, python3 and mysql** installed
 - Windows Users: 
    1. open powershell
    2. use the cd command to navigate to your project directory
    3. once in the directory, use the command python routes.py
    4. then using a browser open page with the url: http://127.0.0.1:5000/
  
 - Mac users:
    1. Open terminal 
    2. Use the cd command to naviagte to the project directory
    3. once in the directory, use command python routes.py
    4. then using a browser open page with the url: http://127.0.0.1:5000/

## Features: 

 - Login: it is for existing customer to log in to the main page
 - Logout: When the customer want to log out, then they will be redirected to the homepage.
 - Register: For new customer to create new account
 - Location: we use google's api for geolocation in html5. We simply use the ip_address of the user with their consent in order to show    them their location.
 - Find study buddy: using your location, we see in our data base who else in proximity of you or the general area of the school   would    like to study the same course
- add friend:keep track of list of people that you studied with
- remove friend
- change profile pic
- change username
- change class
- delete account
