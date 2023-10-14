# Build a Flask app with a Postgres database.

Your app should be able to do all the CRUD Actions: create, read, update, delete.

## Planning:

Plan 2 models with a One-Many relationship.
Keep it simple to begin with!

Draw class diagrams for the models (don't worry about methods).

Draw what the models would look like as tables in the database. Which are the Primary Keys? Where does the Foreign Key go?

Plan your pages using wireframes.

Plan your Restful Routes:

|VERB  |PATH                    |ACTION |
|:----:|:----------------------:|:-----:|
|GET   |/tasks                  |index  |
|GET   |/tasks/:id              |show   |
|POST  |/tasks                  |create |
|POST  |/tasks/:id             |update |
|POST  |/tasks/:id/delete      |destroy|

Optional ones for displaying forms:
|VERB  |PATH                    |ACTION |
|:----:|:----------------------:|:-----:|
|GET   |/tasks/new              |new    |
|GET   |/tasks/:id/edit        |edit   |



## Set up a Flask app:

A boilerplate app might look like:


```python
# .flaskenv

FLASK_APP=app.py
FLASK_DEBUG=true
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=4999
```

```python
# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "This is the home page!"
```

`flask run` and check you can see the message on this route.

Bring in SQLAlchemy, Migrate, and configure the app **with your own psql username/password and database name**: 

```python
# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Change user to your psql username, and tasks_app to your database name 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/tasks_app" 

db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

Write your models:
```python
models.py

from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    tasks = db.relationship('Task', backref='user')

    def __repr__(self):
        return f'<User {self.id}: {self.first_name} {self.last_name}>'

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text())
    duration = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Task {self.id}: {self.description}>'
```

Import them into `app.py`:
```python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/tasks_app"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import User, Task

@app.route("/")
def home():
  return "This is the home page!"
```

Create your database from your terminal:

```
createdb tasks_app
```

Initialize the migration folder with:

```
flask db init
```

Migrate and Update (like stage and commit) your database changes:

```
flask db migrate
flask db upgrade
```

Check in your GUI or `psql` that the tables have been created correctly.

Enter some data directly into your database, so you have some data to work with.

Begin working through **one route at a time** in your `controllers` folder and create the relavent `templates` (base + block content). Maybe start with a home page for the route `"/"`.

Don't forget to import and register your `blueprint`s in `app.py` near the bottom of your file (to avoid a circular import)!
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/tasks_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import User, Task
from controllers.tasks_controller import tasks_blueprint

app.register_blueprint(tasks_blueprint)

@app.route("/")
def home():
  return "This is the home page!"
```
