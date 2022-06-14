from db.run_sql import run_sql
from models.ordered_books import OrderedBooks
from models.book import Book
import repositories.book_repository as book_repository
from models.order import Order
import repositories.order_repository as order_repository

def save(ordered_books):
  sql = "INSERT INTO ordered_books (order_id, book_id) VALUES (%s, %s) RETURNING id"
  values = [ordered_books.book.id, ordered_books.order.id]
  results = run_sql(sql, values)
  id = results[0]["id"]
  ordered_books.id = id
  
def select_all():
  pass

def select(id):
  pass

def delete_all():
  sql = "DELETE FROM ordered_books"
  run_sql(sql)

def delete(id):
  pass

def update(ordered_books):
  pass