from db.run_sql import run_sql
from models.book import Book
import repositories.publisher_repository as publisher_repository


def save(book):
  sql = "INSERT INTO books (title, author, genre, quantity, buy_price, sell_price, publisher_id, isbn, book_format) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
  values = [book.title, book.author, book.genre, book.quantity, book.buy_price, book.sell_price, book.publisher.id, book.isbn, book.book_format]
  results = run_sql(sql, values)
  book.id = results[0]["id"]
  return book

def select_all():
  books = []
  sql = "SELECT * FROM books"
  results = run_sql(sql)
  for row in results:
    publisher = publisher_repository.select(row["publisher_id"])
    book = Book(row["title"], row["author"], row["genre"], row["quantity"], row["buy_price"], row["sell_price"], publisher, row["isbn"], row["book_format"])
    books.append(book)
  return books

def delete_all():
  sql = "DELETE FROM books"
  run_sql(sql)