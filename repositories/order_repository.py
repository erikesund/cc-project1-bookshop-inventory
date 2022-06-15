from db.run_sql import run_sql
from models.order import Order
from models.book import Book
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

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

def select_books_in_order(id):
  books = []
  sql = "SELECT books.* FROM books INNER JOIN ordered_books ON ordered_books.book_id = books.id WHERE ordered_books.order_id = %s"
  values = [id]
  results = run_sql(sql, values)
  for result in results:
    publisher = publisher_repository.select(result["publisher_id"])
    book = Book(result["title"], result["author"], result["genre"], result["quantity"], result["buy_price"], result["sell_price"], publisher, result["isbn"], result["book_format"], result["id"])
    books.append(book)
  return books