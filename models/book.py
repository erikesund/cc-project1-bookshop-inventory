class Book:
  def __init__(self, title, author, genre, quantity, buy_price, sell_price, publisher, isbn, book_format, id = None):
    self.title = title
    self.author = author
    self.id = id
    self.genre = genre
    self.quantity = quantity
    self.buy_price = buy_price
    self.sell_price = sell_price
    self.publisher = publisher
    self.isbn = isbn
    self.book_format = book_format
    self.id = id

  def calculate_markup():
    pass

  def change_quantity():
    pass

  def stock_status():
    pass