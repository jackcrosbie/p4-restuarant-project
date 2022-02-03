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

### Structure

### Surface


## Technologies


## Features

**Features Implemented**

_As a User I want to be able to request a booking so that i can easily book a table_

As stated above, one of the primary functions of Jack's Bistro website will be to allow user/customers to request a booking. The information from this bookings would be stored in a database, in our case using PostgresSQL. The user will be required to enter their name, email, number in party, date required and time desired.

_As a Site Admin I want to be able to approve or reject bookings so that i can control capacity for the restuarant_

The site admin needs the ability to approve and reject bookings. This helps the owner maintain control of customer numbers to prevent overbookings. Bookings approval is required so the customer gets confirmation the restuarant can accommodate them on the date and time requested. This information will be stored on the PostgreSQL database and the site admin will be able to access it on the site admin panel. The admin panel will be generated and accessed through Django.

_As a Site Admin I want to delete and manage bookings so that i can maintain the calender_

Due to the nature of the website/product cancellations will occur. Either due to illness or unforeseen circumstances customers will have to cancel or rearrange bookings. This means the site admin will need to have the ability to cancel or change bookings on the system. This keeps everything tidy and more easily managed. This function will be created through a combination of PostgreSQL and Django.


**Features Left To Implement**

_As a User I want a stylish looking website so that i can navigate it easily_

By providing a well designed and easily navigated website it improves the user satisfaction while using the website and also increases the likelyhood of them revisiting it.
As Jack's Bistro, from a user point of views, primary use would be making a reservation, seeing what was on the updated menu and making contact, if required, it meant a more simple website design was best suited, in my opinion. To make a well laid out website which was easily navigational I used general CSS styling and also Bootstrap for a more solid design.

_As a User I want to be able to easily navigate the site so that i can easily view all the content_

A well designed and thoughtout website should allow the user to navigate through it effectively. They should be able to move to the content they wish to view intuitively and quickly. The main approach to solve this was to put in a navigation bar at the top of the page. The links provided (Home, Reservations, Menu, Contact Us) allow the user go to the page they need with one click of a mouse. I used general HTML and CSS styling in conjunction with Bootstrap to create a fully functioning navigational bar at the top of everypage of the website. In the mobile version of the website the navigation bar is a Hamburger stlye menu achieved through Bootstrap.


_As a User I want to be able to edit my bookings so that i can make a correction or change if needed_


_As a User I want to be able to register so that i can save my information for future bookings_

A user will be able to register 

_As a User I want to be able to login and logout so that i can keep my information safe_

If a user is registered they need the ability to login and logout of the website. This is a safety issue and stops someone else being able to use their account or access their information, if they were continually logged in. The login and logout ability was created through Django.

_As a User I want to see messages when logging in and logging out so that i can be sure the action was undertaken_

When user are logging in and logging out it is beneficial for them to see a message stating the action has occured. Again this is a safety issue and just confirms the action was undertaken so the user can navigate away from the website knowing they have been logged out. This helps prevents users staying logged in if an error occurs as the user will be alerted.

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


## Credit

### Acknowledgements






