from db.run_sql import run_sql
from models.order import Order
from models.book import Book
import repositories.book_repository as book_repository

def save(order):
  sql = "INSERT INTO orders (customer, status) VALUES (%s, %s) RETURNING id"
  values = [order.customer, order.status]
  results = run_sql(sql, values)
  id = results[0]["id"]
  order.id = id

def select_all():
  orders = []
  sql = "SELECT * FROM orders"
  results = run_sql(sql)
  for result in results:
    order = Order(result["customer"], result["status"], result["id"])
    orders.append(order)
  return orders

def select(id):
  sql = "SELECT * FROM orders WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  order =  Order(result["customer"], result["status"], result["id"])
  return order

def delete_all():
  sql = "DELETE FROM orders"
  run_sql(sql)

def delete(id):
  sql = "DELETE FROM orders WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def update(order):
  pass