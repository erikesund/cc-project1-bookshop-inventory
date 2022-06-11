from flask import Flask, render_template, Blueprint, redirect, request

from models.book import Book
import repositories.book_repository as book_repository


books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books") #index
def books():
  books = book_repository.select_all()
  return render_template("books/index.html", books = books)

#show

#new

#create

#edit

#update

#delete