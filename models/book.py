class Book:
  def __init__(self, title, author, genre, quantity, buy_price, sell_price, publisher, isbn, book_format, id = None):
    self.title = title
    self.author = author
    self.genre = genre
    self.quantity = quantity
    self.buy_price = buy_price
    self.sell_price = sell_price
    self.publisher = publisher
    self.isbn = isbn
    self.book_format = book_format
    self.id = id

  def calculate_markup(self):
    markup_float = (self.sell_price) - (self.buy_price)
    markup_float = round(markup_float, 2)
    markup_string = format(markup_float, '.2f')
    return markup_string

  def stock_status(self):
    if self.quantity == 0:
      return "out_of_stock"
    if self.quantity >= 5:
      return "stock_high"
    elif self.quantity < 5:
      return "stock_low"
  
  # def change_quantity(): should this be handled by the db?
  #   pass