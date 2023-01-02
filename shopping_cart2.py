import tkinter as tk
from tkinter import ttk
from Database import Database

total_price = 0
ITEM_KEYS = Database.get_column_names("cart")
price_label = None
tree = None


def change_quantity(cart_master):
    master = tk.Tk()
    
    index = tree.focus()
    if not index:
        return
    index = int(index[-1]) - 1
    
    product = dict(zip(ITEM_KEYS, tree.item(tree.focus())["values"]))
    tk.Label(master, text="Old Quantity:").grid(row=0, column=0)
    tk.Label(master, text=product["qty"]).grid(row=0, column=1)
    
    new_quantity = tk.StringVar(master, value="")
    master.title("Quantity")
    tk.Label(master, text="Enter New Quantity: ").grid(row=1, column=0)
    entry = tk.Entry(master, textvariable=new_quantity)
    entry.grid(row=1, column=1)
    item_name, unit_price = product["item_name"], float(product["unit_price"])
    entry.bind("<Return>", lambda event: (master.destroy(),
                                          Database.update_column_with_condition("cart", 
                                                    "qty", int(new_quantity.get()), condition=f"item_name = '{item_name}'"),
                                           Database.update_column_with_condition("cart", 
                                                    "total_price", int(new_quantity.get()) * unit_price, 
                                                    condition=f"item_name = '{item_name}'"),
                                          display_cart(cart_master),
                                          display_total_price(cart_master)
                                          ))
    
    master.mainloop(3)
    

def display_total_price(master):
    global total_price, price_label
    data = Database.get_column_data("cart", "total_price")
    total_price = str(sum([float(price) for price in data]))
    
    try:
        price_label.destroy()
    except (tk.TclError, AttributeError):
        pass
    price_label = tk.Label(master, text="$" + total_price)
    price_label.grid(row=2, column=2) 
    

def remove_item(cart_master):
    item_name = tree.item(tree.selection())["values"][0]
    Database.delete_record("cart", f"item_name = '{item_name}'")
    tree.delete(tree.selection()[0])
    display_total_price(cart_master)

    
def display_cart(master):
    global tree
    scrollbar = tk.Scrollbar(master)
    scrollbar.grid(row=1, column=1, sticky="ns")
    tree = ttk.Treeview(master, columns=["c" + str(i) for i in range(1, len(ITEM_KEYS) + 1)], show="headings")
    
    for i in range(1, len(ITEM_KEYS) + 1):
        tree.column(f"# {i}", anchor=tk.CENTER, width=90)
        tree.heading(f"# {i}", text=ITEM_KEYS[i - 1])
        
    for item in Database.get_data("cart"):
        tree.insert('', "end", values=item)
    
    tree.grid(row=1, column=0, sticky="nsew")
    scrollbar.config(command=tree.yview)
    

def shopping_cart_page(prev_window_func, mainloop_index=2):
    master = tk.Tk()
    master.title("Shopping Cart")

    tk.Button(master, text="Go Back", command=lambda: (master.destroy(), prev_window_func())).grid(row=0, column=0)
    tk.Button(master, text="Checkout", command=lambda: master.destroy()).grid(row=0, column=1)
    tk.Button(master, text="Change Quantity", 
              command=lambda: change_quantity(master)).grid(row=0, column=2)
    tk.Button(master, text="Remove Item", command=lambda: remove_item(master)).grid(row=2, column=0)
    tk.Label(master, text="Total Price:").grid(row=2, column=1)
    display_cart(master)
    display_total_price(master)

    master.mainloop(mainloop_index)
    

if __name__ == "__main__":
    shopping_cart_page(lambda: None,  0)