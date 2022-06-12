from flask import Flask, render_template, Blueprint, redirect, request

from models.book import Book
from models.publisher import Publisher
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository


books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books") #index
def books():
  books = book_repository.select_all()
  return render_template("books/index.html", books = books)

@books_blueprint.route("/books/<id>") #show - this is not working
def show_book(id):
  book = book_repository.select(id) 
  publisher = publisher_repository.select(book.publisher.id)
  return render_template("/books/show.html", book = book, publisher = publisher)

#new
@books_blueprint.route("/books/new")
def new_book():
  publishers = publisher_repository.select_all()
  books = book_repository.select_all()
  return render_template("/books/new.html", publishers = publishers, books = books)


@books_blueprint.route("/books", methods = ["POST"]) #create
def create_book():
  title = request.form["title"]
  author = request.form["author"]
  genre = request.form["genre"]
  quantity = request.form["quantity"]
  buy_price = request.form["buy_price"]
  sell_price = request.form["sell_price"]
  publisher_id = request.form["publisher_id"]
  publisher = publisher_repository.select(publisher_id) #this line is not right?
  isbn = request.form["isbn"]
  book_format = request.form["book_format"]
  new_book = Book(title, author, genre, quantity, buy_price, sell_price, publisher, isbn, book_format)
  book_repository.save(new_book)
  return redirect("/books")

@books_blueprint.route("/books/<id>/edit") #edit
def edit_book(id):
  book = book_repository.select(id)
  publishers = publisher_repository.select_all()
  return render_template("/books/edit.html", book = book, publishers = publishers)

@books_blueprint.route("/books/<id>", methods = ["POST"]) #update
def update_book(id):
  title = request.form["title"]
  author = request.form["author"]
  genre = request.form["genre"]
  quantity = request.form["quantity"]
  buy_price = request.form["buy_price"]
  sell_price = request.form["sell_price"]
  publisher_id = request.form["publisher_id"]
  publisher = publisher_repository.select(publisher_id) #this line is not right?
  isbn = request.form["isbn"]
  book_format = request.form["book_format"]
  book = Book(title, author, genre, quantity, buy_price, sell_price, publisher, isbn, book_format, id)
  book_repository.update(book)
  return redirect("/books")


@books_blueprint.route("/books/<id>/delete", methods = ["POST"]) #delete
def delete_book(id):
  book_repository.delete(id)
  return redirect("/books")