from flask import Flask, Blueprint, redirect, render_template, request

from models.ordered_book import OrderedBook
import repositories.ordered_book_repository as ordered_book_repository
import repositories.book_repository as book_repository
import repositories.order_repository as order_repository

ordered_books_blueprint = Blueprint("ordered_books", __name__)

@ordered_books_blueprint.route("/ordered_books") #index
def ordered_books():
  ordered_books = ordered_book_repository.select_all()
  return render_template("/ordered_books/index.html", ordered_books = ordered_books)