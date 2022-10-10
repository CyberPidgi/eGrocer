import tkinter as tk
from Database import Database

cleared = False


def successful_purchase():
    root = tk.Tk()
    root.title("Successful Purchase")
    tk.Label(root, text="Your Purchase has been Successful!").grid(row=0, column=0)
    tk.Label(root, text="Thank you for shopping with us!").grid(row=1, column=0)
    Database.clear_table("cart")
    root.mainloop()


def checkout_window():
    master = tk.Tk()
    data = Database.get_column_data("cart", "total_price")
    total_price = str(sum([float(price) for price in data]))
    tk.Label(master, text=f"Total Price: ${total_price}").grid(row=0, column=0)
    tk.Label(master, text="Only Cash On Delivery!").grid(row=1, column=0)
    tk.Button(master, text="Buy", command=lambda: master.destroy()).grid(row=2, column=0)
    master.mainloop()
    successful_purchase()


if __name__ == "__main__":
    checkout_window()