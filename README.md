# To-Do List Application

### Using django rest framework 

# Description

It is a To-Do Application developed with Django Rest Framework, and MySQL Database is used.


## End Points

### Without Token Authentication

* `GET /task-list/`
* `GET /task-detail/{pk}/`
* `POST /task-create/`
* `PUT /task-update/{pk}/`
* `PATCH /task-update-status/{pk}/`
* `DELETE /task-delete/{pk}/`

<!-- ### With Token Authentication

* `POST /add`
* `GET /task-detail/{pk}/`
* `POST /register`
* `POST /login`
* `GET /getTodoList/{user_id}` -->


## Get the code
* Clone the repository
`git clone https://github.com/safiullah1999/Todo_App.git`

## Install the project dependencies

First create virtualenv, then enter the following command.

`pip install -r requirements.txt`

## Install xampp and MySQL

Create a new Database as "todo"

## Run the commands to generate the database
`python manage.py makemigrations`

`python manage.py migrate`

## Run the server
`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**
