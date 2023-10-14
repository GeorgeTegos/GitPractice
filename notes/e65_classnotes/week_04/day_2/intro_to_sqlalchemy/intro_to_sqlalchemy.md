# Intro to SqlAlchemy

**Duration: 120 minutes**

## Learning Objectives

- Understand what an ORM is.
- Understand what SqlAlchemy does
- Be able to configure SqlAlchemy with Flask.
- Use SqlAlchemy to Read from Postgres database.
- Use SqlAlchemy to Create a new entry in Postgres database.

## Introduction

So far our data is hard coded in the app. This is an issue as every time we restart the server our data is recreated. So if we were to add new tasks then we would lose them every time we restart.

Flask does not support databases natively. This is one of the many areas in which Flask is intentionally not opinionated, which is great, because you have the freedom to choose the database that best fits your application instead of being forced to adapt to one.

To solve this problem we will be using an ORM called SqlAlchemy and an Postgres database.

### Why use an ORM?

ORM stands for Object Relational Mapping. Looking at each of these words will explain their use in the real world:

- Object - This part represents the objects and programming language where the framework is used, for example Python.

- Relational - This part represents the RDBMS database you're using (Relational Database Manager System). There are numerous popular relational databases out there, but you're probably using on of the following - MSSQL, MySQL, Oracle Database, PostgreSQL.
What's common between most relational databases is their relational structures (tables, columns, keys, constraints, etc.).

- Mapping - This final part represents the bridge and connection between the two previous parts, the objects and the database tables.

A common task when programming any web service is to create a robust database backend. Traditionally, programmers would write raw SQL statements, pass them to the database engine and parse the returned results as a normal array of records. Like such:

```python
import psycopg2
conn = psycopg2.connect('example.db')

c = conn.cursor()
c.execute('''
          CREATE TABLE users
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE tasks
          (id INTEGER PRIMARY KEY ASC, title varchar(250), description varchar(250),
          user_id INTEGER NOT NULL,
           FOREIGN KEY(user_id) REFERENCES users(id))
          ''')

c.execute('''
          INSERT INTO users VALUES(1, 'Sandy')
          ''')
c.execute('''
          INSERT INTO tasks VALUES(1, 'Learn Python', 'Get to grips with this language!', 1)
          ''')

conn.commit()
conn.close()
```

Nowadays, programmers can use Object-relational mapping (ORM) programs to remove the necessity of writing tedious and error-prone raw SQL statements that are inflexible and hard-to-maintain.

ORM is a tool for converting data between incompatible types in object-oriented programming languages. Usually, the classes used in an OO language, such as Python, contains types that cannot be expressed as primitives, such as integers and strings. For example, a User object may have a list of Task objects.

In order to deal with the complexity of managing objects, ORMs were developed. Our to-do list can be expressed as an ORM system with a User class, and a Task class, where each class maps to a table in the underlying database. Instead of writing database interfacing code yourself, an ORM takes care of these issues for you while you can focus on programming the logics of the system.

We want to create a database with the following structure:

![users_tasks](images/users_tasks.png)


### SqlAlchemy

We will be using a popular ORM called SqlAlchemy.

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

There are three most important components in writing SQLAlchemy code:

- A Table that represents a table in a database.
- A mapper that maps a Python class to a table in a database.
- A class object that defines how a database record maps to a normal Python object.

Instead of having to write code for Table, mapper and the class object at different places, SQLAlchemy allows a Table, a Mapper and a Class object to be defined at once in one class definition.

### Installing and Configuring SqlAlchemy

To install `Flask-SQLAlchemy` in your virtual environment, make sure you have activated it first, and then run:

```bash
pip3 install flask-sqlalchemy
```

We also need to address making updates to an existing database as the application needs change or grow. This is hard because relational databases are centred around structured data, so when the structure changes the data that is already in the database needs to be migrated to the modified structure.

The second extension we will install is `Flask-Migrate`.

This extension is a Flask wrapper for `Alembic`, a database migration framework for SQLAlchemy. Working with database migrations adds a bit of work to get a database started, but that is a small price to pay for a robust way to make changes to your database in the future.

```bash
pip3 install flask-migrate
```

Now in `app.py` we will create our Flask app, an instance of the database and the database migration engine.

```python
# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://user@localhost:5432/tasks_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

First, we create a Flask app and configure the database connection URL, following the format:

`dialect://username:password@host:port/database`

We are going to use a PostgreSQL database, running on localhost:5432, with a database named `tasks_app`. Your username and password may be different depending on how you set up PostgreSQL.

We then create a `db` object that represents the database, and a `migrate` object that represents the migration engine.

### Creating our models

Now that our database is set up we can write our classes to represent our Users and Tasks.

When we create these models SqlAlchemy allows us to pass in a Database Model. The properties of the class will then be mapped to columns in the database.

We will write these classes in a file called `models.py`.

```bash
touch models.py
```

And in here we will create the 2 classes we need with the correct structure.

```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    tasks = db.relationship('Task', backref='user', lazy='true')

    def __repr__(self):
        return f'<User {self.id}: {self.first_name} {self.last_name}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text())
    duration = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Task {self.id}: {self.description}>'

```

The User class created above inherits from db.Model, a base class from Flask-SQLAlchemy. This class defines several fields as class variables. Fields are created as instances of the db.Column class, which takes the field type as an argument, plus other optional arguments that, for example, allow us to indicate which fields have defaults.

When you define a primary key column in a SQLAlchemy model, it automatically generates an auto-incrementing integer value for each new row inserted into the database table. 

We also defined the relationship between the 2 tables in the User class by adding a db.relationship. With `backref` we declare a new property on the Task class called `user`. We can then use my_task.user to get to the associated user object. When we create a new task, we can also then pass in the full user instead of just the user.id.

The `__repr__` method tells Python how to print objects of this class, which is useful for debugging.

### Migrating the database

We have defined the initial database structure in `models.py`.

As the application continues to grow, there is going to be a need change that structure.

`Alembic` (the migration framework used by Flask-Migrate) will allow us to make these changes in a way that does not require the database to be recreated from scratch.

`Alembic` maintains a migration repository, which is a folder in which it stores its migration scripts. Each time a change is made to the database structure, a migration script is added to the repository with the details of the change. To apply the migrations to a database, these migration scripts are executed in the sequence they were created.

We can run these migrations through the Flask command. But firstly, we need to create our database:

```bash
createdb tasks_app
```

Now let's create the migration repository for our app by running the following command:

```bash
flask db init
```

After you run this command, you will find a new migrations folder.

Now to create the first database migration, which will include the users and tasks tables that maps to the database model.

 There are two ways to create a database migration: manually or automatically. To generate a migration automatically, Alembic compares the database structure as defined by the database models, against the actual database structure currently used in the database. It then populates the migration script with the changes necessary to make the database structure match the application models. In this case, since there is no previous database, the automatic migration will add the entire User and Task models to the migration script.

```bash
flask db migrate -m "users and tasks tables"
```

The migration folder now has a migration script. If you look at the script you will find that it has two functions called upgrade() and downgrade(). The upgrade() function applies the migration, and the downgrade() function removes it. This allows you to rollback any migration.

The `flask db migrate` command does not make any changes to the database, it just generates the migration script. To apply the changes to the database, the `flask db upgrade` command must be used.

```bash
flask db upgrade
```

## Adding data

Let's use SqlAlchemy to interact with the database from our Flask app. We'll create a temporary route so that we can write and execute code in our app when the "/" route is visited.

First, we'll import the models, and write a basic route:

```python
# app.py
# AS BEFORE

from app.models import User, Task

@app.route("/")
def temporary_route():
  # We'll try out SqlAlchemy methods here
  return "Done!"
```

We can access a number of SqlAlchemy methods by using the pattern `AModelName.query.some_function()`

Common functions we will use are:

- delete() - Delete all entries in a table
- all() - Get all entries
- get({id}) - get an entry by id,

To make sure we don't duplicate data we will initially delete all from the database.

```python
@app.route("/")
def temporary_route():
  Task.query.delete()
  User.query.delete()

  return "Done!"
```

Now create a new user:

```python
# Continuing in temporary_route, before the return

  user = User(username='Sandy')
  print("user before commit")
  print(user)
  db.session.add(user)
  db.session.commit()
  print("user after commit")
  print(user)
```

Changes to a database are done in a session. Multiple changes can be accrued in a session and once all the changes have been added you can issue a single `db.session.commit()`, which writes all the changes atomically. If at any time while working on a session there is an error, a call to `db.session.rollback()` will abort the session and remove any changes stored in it.

Changes are only written to the database when `db.session.commit()` is called. Sessions guarantee that the database will never be left in an inconsistent state.

## Two ways of interacting with the database

In Flask-SQLAlchemy, there are two primary ways to interact with the database:

1. Using methods on `db.session`: `db.session` is an instance of `Session`, which represents the current database session. It acts as a transactional container for all the objects that have been loaded or modified during the request. When you perform operations using `db.session`, you are working directly with instances of your models (Python objects) before committing the changes to the database.

2. Using methods on `Model.query`: When defining a model class, SQLAlchemy automatically adds a query object to it, which is accessible through `Model.query`. The `Model.query` attribute provides a convenient way to perform database queries directly on the model without having to interact with the session explicitly.

The main differences between the two methods are:

`db.session` is used when you want to perform multiple operations in a single transaction. For example, when you need to create, update, or delete multiple objects and want all the changes to be committed together.

`Model.query` is more suitable for simple queries and is commonly used when you want to retrieve data from the database. It is a cleaner and more concise way to perform basic CRUD (Create, Read, Update, Delete) operations.

Both methods have their use cases, and you can choose the one that fits your specific needs. In more complex scenarios, you might use a combination of both methods to achieve your desired functionality.

Now we will make sure that this has worked by querying the database and getting our user back.

```python
# temporary_route

  users = User.query.all()
  print("query all users")
  print(users)
```

There is another way to do queries. If you know the id of a user, you can retrieve that user as follows:

```python
# temporary_route

  found_user = User.query.get(user.id)
  print(f"query get user with id = {user.id}")
  print(found_user)
```

Now let's add a couple of tasks:

```python
# temporary_route

  task1 = Task(description='Learn Python', completed=True, user=found_user)
  db.session.add(task1)
  task2 = Task(description='Buy Milk', user=found_user)
  db.session.add(task2)
  db.session.commit()
```

And lets query these tasks

```python
# temporary_route

  tasks = Task.query.all()
  print("query all tasks")
  print(tasks)

```
We did not need to set a value for the done field in the second task because that field has a default, which we set up in the model definition.

We can also now access the tasks user details as well through the relationship we set up earlier.

```python
# temporary_route

  print("task1.user")
  print(task1.user)
```

We can also access the user's tasks

```python
# temporary_route

  print("found_user.tasks")
  print(found_user.tasks)
```

## Summary

ORM's provide us with an interface to communicate with databases without the need to write SQL code in our app.

SqlAlchemy is the most popular ORMs used with Python and can provide us with a number of methods to query the database

Migration is an important part of developing a database as this allows us to track changes to the database structure through migration scripts.
