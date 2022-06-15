from optparse import Values
from db.run_sql import run_sql
from models.ordered_book import OrderedBook
from models.book import Book
import repositories.book_repository as book_repository
from models.order import Order
import repositories.order_repository as order_repository

def save(ordered_book):
  sql = "INSERT INTO ordered_books (order_id, book_id) VALUES (%s, %s) RETURNING id"
  values = [ordered_book.order.id, ordered_book.book.id]
  results = run_sql(sql, values)
  id = results[0]["id"]
  ordered_book.id = id
  
def select_all():
  ordered_books = []
  sql = "SELECT * FROM ordered_books"
  results = run_sql(sql)
  for result in ordered_books:
    book = book_repository.select(result["book_id"])
    order = order_repository.select(result["order_id"])
    ordered_book = OrderedBook(order, book, result["id"])
    ordered_books.append(ordered_book)
  return ordered_books

def select(id):
  sql = "SELECT * FROM ordered_books WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  book = book_repository.select(result["book_id"])
  order = order_repository.select(result["order_id"])
  ordered_book = OrderedBook(order, book, result["id"])
  return ordered_book

def delete_all():
  sql = "DELETE FROM ordered_books"
  run_sql(sql)

def delete(id):
  pass

def update(ordered_books):
  pass