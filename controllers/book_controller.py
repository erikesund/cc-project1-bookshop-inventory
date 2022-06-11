from flask import Flask, render_template, Blueprint

from models.book import Book
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
  # publishers = publisher_repository.select_all()
  books = book_repository.select_all()
  return render_template("books/index.html", books = books)