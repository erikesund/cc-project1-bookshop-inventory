from flask import Flask, render_template

from controllers.book_controller import books_blueprint
from controllers.publisher_controller import publishers_blueprint
from controllers.order_controller import orders_blueprint
from controllers.ordered_book_controller import ordered_books_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint)
app.register_blueprint(publishers_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(ordered_books_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)