# FlaskMVC Starter Kit

A Flask Starter Kit following the MVC pattern for rapidly building small applications. Use the powerful CLI tool [Crafter](https://github.com/rdp-jr/crafter) to help you in building your application.

## Features
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [flask-login](https://flask-login.readthedocs.io/en/latest/)
- [flask-wtf](https://flask-wtf.readthedocs.io/en/0.15.x/)

## Project Structure
    .
    ├── app                     # main application directory
    │   ├── controllers          
    │   ├── forms               # flask-wtf forms
    │   ├── models              # flask-sqlalchemy models
    │   ├── public              
    │   │   ├── css             
    │   │   │   └── app.css     # global css file
    │   │   └── js               
    │   │       └── app.js      # global js file
    │   ├── routes              
    │   ├── views               # jinja template files
    │   │   ├── errors          # contains error views for 400, 404, etc.
    │   │   └── templates       
    │   │       └── base.html   # base template for all views    
    │   ├── config.py           # config file
    │   ├── utils.py            # helpers for app
    │   └── __init__.py         # application factory    
    ├── database                # where sqlite file is stored   
    ├── tests                   
    └── wsgi.py                 # entry point


## Getting Started
1. click `Use this template` and clone the newly created repository
2. Change config variables in `app/config.py`
3. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) -- `py -m venv venv`
4. Activate the virtual environment 
  * Windows -- `venv\Scripts\activate`
  * MacOS/Unix -- `source venv/bin/activate`
5. Install requirements -- `pip install -r requirements.txt`
6. Run application -- `flask run`
7. Go to [localhost:5000](http://localhost:5000) to see the welcome page

## User 
- The starter kit includes a `user` resource (implemented with flask-login) to get you started.

1. Go to [localhost:5000/register](http://localhost:5000/register) and register a new user
2. You will be redirected to [localhost:5000/login](http://localhost:5000/login) upon successful registration, then enter the new user's credentials
3. You will be logged in and redirected to [localhost:5000/dashboard](http://localhost:5000/dashboard)

## Adding Flask Extensions
-  to add other Flask extensions, simply install an extension and initialize it in `app/__init__.py` following the [application factory pattern](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/)

## Crafter
- a CLI tool to help you in building applications rapidly
- refer to [Crafter's documentation](https://github.com/rdp-jr/crafter) regarding its usage

## License
MIT


Made with ❤️ by Obee