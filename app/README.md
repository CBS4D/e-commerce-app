# Shopping Cart  
1. A simple E-commerce app using FlaskRestful.
2. Postman Collection - [Download](https://api.postman.com/collections/8868957-01fea58a-7a84-4aeb-9491-6729c073a2c1?access_key=PMAT-01GYXRH0BA43KDE8P184V3BPN7)
  
## Dependencies ##
1. Python3
2. Flask
3. Sqlite

## Pipenv instructions ##
1. Install virtualenv (pip install virtualenv)
2. Activate encironment (.\vnv\Scripts\activate)
3. Install dependencies (pipenv install -r requirements.txt)

## How to run ##
1. python main.py
2. Enter localhost:5000 in the browser.

# Functionality on Order/OrderItem/Product entity
  - Order Entity, Order Item Entity and Product Entity.
  - CRUD operation are there for Product Entity.
  - Apart from CRUD we have search product endpoint where othere functionality is icluded like - search by name, order by name/price/created_date, specify order like ascending or discending.
  - For Order entity we have similar search functionality as we have for products.
  - We can create and fetch order item entity.