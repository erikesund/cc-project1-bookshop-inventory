DROP TABLE IF EXISTS ordered_books;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS publishers;

CREATE TABLE publishers(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255),
  phone_number VARCHAR(255)
);

CREATE TABLE books(
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255),
  genre VARCHAR(255),
  quantity INT,
  buy_price FLOAT,
  sell_price FLOAT,
  publisher_id INT REFERENCES publishers (id),
  isbn VARCHAR(255),
  book_format VARCHAR(255)
  
);

CREATE TABLE orders(
  id SERIAL PRIMARY KEY,
  customer VARCHAR(255),
  status BOOLEAN 

);

CREATE TABLE ordered_books(
  id SERIAL PRIMARY KEY,
  order_id SERIAL REFERENCES orders(id),
  book_id SERIAL REFERENCES books(id)

);