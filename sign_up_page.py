import tkinter as tk
from Database import Database
from encrypt_password import encrypt_password

cleared = False


def add_new_login(username, password, c_password, master):
    global cleared
    username, password = username.get(), password.get()
    if password != c_password.get():
        c_password.set("")
        print("Passwords do not match")
        return
    Database.insert_data("Login", (username, encrypt_password(password)))
    master.destroy()
    cleared = True
    

def sign_up_window():
    root = tk.Tk()
    root.title("Login")
    root.geometry("150x90")

    username = tk.StringVar(root, value="")
    password = tk.StringVar(root, value="")
    confirmed_password = tk.StringVar(root, value="")
    tk.Label(root, text="New Username:").grid(row=0, column=0)
    tk.Label(root, text="New Password:").grid(row=1, column=0)
    tk.Label(root, text="Confirm Password:").grid(row=2, column=0)
    tk.Entry(root, textvariable=username).grid(column=1, row=0)
    entry = tk.Entry(root, textvariable=password)
    entry.grid(column=1, row=1)
    entry.config(show="*")
    confirm_p = tk.Entry(root, textvariable=confirmed_password)
    confirm_p.grid(column=1, row=2)
    confirm_p.config(show="*")
    
    tk.Button(root, text="Sign Up", command=lambda: add_new_login(username, password, confirmed_password, root)).place(x=45, y=62)
    root.mainloop()
    
    return cleared
    

if __name__ == "__main__":
    sign_up_window()