import pdb
from models.book import Book
from models.publisher import Publisher
from models.order import Order

import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository
import repositories.order_repository as order_repository

book_repository.delete_all()
publisher_repository.delete_all()
order_repository.delete_all()

publisher1 = Publisher("HarperCollins Publishers Ltd", "103 Westerhill Road, Bishopbriggs, Glasgow, G64 2QT.", "0141 306 3100")
publisher_repository.save(publisher1)

publisher2 = Publisher("Penguin Books Ltd", "One Embassy Gardens, 8 Viaduct Gardens, London, SW11 7BW.", "020 7139 3000")
publisher_repository.save(publisher2)

publisher3 = Publisher("Hachette UK", "Carmelite House, 50 Victoria Embankment, London, EC4Y 0DZ", "020 3122 6000")
publisher_repository.save(publisher3)

publisher4 = Publisher("Transworld Publishers Ltd", "20 Vauxhaull Bridge Road, London, SW1V 2SA", "020 7840 8400")
publisher_repository.save(publisher4)

book1 = Book("The Lord of the Rings", "JRR Tolkien", "fantasy", 9, 8.50, 16.99, publisher1, "9780261102385", "paperback")
book_repository.save(book1)

book2 = Book("The Hobbit", "JRR Tolkien", "fantasy", 3, 4.00, 8.99, publisher1, "9780007458424", "paperback")
book_repository.save(book2)

book3 = Book("The Silmarillion", "JRR Tolkien", "fantasy", 0, 8.50, 16.99, publisher1, "9780008433956", "hardback")
book_repository.save(book3)

book4 = Book("The Girl with the Dragon Tattoo", "Steig Larsson", "crime", 12, 4.44, 8.99, publisher3, "9780857054036", "paperback")
book_repository.save(book4)

book5 = Book("Dracula", "Bram Stoker", "horror", 2, 7.50, 14.99, publisher2, "9780141196886", "hardback")
book_repository.save(book5)

book6 = Book("Thud!", "Terry Pratchett", "fantasy", 3, 4.40, 8.99, publisher4, "9780552167697", "paperback")
book_repository.save(book6)

order1 = Order("Customer 1 class placeholder", True)
order_repository.save(order1)

order2 = Order("Customer 2 class placeholder", True)
order_repository.save(order2)


pdb.set_trace()