# backend-assignment
True Value Access - Backend Assignment
REST APIs using Python Django rest framework and PSQL database for managing the user’s data.

This API have following functionalities:

list users (/api/users GET)
search for a user by name
sort list by field name
pagination of users list
create new user (/api/users - POST)
get detail of a user (/api/users/<id> - GET)
update details of a user (/api/users/<id> - PUT)
delete a user (/api/users/<id> - DELETE)

How to setup and run this project:-
first install Django, Django rest framework, python decouple and psycopg2 or run requirement.txt.
create .env file configure secret key, debug, Database name, user,password and host.



## **Task Overview**

User have the following attributes:-

```
ID
First Name
Last Name
Company Name
Age
City
State
Zip
Email
Web
```

Application have the following endpoints:

- `/api/users - GET` - To list the users

  - Response with HTTP status code 200 on success

    ```json
    {
    "links": {
        "next": "http://127.0.0.1:8000/api/users?page=2"
    },
    "results": [
        {
            "id": 4,
            "first_name": "kans",
            "last_name": "hjkkj",
            "email": "kans@gmail.com",
            "age": 29,
            "company_name": "company_name",
            "city": "malappuram",
            "state": "Kerala",
            "web": "https://karshinas-kans.com/",
            "zip": 676776
        },
        {
            "id": 5,
            "first_name": "akkkik",
            "last_name": "kkkak",
            "email": "akkkik@gmail.com",
            "age": 46,
            "company_name": "company_ame",
            "city": "malappuram",
            "state": "Kerala",
            "web": "https://akkiki.app/",
            "zip": 679573
        }
    ]
}
    ```

  - page - a number for pagination
  - limit - no. of items to be returned, default limit is 5
  - name - search user by name as a substring in First Name or Last Name (Note, use substring matching algorithm/pattern to match the name). with case-insensitive.
  - Sort - name of attribute, the items to be sorted. By default it returns items in ascending order if this parameter exist, and if the value of parameter is prefixed with ‘-’ character, then it return items in descending order

  Sample query endpoint:- `/api/users?page=1&limit=10&search=James&sort=-age` This endpoint return list of 10 users whose first name or last name contains substring given name and sort the users by age in descending order of page 1.

- `/api/users - POST` - To create a new user

  - Request Payload is like in json format :-

    ```json
    {
      "id": 2,
      "first_name": "Josephine",
      "last_name": "Darakjy",
      "company_name": "Chanay, Jeffrey A Esq",
      "city": "Brighton",
      "state": "MI",
      "zip": 48116,
      "email": "josephine_darakjy@darakjy.org",
      "web": "http://www.chanayjeffreyaesq.com",
      "age": 48
    }
    ```

  - Response with HTTP status code 201 on success
    ```json
    {}
    ```
  - This endpoint will create a new user inside the database

- `/api/users/{id} - GET` - To get the details of a user

  1. Here {id} will be the id of the user in path parameter
  1. Response with HTTP status code 200 on success

  ```json
  {
    "id": 1,
    "first_name": "James",
    "last_name": "Butt",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutt@gmail.com",
    "web": "http://www.bentonjohnbjr.com",
    "age": 70
  }
  ```

  Sample query looks like:- `/api/users/1 GET`

- `/api/users/{id} PUT` - To update the details of a user

  - Here {id} will be the id of the user in path parameter
  - Request Payload is like in json format for updating first name, last name and age:-
    ```json
    {
      "first_name": "Josephine",
      "last_name": "Darakjy",
      "age": 48
    }
    ```
  - Response with HTTP status code 200 on success
    {}

- `/api/users/{id} DELETE` - To delete the user

  - Here {id} will be the id of the user in path parameter
  - Response with HTTP status code 200 on success

    ```json
    {}
    ```
