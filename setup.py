from Database import Database
from encrypt_password import encrypt_password

db, cursor = Database.db, Database.cursor
db.autocommit = True


def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS login (username varchar(30), password varchar(256), primary key (username));")
    cursor.execute("CREATE TABLE IF NOT EXISTS products(item_name varchar(30), category varchar(30), qty int, unit_price Decimal(7, 2));")
    cursor.execute("CREATE TABLE IF NOT EXISTS cart(item_name varchar(30), qty int, unit_price Decimal(7, 2), total_price Decimal(7, 2));")


def insert_login_values():
    command = "INSERT INTO login VALUES (%s, %s);"
    cursor.execute(command, ("Allen", encrypt_password("123")))


def add_products():
    command = "INSERT INTO products VALUES(%s, %s, %s, %s);"
    cursor.execute(command, ("Apple", "Fruits", 120, 1.25))
    cursor.execute(command, ("Orange", "Fruits", 100, 1.50))
    cursor.execute(command, ("Banana", "Fruits", 80, 1.75))
    cursor.execute(command, ("Grape", "Fruits", 60, 2.00))
    cursor.execute(command, ("Pineapple", "Fruits", 40, 2.25))
    cursor.execute(command, ("Mango", "Fruits", 20, 2.50))
    cursor.execute(command, ("Watermelon", "Fruits", 10, 2.75))
    cursor.execute(command, ("Cucumber", "Vegetables", 120, 3.25))
    cursor.execute(command, ("Tomato", "Vegetables", 100, 3.50))
    cursor.execute(command, ("Carrot", "Vegetables", 80, 3.75))
    cursor.execute(command, ("Potato", "Vegetables", 60, 4.00))
    cursor.execute(command, ("Onion", "Vegetables", 40, 4.25))
    cursor.execute(command, ("Cauliflower", "Vegetables", 20, 4.50))
    cursor.execute(command, ("Garlic", "Vegetables", 10, 4.75))
    cursor.execute(command, ("Chicken", "Meat", 120, 5.25))
    
    
if __name__ == "__main__":
    create_tables()
    insert_login_values()
    add_products()