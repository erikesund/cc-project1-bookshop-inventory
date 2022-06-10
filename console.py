import pdb
from models.book import Book
from models.publisher import Publisher

import repositories.book_repository as book_repository
import repositories. publisher_repository as publisher_repository

book_repository.delete_all()
publisher_repository.delete_all()

publisher1 = Publisher("HarperCollins Publishers Ltd", "103 Westerhill Road, Bishopbriggs, Glasgow, G64 2QT.", "0141 306 3100")
publisher_repository.save(publisher1)

publisher2 = Publisher("Penguin Books Ltd", "One Embassy Gardens, 8 Viaduct Gardens, London, SW11 7BW.", "020 7139 3000")
publisher_repository.save(publisher2)

book1 = Book("The Lord of the Rings", "JRR Tolkien", "fantasy", 9, 8.50, 16.99, publisher1, "9780261102385", "paperback")
book_repository.save(book1)

pdb.set_trace()