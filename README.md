# Trello Clone API
### created with django rest framework 

# Description

A RESTFul API for the Trello.com clone.

## End Points
### Auth
* `POST /auth/login/`
* `POST /auth/logout/`
### Users
* `GET /users/`
* `POST /users/`
* `GET /users/pk`
* `PUT /users/pk`
* `PATCH /users/pk`
* `DELETE /users/pk`
### Columns
* `GET /columns/`
* `POST /columns/`
* `GET /columns/pk`
* `PUT /columns/pk`
* `PATCH /columns/pk`
* `DELETE /columns/pk`
### Cards
* `GET /cards/`
* `POST /cards/`
* `GET /cards/pk`
* `PUT /cards/pk`
* `PATCH /cards/pk`
* `DELETE /cards/pk`
## Images
All the API end point images are available in Demo folder
# Installation process
## Get the code
* Clone the repository
`git clone https://github.com/zeeshanwani/IITB.git`
## Create and activate the virtualenv
`virtualenv venv`
`venv/Scripts/activate`
## Install the project dependencies
`pip install -r requirements.txt`
## Run the command to create the database
`python manage.py migrate`
## Create super user
`python manage.py createsuperuser`
### After creating superuser please login using login-credentials and then you can add, update or delete data.
## Run the server
`python manage.py runserver` the application will be running on port 8000

