# myflatironp5-project

This project is intended to solve the problem of long term parking of ones car/cars in a public parking garage
and be able to use an app to see all cars you parked in the garage, and details about each car. 

An owner of a car/cars looking to park them in safe public parking garage can sign up in the app,
using their personal information like: name, email, phone, and password to create an account.
Once this accoutn is created they are then presented with a form in which they enter the make-model,
color and number plate of each car. An owner/user can then login to the the app to view their parked cars,
edit information about them, add more cars, and also be able to see their parked cars.

## Project Status
This project is still in development phase. This project will be completed by 10/15/2023

## Built with-
Here are the frameworks/libraries used to bootstrap this project:
#### React
#### Flask
#### SQLalchemy

## Getting Started
To get a local coopy up and running folow these simple steps:
Prerequisites
* npm
  npm install
## Installation
1. Clone the repo:
    git clone https://github.com/ATuray77/myflatironp5-project.git
2. Install NPM packages:
    npm install
    npm start

## Features
This project features a backend server built with Flask, a database built with SQLalchemy 
and a frontend/client side built with React
1. SQLalchemy Database
The database stores all the information on cars and their owners
When new cars are aded to the database they become persistent for future retrieval

2. Flask backend server
RESTful API routes
The backend server contains signup, login, session, and logout routes. These use validations techniques
to authenticate and login a user/owner and also maintain their sessions without automatically logging them out.
There are also routes to get all users/owners, and routes to get all cars and also cars by their id. 
There are also routes to make updates or delete a car from the database. 

### Rect frontend
The frontend/client-side presents a programmatically intuitive navigation to the user.
1. Car Form tab:
This enables users to submit information about a car they want to park in the garage
2. My cars tab:
This gives users an interactive view of all their parked cars with detailed information.
Users/Owners can view their cars when they are logged. 
Other users/owners are not able to tell which cars belong to which owner. 
        

Happy coding!

---

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)

