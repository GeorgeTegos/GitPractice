from flask import Blueprint, render_template, request, redirect
from models import Task, User
from app import db

tasks_blueprint = Blueprint("tasks", __name__)

# INDEX
# GET '/tasks'
@tasks_blueprint.route("/tasks")
def tasks():
    # TODO: get all tasks, store it in a variable `tasks`
    return render_template("tasks/index.html", all_tasks = tasks)

# NEW
# GET '/tasks/new'
@tasks_blueprint.route("/tasks/new", methods=['GET'])
def new_task():
    # TODO: get all users, store them in a variable `users`
    return render_template("tasks/new.html", all_users = users)

# CREATE
# POST '/tasks'
@tasks_blueprint.route("/tasks",  methods=['POST'])
def create_task():
    description = request.form['description']
    user_id     = request.form['user_id']
    duration    = request.form['duration']
    completed   = request.form.get('completed') != None
    # TODO: create a new Task object using keyword arguments
    # TODO: add it with db.session
    # TODO: commit the db.session
    return redirect('/tasks')


# SHOW
# GET '/tasks/<id>'
@tasks_blueprint.route("/tasks/<id>", methods=['GET'])
def show_task(id):
    # TODO: get a task by id, store it in a variable `task`
    return render_template('tasks/show.html', task = task)

# EDIT
# GET '/tasks/<id>/edit'
@tasks_blueprint.route("/tasks/<id>/edit", methods=['GET'])
def edit_task(id):
    # TODO: get a task by id, store it in a variable `task`
    # TODO: get all users, store them in a variable `users`
    return render_template('tasks/edit.html', task = task, all_users = users)

# UPDATE
# POST '/tasks/<id>'
@tasks_blueprint.route("/tasks/<id>", methods=['POST'])
def update_task(id):
    description = request.form['description']
    user_id     = request.form['user_id']
    duration    = request.form['duration']
    completed   = 'completed' in request.form
    # TODO: get a task by id, store it in a variable `task`
    # TODO: set all the task properties with the form values
    # TODO: commit the db.session
    return redirect('/tasks')

# DELETE
# POST '/tasks/<id>/delete'
@tasks_blueprint.route("/tasks/<id>/delete", methods=['POST'])
def delete_task(id):
    # TODO: get a task by id
    # TODO: delete the task using db.session
    # TODO: commit the db.session
    return redirect('/tasks')