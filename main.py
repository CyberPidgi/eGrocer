from login_gui import login_window
from shopping_page2 import shopping_window
from checkout import checkout_window

customer_window_queue = [login_window, shopping_window, checkout_window]
for window in customer_window_queue:
    cleared = window()
    if not cleared:
        break