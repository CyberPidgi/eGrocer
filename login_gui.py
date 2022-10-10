import tkinter as tk
from Database import Database
from sign_up_page import sign_up_window
from encrypt_password import encrypt_password

cleared = False


def verify(username, password, master):
    global cleared
    username, password = username.get(), password.get()
    record = Database.get_specific_data("Login", "Username", username)
    
    if not record:  # if username is not in database, record will be empty
        return 
    if encrypt_password(password) == record[1]:
        cleared = True
        master.destroy()


def open_sign_up_window():
    global cleared
    cleared = sign_up_window()
    

def login_window():
    root = tk.Tk()
    root.title("Login")
    root.geometry("100x70")

    username = tk.StringVar(root, value="")
    password = tk.StringVar(root, value="")
    tk.Label(root, text="Username:").grid(row=0, column=0)
    tk.Label(root, text="Password:").grid(row=1, column=0)
    tk.Entry(root, textvariable=username).grid(column=1, row=0)
    entry = tk.Entry(root, textvariable=password)
    entry.grid(column=1, row=1)
    entry.config(show="*")
    tk.Button(root, text="Login", command=lambda: verify(username, password, root)).place(x=15, y=43)
    tk.Button(root, text="Sign Up", command=open_sign_up_window).place(x=65, y=43)
    root.mainloop()
    
    return cleared
    

if __name__ == "__main__":
    login_window()