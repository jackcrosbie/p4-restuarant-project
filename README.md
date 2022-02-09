# Jack's Bistro


## Contents
- [Introduction](#introduction)
- [UX](#ux)
- [Technologies](#technologies)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credit)
- [Acknowledgements](#acknowledgements)


## Introduction

This is my submission for the portfolio 4, Fullstack toolkit, project. It is a booking system and website for a fictional restuarant.
Within the website will be a reservations/booking system, a section to view and print menus and a contact form to get in touch with the restuarant. Here the information will be stored on a PostgreSQL database and will be able to be maintained and edited by the superuser.

### Demo

Live link will be deployed here !!!

## UX

Utilising UX design is essential these days to provide meaningful and relevant experiences to the user. To provide more balance and structure to my UX design I opted to use the five planes method to design and implement on my website.

### Strategy

**Vision**

The vision of the website is to enable users an easy method to reserve a table and stay up to date with what the restuarant has to offer.
This provides an overall better user experience and enables the user to make edits/corrections to their reservations.
From an Admin point of view the website would mean less work when it came through the management and organistion of bookings/reservations.

**Aims**

1. Provide a stylish, easy to use and intuitive website.
2. Implement a booking system which is easily maintained and straightforward to use.
3. Supply a contact form for any special requests/large booking parties which goes from the user to the admin.
4. Display an updated version of the menu which is easy to maintain and edit for the site admin.
5. Enable users to Login/Logout, autofilling information when logged in to save time when making future bookings.

**User Stories**

- As a User I want to be able to easily navigate the site so that i can easily view all the content
- As a User I want a stylish looking website so that i can navigate it easily
- As a User I want to be able to view, print and download the menu so that i can see what items are being sold
- As a User I want to be able to request a booking so that i can easily book a table
- As a User I want to be able to edit my bookings so that i can make a correction or change if needed
- As a User I want to be able to check availability for any given night so that i can see if i should make a booking request
- As a User I want to be able to register so that i can save my information for future bookings
- As a User I want to be able to login and logout so that i can keep my information safe
- As a User I want forms to autocomplete if logged in so that i can save time when making bookings
- As a User I want to see messages when logging in and logging out so that i can be sure the action was undertaken
- As a Site Admin I want to be able to edit the menu so that i can keep it up to date with new items
- As a Site Admin I want to delete and manage bookings so that i can maintain the calender
- As a Site Admin I want to be able to approve or reject bookings so that i can control capacity for the restuarant

### Scope

Based on my user stories these are the features I felt needed implementing:

- Homepage with information about who we are, what we do and where we are.
- A navigation bar to take you to the pages on the site
- Registration page so that customers could register
- Reservations page so users could make a reservation
- Login and Logout, powered by Django AllAuth, so user could safely log in and out.
- Contact Us page, with form, so customers with special requests could get in touch 
- Edit/Delete reservations page so registered users could manage their reservations

### Structure

Due to the nature of the website I felt keeping things simple was essential to it's use. Everything is clearly labeled and easily navigational so the user can get to what they need easily.
All the major aspects of the website have their own page:
- Homepage for basic information
- Reservations page for making reservations
- Menu page to view the current menu the restuarant has to offer
- Contact Us page to easily get in touch for extra information or special requests
- Account page for people to manage their reservations by either editing or deleting them.

### Databases

The two apps I use that require databases are the Reservations App and the Contact App.

Both these apps have models in them to create a form by which user can make reservations or get in contact.
Each app has a model to create a form and extra variables such as time_options and others.

#### Reservations

This app requires the user to fill field within the form and each field has specific parameters for entering data, such as phone_number requires integers and can't have letters.
This feature can be used by either users who are register and logged in and those that aren't registered. I felt users shouldn't have to register to make a reservation. The information from the form is then sent to the database which can then me managed by the admin on the backend.

User who are registered and logged in will have the ability to edit or delete their bookings through their account page.

#### Contact Us

Contact App also utilises a form with various fields for the user to get in touch with the restuarant. This is more if they have special booking requests, want to find out more information or want to give some feedback. The user does not need to be signed in to use this feature.

#### Menu

The menu app has one model in this and it contains four images which are the menu. This can easily be changed by uploading pictures of the new menu making it easy and efficient for the admin.

### Skeleton

[Wireframes for this project](assets/documents/p4-wireframes.pdf)

My wireframes were created using Balsamiq and represent the simplicity I was going for.

Using bootstrap I tried to give everything uniform and similar so the user would feel comfortable navigating around the site.
I tried to keep as close to my wireframes as possible when creating the various pages.

### Surface

(Coolors picture of palette)

I chose the colours in the above palette as I felt they had nice contrast to each other as well as blending together nicely for the overall look.
The antique white was much softer as an overall background then just white and also means the field boxes for the form stand out a little more.
The black background on the first top container, which holds the logo and first navbar, makes the antique white text stand out nicely so it's easily read. 

![coolors image](https://github.com/jackcrosbie/p4-restuarant-project/blob/main/assets/documents/images/p4-colors.png?raw=true)

## Technologies

The following is a list of the various technologies I used along with what they were used for:

- Django
Django is the framework that has been used to build the over project and its apps.
- Python
Python is the core programming language used to write all of the code in this application to make it fully functional.
- Bootstrap
Used for creating responsive design.
- Google Fonts
Used to obtain the fonts linked in the header, fonts used were Raleway and Lobster
- Font Awesome
Used to obtain the icons used on the high scores and rules pages.
- Google Developer Tools
Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project.
- GitHub
Used to store code for the project after being pushed.
- Git
Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- Gitpod
Used as the development environment.
- Heroku
Used to deploy my application..
- Pep8
Used to test my code for any issues or errors.
- Unicorn Revealer
Used to detect overflow of elements, which allowed me to quickly debug any issues.
- Coloors
Used to create a colour palette for the design.
- Cloudinary
Used to store all of my static files and images.
- W3C Markup Validation Service
Used to validate all HTML code written and used in this webpage.
- W3C CSS Validation Service
Used to validate all CSS code written and used in this webpage.
- PostgreSQL
I have used Heroku's PostgreSQL relational database in deployment to store the data for my models.

## Features

**Features Implemented**

_As a User I want to be able to request a booking so that i can easily book a table_

As stated above, one of the primary functions of Jack's Bistro website will be to allow user/customers to request a booking. The information from this bookings would be stored in a database, in our case using PostgresSQL. The user will be required to enter their name, email, number in party, date required and time desired.

![reservation form](https://github.com/jackcrosbie/p4-restuarant-project/blob/main/assets/documents/images/reservation-form.png?raw=true)

_As a Site Admin I want to be able to approve or reject bookings so that i can control capacity for the restuarant_

The site admin needs the ability to approve and reject bookings. This helps the owner maintain control of customer numbers to prevent overbookings. Bookings approval is required so the customer gets confirmation the restuarant can accommodate them on the date and time requested. This information will be stored on the PostgreSQL database and the site admin will be able to access it on the site admin panel. The admin panel will be generated and accessed through Django.

_As a Site Admin I want to delete and manage bookings so that i can maintain the calender_

Due to the nature of the website/product cancellations will occur. Either due to illness or unforeseen circumstances customers will have to cancel or rearrange bookings. This means the site admin will need to have the ability to cancel or change bookings on the system. This keeps everything tidy and more easily managed. This function will be created through a combination of PostgreSQL and Django.

_As a User I want to be able to easily navigate the site so that i can easily view all the content_

A well designed and thoughtout website should allow the user to navigate through it effectively. They should be able to move to the content they wish to view intuitively and quickly. The main approach to solve this was to put in a navigation bar at the top of the page. The links provided (Home, Reservations, Menu, Contact Us) allow the user go to the page they need with one click of a mouse. I used general HTML and CSS styling in conjunction with Bootstrap to create a fully functioning navigational bar at the top of everypage of the website. In the mobile version of the website the navigation bar is a Hamburger stlye menu achieved through Bootstrap.

![navbar-1](https://github.com/jackcrosbie/p4-restuarant-project/blob/main/assets/documents/images/navbar-1.png?raw=true)

![navbar-2](https://user-images.githubusercontent.com/82109134/153136781-2d5cb2fc-3a63-46b5-80ad-2da21588c896.png)

AS shown in the pictures above I opted to use two navbars for this project. Navbar one sat at the top of the page and dealt with all the AllAuth authorisation. If the user is logged in the navbar shows account and logout. If the user it not logged in it shows Register and Login. The second navbar I used was for each page on the site. Even though I could have put all the links on one navbar I thought the use of two was better as it gave each more space and was less information all in once place.

_As a User I want to see messages when logging in and logging out so that i can be sure the action was undertaken_

When user are logging in and logging out it is beneficial for them to see a message stating the action has occured. Again this is a safety issue and just confirms the action was undertaken so the user can navigate away from the website knowing they have been logged out. This helps prevents users staying logged in if an error occurs as the user will be alerted.

![log out message](![image](https://user-images.githubusercontent.com/82109134/153181129-d5669f06-8c1a-42f6-807a-197b197115fa.png)


Using Bootstrap I added messages so the user could see if he or she logged out or in. These messages show the users if they logged out successfuly or not. 

_As a User I want to be able to login and logout so that i can keep my information safe_

If a user is registered they need the ability to login and logout of the website. This is a safety issue and stops someone else being able to use their account or access their information, if they were continually logged in. The login and logout ability was created through Django.

![login](https://github.com/jackcrosbie/p4-restuarant-project/blob/main/assets/documents/images/login.png?raw=true)

_As a User I want to be able to register so that i can save my information for future bookings_

A user will be able to register through the register button on the site. Once they fill out the register form they will then be about to log in and log out in future. Authenication is provided by django AllAuth which keeps users and their information safe and secure

![registration form](https://github.com/jackcrosbie/p4-restuarant-project/blob/main/assets/documents/images/registration-form.png?raw=true)

_As a User I want to be able to edit my bookings so that i can make a correction or change if needed_

Once a user has registered and is logged in the account section of the website will become available. If a user navigated to the account page they will see any resevations that have displayed in a bootstrap image card. Pictured here:

![edit reservation](https://user-images.githubusercontent.com/82109134/153183280-3c54d8b8-e2df-42eb-915c-904112fc44a5.png)

Below the cards will be a button to either delete or edit a booking. This completes the CRUD functionality for the reservations on my website. Users are able to Create, Retrieve, Updated and Delete reservations they have made once they are registered and logged in.

_As a User I want a stylish looking website so that i can navigate it easily_

By providing a well designed and easily navigated website it improves the user satisfaction while using the website and also increases the likelyhood of them revisiting it.
As Jack's Bistro, from a user point of views, primary use would be making a reservation, seeing what was on the updated menu and making contact, if required, it meant a more simple website design was best suited, in my opinion. To make a well laid out website which was easily navigational I used general CSS styling and also Bootstrap for a more solid design.

The website is broken down into the main componenets and each one of these has it's own page. They are all clearly marked and easily navigational to through the navbars.
Every step is clearly marked and the styles are uniform through, like all the buttons are styled the same using bootstrap for a sense of familiarity throughout for the user.
Through my choice of colours, images, use of bootstrap, HTML and CSS i feel the website i have created is both easy to navigate as well as stylish.

**Features Left To Implement**

_As a User I want forms to autocomplete if logged in so that i can save time when making bookings_

When a user logins to make a reservation sections of the form autocompletes based on their login information. Details such as name and email will be autogenerated in the form and just leave the other variable fields such as date, time and number of party left to fill in. This will save the user time when making future bookings.

_As a User I want to be able to view, print and download the menu so that i can see what items are being sold_

In the menu section of the webpage a user can view, print and download the latest up to date menu for the restuarant. This helps give the user the information they might need about products and dietary requirements. This helps cut down on the owners having to be contacted for the information requested allowing them more time to focus on running the restuarant. Menu created through HTML, Bootstrap and CSS.

_As a Site Admin I want to be able to edit the menu so that i can keep it up to date with new items_

Menus will need to be edited at times due to produce availability, chef changes and other factors. 

_As a User I want to be able to check availability for any given night so that i can see if i should make a booking request_

The ability to be able to check the availability or number of tables left for a given date helps the user know whether they can request a booking or not. This is turn cuts down on time utilised managing the bookings. If a user sees the restuarant is full for a given night they won't request a booking therefor cutting down the time the site admin needs to manage the bookings. 

## Testing

### Manual Testing

### Automated Testing


## Deployment

The master branch of this repository has been used for the deployed version of this application.

Using Github & Gitpod
To deploy my command-line interface application, I had to use the Code Institute Python Essentials Template, as this enables the application to be properly viewed on Heroku using a mock terminal.

- Click the Use This Template button.  
-  Add a repository name and brief description.
-  Click the Create Repository from Template to create your repository.
-  To create a Gitpod workspace you then need to click Gitpod, this can take a few minutes.
-  When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
   -  git add .: adds all modified files to a staging area
   -  git commit -m "A message explaining your commit": commits all changes to a local repository.
   -  git push: pushes all your committed changes to your Github repository.

### Creating an Application with Heroku

I followed the below steps using the Code Institute tutorial:

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies pip3 freeze --local > requirements.txt. Please note this file should be added to a .gitignore file to prevent the file from being committed.
1. Go to Heroku.com and log in; if you do not already have an account then you will need to create one.
2. Click the New dropdown and select Create New App.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

Heroku Settings You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

- In the Settings tab, click on Reveal Config Vars and set the following variables:
  - If using credentials you will need to add the credentials as a variable, the key is the name 'CREDS' and the value is the contents of your creds JSON
  - Add key: PORT & value 8000
- Buildpacks are also required for proper deployment, simply click Add buildpack and search for the ones that you require.
  - For this project I needed to add Heroku Postgres.

Heroku Deployment In the Deploy tab:

- Connect your Heroku account to your Github Repository following these steps:
  - Click on the Deploy tab and choose Github-Connect to Github.
  - Enter the GitHub repository name and click on Search.
  - Choose the correct repository for your application and click on Connect.
- You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the Deploy Branch button whenever you want a change made.
- Once you have chosen your deployment method and have clicked Deploy Branch your application will be built and you should see the below View button, click this to open your application:

## Credit

All the code used is entirely original and written by me. However I drew on resources such as Stack Overflow, django.docs, tutor support and Slack to fix various bugs and issues i encountered.

### Acknowledgements

As always I want to thank my mentor, Daisy McGirr for her fantastic advice, support and feedback throughout this project and beyond. I would also like to thank my peer Daisy Gunn for always being helpful, full of advice and willing to listen. 






