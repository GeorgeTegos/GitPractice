# Using Loops to Search Lists

**Lesson Duration: 30 minutes**

### Learning Objectives
- Understand how to use a loop to search through a list

## Combining Loops, Lists & Dictionaries

Often we will find that we need to find a specific element of a list using a loop. Let's say we wanted to find a chicken object if we're given the name of the chicken.

Consider the following. Why would it not behave as we expect?

```python
# search_funcion.py

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

for chicken in chickens:
  if chicken["name"] == "Audrey":
    print(chicken)
  else:
    print("Audrey not found")
```

If we try it with "Margaret", it works! But if we try it with any other name, it doesn't. Why?

The code will **always** return after the first iteration of the loop. It doesn't matter if the chicken is found or not. So we end up checking the first item in the list but not the others.

# The Fix

How do we fix it? We could get rid of the else and return outside the loop.

```python
for chicken in chickens:
  if chicken["name"] == "Audrey":
    print(chicken)

print("Audrey not found")
```

Another solution would be to create a variable to return and set it if we find the chicken.

```python
result = "chicken not found"
for chicken in chickens:
  if chicken["name"] == "Audrey":
    result = chicken

print(result)
```

# Try it for yourself

Given a list of users, write a loop to find a user by id. Test your code works with a specific id (e.g. 4).

```python
users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
]
```

### Solution

```python
found_user = None
for user in users:
  if user["user_id"] == 4:
    found_user = user

print(found_user)
```
