# Flask SQLAlchemy Practice

Complete each of the TODOs in the `tasks_controller.py` file

The CRUD Actions with SQLAlchemy are:


## Read

Reading doesn't make changes to the database, so we don't need to use `db.session.commit()`

```python
# get all tasks
Task.query.all()

# get task with id = 1
Task.query.get(1) 
```

## Create

```python
# create with Task class and keyword arguments
task = Task(description='sleep', duration='480')
db.session.add(task)
db.session.commit()
```

## Update

```python
# set new property values
task.description = 'wake up'
task.duration = '1'
db.session.commit()
```

## Delete

```python
db.session.delete(task)
db.session.commit()
```