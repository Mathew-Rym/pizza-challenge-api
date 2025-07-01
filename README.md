# open Pizza Restaurants API

A simple Flask API to manage restaurants and their pizzas.

---

## Project Structure

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── server
    ├── app.py
    ├── controllers
    │   ├── __init__.py
    │   ├── pizza_controller.py
    │   ├── restaurant_controller.py
    │   └── restaurant_pizza_controller.py
    ├── instance
    │   └── app.db
    ├── migrations
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── README
    │   ├── script.py.mako
    │   └── versions
    │       └── 822baf8a8cae_initial_migrations.py
    ├── models
    │   ├── __init__.py
    │   ├── pizza.py
    │   ├── restaurant_pizza.py
    │   └── restaurant.py
    └── seed.py
```

---

## Setup Instructions

### 1. Clone the repo and navigate into the cloned repository
```bash
 git clone https://git@github.com:Mathew-Rym/pizza-challenge-api-v1.git
 cd pizza-api-challenge
```
---
### 2. Install dependencies using Pipenv

```bash 
pipenv install
```
---

### 3. Activate the virtual environment

```bash
pipenv shell
```
---

### 4. Set your Flask app


```bash
cd server
export FLASK_APP=app.py
```

---

### 5. Run database migrations

```bash
flask db upgrade head
```

---

### 6. Seed the database

```bash
python seed.py
```

---

### 7. Start the server

```bash
python app.py
```

Your API should now be running at [http://127.0.0.1:5555](http://127.0.0.1:5555) by default.

---


## Testing with Postman

1. Open Postman.
2. Create new request by clicking the '+' icon in the top left.
3. Enter URL which is `http://127.0.0.1:5555`.
4. Test with the following endpoints:


| Method | Endpoint             | Description                            |
| ------ | -------------------- | -------------------------------------- |
| GET    | `/restaurants`       | Get all restaurants                    |
| GET    | `/restaurants/<id>`  | Get a specific restaurant by ID        |
| DELETE | `/restaurants/<id>`  | Delete a restaurant by ID              |
| GET    | `/pizzas`            | Get all pizzas                         |
| GET    | `/restaurant_pizzas` | Get all restaurant-pizza               |
| POST   | `/restaurant_pizzas` | Create a restaurant-pizza relationship |

---

##  Notes

* Make sure your database is migrated **and seeded** before running.
* Update the port in Postman requests if your Flask app uses a different port.

---

## Requirements

* Python 3.x
* Pipenv
* Flask
* Flask-Migrate
* SQLAlchemy

---
