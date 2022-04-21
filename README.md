# Airline-Project

By: Evan Swett, AJ Abam, and Henock Zemenfes

Run Server:
```python3 manage.py runserver```

Create Virtual Environment: 
```python3 -m venv virtual_environment```

Make Migrations:
```python models.py makemigrations```

To login as admin:
email: admin@example.com
Password: admin


Each user is a Django User object with an:
-id
-name
-email
-DOB
-password
-group -> permissions

The User/permission structure is as follows:
Each user has a set of default attributes like name, email, DOB, a password, a unique ID assigned on instantiation, and one attribute that is reserved for a 'group' that they belong in.
We have 4 different groups: First class, coach, flight attendant and pilot
A 'Group' represents a subset of users that have specific permissions. One group can have more than one Permission object assigned to it. Those permissions are granted to every user that belongs in that group.
A 'Permission' object consists of a name and a 'ContentType'
The 'ContentType' points to the Model (SQLite3 table) that a permitted user needs to access
Our four different groups have uses for different data, so being assigned to a group allows for this functionality

For example: The coach and pilot do not need to access a database of desserts, but a first class user needs permission to order them. Likewise a flight attendant needs to know what desserts to bring on the plane so they need access as well.
User:
```id```
```name```
```email```
```DOB```
```password```
