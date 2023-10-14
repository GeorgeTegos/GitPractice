# Many to many associations

## Objectives

* Have an awareness of the different types of relationships that exist in a relational database
* Describe and provide an example of a many to many relationship and when we would use one
* Draw and 'model' many to many relationship

## Recap

Until now we have learned 2 associations:

* one to one; for example a Person and NI number
* one to many; Team has many players; Bank has many accounts...

There is one other relationship we need to learn about.

## Many to many

When modelling data there will be occasions when one or more rows in a table are associated with one or more rows in another table.

For example:

> DRAW ON BOARD:

Let's say we are going to build a review site for travellers to show locations that they have visited and include reviews. A location can be visited by many users, and a user can visit many locations. I could visit Paris, London and New York, and Paris could be visited by me, you and someone else.

User:

* name

Location:

* name
* category (e.g. restaurants, hotels, attractions, museums)

When we have a many to many association like this we require a third table in the mix. We call this a join table. A join table will have two foreign keys; one for each model. It will also have its own ID, and can contain extra fields.

So we need a third model. General convention is that if there is no better name for it, we give it the name table1_table2. For our example, 'visits' is probably a good name, but we could call it 'users_locations'.

Visit:

* id
* user_id
* location_id
* review

Here's the twist.. we're going to make this a bit more fun and imagine this review site is for fantasy characters, and it's going to be called QuestAdvisor.

## Models and our database

> Hand out Quest_Advisor_start code.

Now let's start by creating our database:

```bash
#terminal

dropdb quest_advisor
createdb quest_advisor
flask db init
flask db migrate
flask db upgrade
flask db seed
```

## In-depth with the join model

If you look at a single location or user at the moment we havea TODO message. `/locations/1` for example requires us to complete the route and respond with a template with the location name and the users that have visited that location. 

Likewise the users page requires us to complete the route and respond with a template with the user name and the locations that they have visited.

## SQL Joins

In order to retrieve the data we need from the database we need to do an SQL join. For example:

```sql
SELECT users.name
FROM users

-- Join the visits table
JOIN visits 
ON visits.user_id = users.id

-- Join the locations table (we need the name)
JOIN locations
ON visits.location_id = locations.id

-- Only for location 1
WHERE location_id = 1
```

And vice-versa for the user:

```sql
-- What columns do we need?
SELECT locations.name 
FROM locations

-- Join the visits table
JOIN visits
ON visits.location_id = locations.id

-- Join locations table (we need the name)
JOIN users
ON visits.user_id = users.id

-- Only for user 1
WHERE user_id = 1
```

So this is what we would write if we were communicating directly with a database. 

BUT, we are going to get SQLAlchemy to do the heavy lifting. In our locations route, we want to execute the SQLAlchecmy code to retrieve the appropriate data.


```python
# location_controller.py

@locations_blueprint.route("/locations/<id>")
def show(id):
    location = Location.query.get(id)
    users = User.query.join(Visit).filter(Visit.location_id == id) # JOIN statement
    return render_template("locations/show.jinja", location=location, users=users)

```

```python
# user_controller.py 

@users_blueprint.route("/users/<id>")
def show(id):
    user = User.query.get(id)
    locations = Location.query.join(Visit).filter(Visit.user_id == id) # JOIN statement
    return render_template("users/show.jinja", user=user, locations=locations)
```


## Viewing the data

Great we can now see this data if we browse to `/locations/1` or `users/1`

```python
# user_controller.py

@users_blueprint.route("/users/<id>")
def show(id):
    user = user_repository.select(id)
    locations = user_repository.locations(user) # ADDED
    return render_template("users/show.html", user=user, locations = locations) # MODIFIED

```


## Summary

When we have a many-to-manyh relationship, we usually need to execute a JOIN at some point to get the data we need. This requires an SQL JOIN statement (also known as an INNER JOIN, same thing).

Since we are using SQLAlchemy, we passed it the responsibility for the JOIN query and executed it in our routes to return the data required. 