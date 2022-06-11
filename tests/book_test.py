import unittest
from models.book import Book
from models.publisher import Publisher

class TestBook(unittest.TestCase):
  def setUp(self):
    self.publisher = Publisher("HarperCollins Publishers Ltd", "103 Westerhill Road, Bishopbriggs, Glasgow, G64 2QT.", "0141 306 3100")
    publisher = self.publisher
    self.book = Book("The Lord of the Rings", "JRR Tolkien", "fantasy", 9, 8.50, 16.99, publisher, "9780261102385", "paperback")

  def test_calculate_markup(self):
    self.book.calculate_markup()
    self.assertEqual(8.49, self.book.calculate_markup())

  def test_change_guantity(self):
    pass

  def test_stock_status_normal(self):
    self.book.stock_status()
    self.assertEqual("stock_high", self.book.stock_status())

  def test_stock_status_low(self):
    self.book.stock_status()
    self.assertEqual("stock_low", self.book.stock_status())
  

  def test_out_of_stock(self):
    self.book.stock_status()
    self.assertEqual("out_of_stock", self.book.stock_status())
