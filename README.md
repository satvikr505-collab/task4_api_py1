# Flask User REST API

## Project Overview

This project is a simple REST API developed using Python and Flask.

The API manages user data and provides endpoints for creating, viewing, updating, and deleting users.

## Technologies Used

* Python
* Flask
* REST API
* JSON
* Postman

## Features

* Get all users
* Get a single user
* Create a new user
* Update an existing user
* Delete a user
* Basic error handling
* HTTP status codes

## API Endpoints

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/`           | API welcome message |
| GET    | `/users`      | Get all users       |
| GET    | `/users/<id>` | Get one user        |
| POST   | `/users`      | Create a new user   |
| PUT    | `/users/<id>` | Update a user       |
| DELETE | `/users/<id>` | Delete a user       |

## Example POST Request

```json
{
    "name": "Amit",
    "email": "amit@gmail.com"
}
```

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Create a virtual environment.
4. Activate the virtual environment.
5. Install the required packages.

```bash
pip install -r requirements.txt
```

6. Run the Flask application.

```bash
python app.py
```

7. Open the API in a browser or Postman.

```text
http://127.0.0.1:5000
```

## Testing

The API was tested using Postman with GET, POST, PUT and DELETE requests.

## Storage

For this internship task, user data is stored temporarily in an in-memory Python list. The data will reset when the Flask application is restarted.

## Learning Outcome

This project helped me understand Flask application structure, REST APIs, HTTP methods, routes, JSON requests and responses, status codes, and API testing.
