import tkinter as tk
from tkinter import ttk
from shopping_cart2 import shopping_cart_page
from Database import Database

tree = None
products = []
PRODUCT_KEYS = Database.get_column_names("products")


def get_quantity():
    
    # open a new window to get the quantity of the product required
    master = tk.Tk()
    quantity = tk.StringVar(master, value="")
    master.title("Quantity")
    tk.Label(master, text="Enter Quantity: ").grid(row=0, column=0)
    
    entry = tk.Entry(master, textvariable=quantity)
    entry.grid(row=0, column=1)
    
    # Destroy the window after ENTER key is pressed
    entry.bind("<Return>", lambda event: master.destroy())
    master.mainloop(1)

    return int(quantity.get())

    
def add_to_cart():
    
    index = tree.focus()
    if not index:
        # if no item was selected, return
        return
    index = int(index[-1]) - 1
    
    item = products[index]
    if not item["item_name"] in Database.get_column_data("cart", "item_name"):
        # initially the customer has not bought anything
        # so set qty and total_price to 0
        data = [item["item_name"], 0, item["unit_price"], 0]
        Database.insert_data("cart", data)
    
    quantity = get_quantity()
    Database.update_column_with_condition("cart", "qty", quantity, condition=f"item_name = '{item['item_name']}'")
    Database.update_column_with_condition("cart", "total_price", 
                                          quantity * float(item["unit_price"]), condition=f"item_name = '{item['item_name']}'")
    

def display_products(master):
    global tree
    
    scrollbar = tk.Scrollbar(master)
    scrollbar.grid(row=1, column=1, sticky="ns")
    tree = ttk.Treeview(master, columns=["c" + str(i) for i in range(1, len(PRODUCT_KEYS) + 1)], show="headings")
    
    for i in range(1, len(PRODUCT_KEYS) + 1):
        tree.column(f"# {i}", anchor=tk.CENTER, width=90)
        tree.heading(f"# {i}", text=PRODUCT_KEYS[i - 1])
        
    for product in products:
        tree.insert('', "end", values=tuple(product.values()))
    
    tree.grid(row=1, column=0, sticky="nsew")
    scrollbar.config(command=tree.yview)


def search_product(master, search_text):
    global products
    
    all_products = Database.get_data("products")
    searched_products = []
    for product in all_products:
        
        # check if what the customer searched for is in the product name
        if not search_text.get() in product[0].lower():
            continue
        
        # convert the product to a dictionary
        product_dict = {key: value for key, value in zip(PRODUCT_KEYS, product)}
        searched_products.append(product_dict)
    products = searched_products
    
    display_products(master)
    
    
def open_cart(master):
    global cleared 
    master.destroy()
    Database.delete_record("cart", condition="qty = 0")
    shopping_cart_page(shopping_window)
    
    
def shopping_window():
    root = tk.Tk()
    root.title("Shopping Page")
    
    search_text = tk.StringVar(root, value="")
    tk.Entry(root, textvariable=search_text).grid(row=0, column=0)
    tk.Button(root, text="Search", command=lambda: search_product(root, search_text)).grid(row=0, column=1)
    tk.Button(root, text="Add to Cart", command=add_to_cart).grid(row=0, column=2)
    tk.Button(root, text="See Cart", command=lambda: open_cart(root)).grid(row=1, column=2)
    root.mainloop()
    
    return True    
    
if __name__ == "__main__":
    shopping_window()
    Database.clear_table("cart")
