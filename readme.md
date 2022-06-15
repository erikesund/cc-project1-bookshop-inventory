# Bookshop Inventory Project
## How to Run

Download the zip file from github and install in a location of your choice.
Once downloaded, in the terminal, navigate to the main folder. You will need to run the following commands in the terminal:

1. "psql -d bookshop_inventory -f db/bookshop_inventory.sql"
2. "python3 console.py"
3. "flask run"

Once this is done you will be able to either navigate to http://127.0.0.1:5000 in your browser or hold control and click the link in the terminal window.

## The Brief

### Shop Inventory
Build an app to aid a shopkeeper in tracking their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop employees.

### MVP
- The inventory should track individual Products, including a name, description, quantity, buy_price, and sell_price.
- The inventory should track Manufacturers, including a name and any other appropriate details.
- The shop can sell anything you like, but you should be able to create and edit Manufacturers and Products separately.
- It may make more sense for a car shop to track manufacturers and models of cars, while a bookstore might sell books by author or publisher, and not by manufacturer. You are free to name classes and tables as appropriate for your project.
- Create an inventory page, listing all the details for the Products in stock in a single view.
- As well as showing stock quantity as a number, the app should indicate "low stock" and "out of stock" items to the user.
### Inspired By
eBay, Amazon, Magento

### Possible Extensions
- Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
- Calculate the markup on items in the store, and display it in the inventory
- Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.

## Technologies Used

Technologies used were:

- VSCode for the coding.
- Postico for testing the database.
- Tested on Google Chrome for Mac.
