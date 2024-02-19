# import sqlite3

# # Connect to SQLite database
# con = sqlite3.connect('gourmet.db')

# # Create tables
# con.execute("""
# CREATE TABLE IF NOT EXISTS customer (
#     user_id INTEGER PRIMARY KEY,
#     name TEXT,
#     username TEXT,
#     password TEXT,
#     mobilehp TEXT
# )
# """)

# con.execute("""
# CREATE TABLE IF NOT EXISTS custorder (
#     order_id INTEGER PRIMARY KEY,
#     order_date TEXT,
#     menu_cat TEXT,
#     menu_item TEXT,
#     total_item INTEGER,
#     total_payment REAL,
#     user_id INTEGER
# )
# """)

# # Function to read menu from file
# def read_menu(filename):
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#     menu = {}
#     category = ''
#     for line in lines:
#         if line.startswith('#'):
#             category = line[1:].strip()
#             menu[category] = []
#         else:
#             item, price = line.split('RM')
#             menu[category].append((item.strip(), float(price.strip())))
#     return menu

# # Function to register a new customer
# def register_customer(name, username, password, mobilehp):
#     con.execute("""
#     INSERT INTO customer (name, username, password, mobilehp)
#     VALUES (?, ?, ?, ?)
#     """, (name, username, password, mobilehp))
#     con.commit()

# # Function to login a customer
# def login_customer(username, password):
#     cursor = con.cursor()
#     cursor.execute("""
#     SELECT * FROM customer WHERE username = ? AND password = ?
#     """, (username, password))
#     return cursor.fetchone()

# # Function to create a new order
# def create_order(user_id, menu_cat, menu_item, total_item, total_payment):
#     con.execute("""
#     INSERT INTO custorder (order_date, menu_cat, menu_item, total_item, total_payment, user_id)
#     VALUES (datetime('now'), ?, ?, ?, ?, ?)
#     """, (menu_cat, menu_item, total_item, total_payment, user_id))
#     con.commit()

 
# # Function to view orders
# def view_orders(user_id):
#     cursor = con.cursor()
#     cursor.execute("""
#     SELECT * FROM custorder WHERE user_id = ?
#     """, (user_id,))
#     return cursor.fetchall()

# # Function to update an order
# def update_order(order_id, menu_cat, menu_item, total_item, total_payment):
#     con.execute("""
#     UPDATE custorder
#     SET menu_cat = ?, menu_item = ?, total_item = ?, total_payment = ?
#     WHERE order_id = ?
#     """, (menu_cat, menu_item, total_item, total_payment, order_id))
#     con.commit()

# # Function to cancel an order
# def cancel_order(order_id):
#     con.execute("""
#     DELETE FROM custorder WHERE order_id = ?
#     """, (order_id,))
#     con.commit()

# # Main function to run the system
# def main():
#     # Display menu of options
#     print("1. Register")
#     print("2. Login")

#     # Ask user to choose an option
#     option = int(input("Enter the number of the option you want to choose: "))

#     if option == 1:
#         # Ask user to register
#         name = input("Enter your name: ")
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         mobilehp = input("Enter your mobile number: ")
#         register_customer(name, username, password, mobilehp)
#         print('Registration successful. Please login.')
#         option = 2

#     if option == 2:
#         # Ask user to login
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         user = login_customer(username, password)
#         if user is None:
#             print('Login failed')
#             return

#         while True:
#             # Display menu of options
#             print("1. Create order")
#             print("2. View orders")
#             print("3. Update order")
#             print("4. Cancel order")
#             print("5. Exit")

#             # Ask user to choose an option
#             option = int(input("Enter the number of the option you want to choose: "))

#             # Read menu from file
#             menu = read_menu('menu.txt')

#             if option == 1:
#                 # Display menu
#                 for category, items in menu.items():
#                     print(f"{category}:")
#                     for item, price in items:
#                         print(f"  {item} - RM {price}")

#                 # Ask user to choose a category
#                 menu_cat = input("Enter the category of the item you want to order: ")

#                 # Ask user to choose an item
#                 menu_item = input("Enter the name of the item you want to order: ")

#                 # Ask user to choose quantity
#                 total_item = int(input("Enter the quantity of the item you want to order: "))

#                 # Calculate total payment
#                 for item, price in menu[menu_cat]:
#                     if item == menu_item:
#                         total_payment = price * total_item
#                         break

#                 # Create a new order
#                 create_order(user[0], menu_cat, menu_item, total_item, total_payment)

#             elif option == 2:
#                 # View orders
#                 orders = view_orders(user[0])
#                 for order in orders:
#                     print(order)

#             elif option == 3:
#                 # View orders
#                 orders = view_orders(user[0])
#                 for order in orders:
#                     print(order)

#                 # Ask user to choose an order to update
#                 order_id = int(input("Enter the ID of the order you want to update: "))

#                 # Ask user to input new details
#                 menu_cat = input("Enter the new category of the item: ")
#                 menu_item = input("Enter the new name of the item: ")
#                 total_item = int(input("Enter the new quantity of the item: "))
#                 total_payment = float(input("Enter the new total payment: "))

#                 # Update the order
#                 update_order(order_id, menu_cat, menu_item, total_item, total_payment)

#             elif option == 4:
#                 orders = view_orders(user[0])
#                 for order in orders:
#                     print(order)

#                 # Ask user to choose an order to cancel
#                 order_id = int(input("Enter the ID of the order you want to cancel: "))

#                 # Cancel the order
#                 cancel_order(order_id)
            
#             elif option == 5:
#                 break

# main()


# # =========================================== GUI ===================================================

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to SQLite database
con = sqlite3.connect('gourmet.db')

# Create tables
con.execute("""
CREATE TABLE IF NOT EXISTS customer (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    password TEXT,
    mobilehp TEXT
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS custorder (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT,
    menu_cat TEXT,
    menu_item TEXT,
    total_item INTEGER,
    total_payment REAL,
    user_id INTEGER
)
""")

# Function to read menu from file
def read_menu(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    menu = {}
    category = ''
    for line in lines:
        if line.startswith('#'):
            category = line[1:].strip()
            menu[category] = []
        else:
            item, price = line.split('RM')
            menu[category].append((item.strip(), float(price.strip())))
    return menu

def register_customer(name, username, password, mobilehp,window):
    if not name or not username or not password or not mobilehp:
        messagebox.showerror("Error", "All fields must be filled")
        return
    con.execute("""
    INSERT INTO customer (name, username, password, mobilehp)
    VALUES (?, ?, ?, ?)
    """, (name, username, password, mobilehp))
    con.commit()
    messagebox.showinfo("Success", "Registration successful")
    window.destroy()


def login_customer(username, password, window):
    if not username or not password:
        messagebox.showerror("Error", "All fields must be filled")
        return
    con.row_factory = sqlite3.Row  # Set the row_factory to sqlite3.Row
    cursor = con.cursor()
    cursor.execute("""
    SELECT * FROM customer WHERE username = ? AND password = ?
    """, (username, password))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Success", "Login successfuly")
        window.destroy()
        main_menu(dict(result))  # Convert the Row to a dictionary and show the main menu
    else:
        messagebox.showerror("Error", "Invalid username or password")

def calculate_total_payment(menu_cat, menu_item, total_item):
    total_payment = 0
    menu = read_menu('menu.txt') 
    for item, price in menu[menu_cat]:
        if item == menu_item:
            total_payment = price * int(total_item)
            break
    return total_payment

# Function to create a new order
def create_order(user, menu_cat, menu_item, total_item, window):
    try:
        total_payment = calculate_total_payment( menu_cat, menu_item, total_item)
        total_payment = round(total_payment, 2)
        con.execute("""
        INSERT INTO custorder (order_date, menu_cat, menu_item, total_item, total_payment, user_id)
        VALUES (datetime('now'), ?, ?, ?, ?, ?)
        """, (menu_cat, menu_item, total_item, total_payment, user.get('user_id')))
        con.commit()
        messagebox.showinfo("Success", "Created successfuly")
        window.destroy()  # Destroy the window after successful insert
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Function to view orders
def view_orders(user):
    cursor = con.cursor()
    cursor.execute("""
    SELECT * FROM custorder WHERE user_id = ?
    """, (user.get('user_id'),))
    return cursor.fetchall()

# Function to update an order
def update_order(order_id, menu_cat, menu_item, total_item,window):
    try:
        total_payment = calculate_total_payment( menu_cat, menu_item, total_item)
        total_payment = round(total_payment, 2)
        con.execute("""
            UPDATE custorder
            SET menu_cat = ?, menu_item = ?, total_item = ?, total_payment = ?
            WHERE order_id = ?
            """, (menu_cat, menu_item, total_item, total_payment, order_id))
        con.commit()
        messagebox.showinfo("Success", "Updated successfuly")
        window.destroy()  # Destroy the window after successful insert
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
   

# Function to cancel an order
def cancel_order(order_id, window):
    try:
        con.execute("""
        DELETE FROM custorder WHERE order_id = ?
        """, (order_id,))
        con.commit()
        messagebox.showinfo("Success", "Deleted successfuly")
        window.destroy()  # Destroy the window after successful insert
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_sales_data():
    # Connect to the database
    cursor = con.cursor()

    # Execute a query to get the sales data
    cursor.execute("""
        SELECT menu_item, SUM(total_item), SUM(total_payment)
        FROM custorder
        GROUP BY menu_item
    """)

    # Fetch all the rows
    sales_data = cursor.fetchall()  # Changed from con.fetchall() to cursor.fetchall()

    return sales_data

def print_sales():
    # Get the sales data
    sales_data = get_sales_data()

    # Open the sales.txt file in write mode
    with open('sales.txt', 'w') as f:
        # Write the header
        f.write("Item sales count Total\n")

        # Write the sales data
        for item, count, total in sales_data:
            f.write(f"{item} {count} RM {total}\n")

#==============================================FRAMES===========================================================
def register():
    # Create a new window
    register_window = tk.Toplevel()
    register_window.title("Register")

    # Create a frame
    frame = ttk.Frame(register_window, padding="10 20 10 20")
    frame.pack(fill='both', expand=True)

    # Create labels and entry fields
    name_label = ttk.Label(frame, text="Name:")
    name_entry = ttk.Entry(frame)
    username_label = ttk.Label(frame, text="Username:")
    username_entry = ttk.Entry(frame)
    password_label = ttk.Label(frame, text="Password:")
    password_entry = ttk.Entry(frame, show='*')
    mobilehp_label = ttk.Label(frame, text="Mobile number:")
    mobilehp_entry = ttk.Entry(frame)

    # Create register button
    register_button = ttk.Button(frame, text="Register", command=lambda: register_customer(name_entry.get(), username_entry.get(), password_entry.get(), mobilehp_entry.get(), register_window))

    # Arrange widgets in grid
    name_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    username_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    username_entry.grid(row=1, column=1, padx=5, pady=5)
    password_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
    password_entry.grid(row=2, column=1, padx=5, pady=5)
    mobilehp_label.grid(row=3, column=0, sticky='w', padx=5, pady=5)
    mobilehp_entry.grid(row=3, column=1, padx=5, pady=5)
    register_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

def login():
    # Create a new window
    login_window = tk.Toplevel()
    login_window.title("Login")

    # Create a frame
    frame = ttk.Frame(login_window, padding="10 20 10 20")
    frame.pack(fill='both', expand=True)

    # Create labels and entry fields
    username_label = ttk.Label(frame, text="Username:")
    username_entry = ttk.Entry(frame)
    password_label = ttk.Label(frame, text="Password:")
    password_entry = ttk.Entry(frame, show='*')

    # Create login button
    login_button = ttk.Button(frame, text="Login", command=lambda: login_customer(username_entry.get(), password_entry.get(), login_window))

    # Arrange widgets in grid
    username_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    username_entry.grid(row=0, column=1, padx=5, pady=5)
    password_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)
    login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def show_create_order(user):
    # Create a new window for the order form
    order_window = tk.Toplevel()
    order_window.title("Create Order")

    # Create a text widget to display the menu
    menu_text = tk.Text(order_window, width=40, height=10)
    menu_text.pack(padx=5, pady=5)

    # Read the menu from menu.txt
    menu = read_menu('menu.txt')

    # Format the menu and insert it into the text widget
    menu_str = ""
    for category, items in menu.items():
        menu_str += f"{category}:\n"
        for item, price in items:
            menu_str += f"  {item} - RM {price}\n"
    menu_text.insert('1.0', menu_str)

    # Create a form to order
    order_form = ttk.Frame(order_window, padding="10 20 10 20")
    order_form.pack(fill='both', expand=True)

    # Create a label and entry for the menu category
    menu_cat_label = ttk.Label(order_form, text="Menu Category:")
    menu_cat_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    menu_cat_entry = ttk.Entry(order_form)
    menu_cat_entry.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    # Create a label and entry for the menu item
    menu_item_label = ttk.Label(order_form, text="Menu Item:")
    menu_item_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
    menu_item_entry = ttk.Entry(order_form)
    menu_item_entry.grid(row=2, column=1, sticky='w', padx=5, pady=5)

    # Create a label and entry for the total item
    total_item_label = ttk.Label(order_form, text="Total Item:")
    total_item_label.grid(row=3, column=0, sticky='w', padx=5, pady=5)
    total_item_entry = ttk.Entry(order_form)
    total_item_entry.grid(row=3, column=1, sticky='w', padx=5, pady=5)

    # Create a button to submit the order
    submit_button = ttk.Button(order_form, text="Submit Order", command=lambda: create_order(user, menu_cat_entry.get(), menu_item_entry.get(), total_item_entry.get(), order_window))
    submit_button.grid(row=4, column=0, columnspan=2, sticky='w', padx=5, pady=5)

def show_view_orders(user):
    # Create a new window
    view_orders_window = tk.Toplevel()
    view_orders_window.title("View Orders")

    # Create a treeview widget
    tree = ttk.Treeview(view_orders_window)
    tree["columns"]=("order_id", "order_date", "menu_cat", "menu_item", "total_item", "total_payment")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("order_id", anchor=tk.W, width=100)
    tree.column("order_date", anchor=tk.W, width=130)
    tree.column("menu_cat", anchor=tk.W, width=100)
    tree.column("menu_item", anchor=tk.W, width=100)
    tree.column("total_item", anchor=tk.W, width=100)
    tree.column("total_payment", anchor=tk.W, width=100)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("order_id", text="Order ID", anchor=tk.W)
    tree.heading("order_date", text="Order Date", anchor=tk.W)
    tree.heading("menu_cat", text="Menu Category", anchor=tk.W)
    tree.heading("menu_item", text="Menu Item", anchor=tk.W)
    tree.heading("total_item", text="Total Item", anchor=tk.W)
    tree.heading("total_payment", text="Total Payment", anchor=tk.W)

    # Fetch data from the custorder table
    orders = view_orders(user)
    for order in orders:
        tree.insert("", "end", values=tuple(order))

    tree.pack()


def show_update_order(user):
    # Create a new window
    update_form = tk.Toplevel()
    update_form.title("Update Order")

    # Create a frame for the treeview and form
    tree_form_frame = ttk.Frame(update_form)
    tree_form_frame.grid(row=0, column=0, columnspan=2)

    # Create a treeview widget
    tree = ttk.Treeview(tree_form_frame)
    tree["columns"]=("order_id", "order_date", "menu_cat", "menu_item", "total_item", "total_payment")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("order_id", anchor=tk.W, width=100)
    tree.column("order_date", anchor=tk.W, width=130)
    tree.column("menu_cat", anchor=tk.W, width=100)
    tree.column("menu_item", anchor=tk.W, width=100)
    tree.column("total_item", anchor=tk.W, width=100)
    tree.column("total_payment", anchor=tk.W, width=100)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("order_id", text="Order ID", anchor=tk.W)
    tree.heading("order_date", text="Order Date", anchor=tk.W)
    tree.heading("menu_cat", text="Menu Category", anchor=tk.W)
    tree.heading("menu_item", text="Menu Item", anchor=tk.W)
    tree.heading("total_item", text="Total Item", anchor=tk.W)
    tree.heading("total_payment", text="Total Payment", anchor=tk.W)
    tree.grid(row=0, column=0)

    # Fetch data from the custorder table
    orders = view_orders(user)
    for order in orders:
        tree.insert("", "end", values=tuple(order))

    tree.pack()

    # Create a text widget to display the menu
    menu_text = tk.Text(update_form, width=40, height=10)
    menu_text.grid(row=1, column=0)

    # Read the menu from menu.txt
    menu = read_menu('menu.txt')

    # Format the menu and insert it into the text widget
    menu_str = ""
    for category, items in menu.items():
        menu_str += f"{category}:\n"
        for item, price in items:
            menu_str += f"  {item} - RM {price}\n"
    menu_text.insert('1.0', menu_str)

    # Create a form to enter the order details
    form_frame = ttk.Frame(update_form)
    form_frame.grid(row=1, column=1, columnspan=2)

    order_id_label = ttk.Label(form_frame, text="Order ID:")
    order_id_label.grid(row=0, column=0)
    order_id_entry = ttk.Entry(form_frame)
    order_id_entry.grid(row=1, column=0)

    menu_cat_label = ttk.Label(form_frame, text="Menu Category:")
    menu_cat_label.grid(row=2, column=0)
    menu_cat_entry = ttk.Entry(form_frame)
    menu_cat_entry.grid(row=3, column=0)

    menu_item_label = ttk.Label(form_frame, text="Menu Item:")
    menu_item_label.grid(row=4, column=0)
    menu_item_entry = ttk.Entry(form_frame)
    menu_item_entry.grid(row=5, column=0)

    total_item_label = ttk.Label(form_frame, text="Total Item:")
    total_item_label.grid(row=6, column=0)
    total_item_entry = ttk.Entry(form_frame)
    total_item_entry.grid(row=7, column=0)

    # Create a submit button
    submit_button = ttk.Button(form_frame, text="Submit", command=lambda: update_order(order_id_entry.get(), menu_cat_entry.get(), menu_item_entry.get(), total_item_entry.get(),update_form))
    submit_button.grid(row=8, column=0, padx=5, pady=5)

def show_cancel_order(user):
    # Create a new window
    cancel_order_window = tk.Toplevel()
    cancel_order_window.title("Cancel Order")

    # Create a treeview widget
    tree = ttk.Treeview(cancel_order_window)
    tree["columns"]=("order_id", "order_date", "menu_cat", "menu_item", "total_item", "total_payment")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("order_id", anchor=tk.W, width=100)
    tree.column("order_date", anchor=tk.W, width=130)
    tree.column("menu_cat", anchor=tk.W, width=100)
    tree.column("menu_item", anchor=tk.W, width=100)
    tree.column("total_item", anchor=tk.W, width=100)
    tree.column("total_payment", anchor=tk.W, width=100)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("order_id", text="Order ID", anchor=tk.W)
    tree.heading("order_date", text="Order Date", anchor=tk.W)
    tree.heading("menu_cat", text="Menu Category", anchor=tk.W)
    tree.heading("menu_item", text="Menu Item", anchor=tk.W)
    tree.heading("total_item", text="Total Item", anchor=tk.W)
    tree.heading("total_payment", text="Total Payment", anchor=tk.W)    
    tree.grid(row=0, column=0, columnspan=2,rowspan=3, padx=5, pady=5) 

    # Fetch data from the custorder table
    orders = view_orders(user)
    for order in orders:
        tree.insert("", "end", values=tuple(order))

    # Create a form to enter the order ID
    order_id_label = ttk.Label(cancel_order_window, text="Order ID:")
    order_id_label.grid(row=0, column=2)  

    order_id_entry = ttk.Entry(cancel_order_window)
    order_id_entry.grid(row=1, column=2)  

    # Create a submit button
    submit_button = ttk.Button(cancel_order_window, text="Submit", command=lambda: cancel_order(order_id_entry.get(),cancel_order_window))
    submit_button.grid(row=2, column=2, padx=5, pady=5)  

def main_menu(user):
    # Create a new window
    main_menu_window = tk.Toplevel()
    main_menu_window.title("Main Menu")

    # Create a frame
    frame = ttk.Frame(main_menu_window, padding="10 20 10 20")
    frame.pack(fill='both', expand=True)

    # Create a label to display the user's name
    user_label = ttk.Label(frame, text=f"Welcome, {user['name']}!")
    user_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Create buttons for the options
    create_order_button = ttk.Button(frame, text="1. Create order", command=lambda: show_create_order(user))
    view_orders_button = ttk.Button(frame, text="2. View orders", command=lambda: show_view_orders(user))
    update_order_button = ttk.Button(frame, text="3. Update order", command=lambda: show_update_order(user))
    cancel_order_button = ttk.Button(frame, text="4. Cancel order", command=lambda: show_cancel_order(user))
    exit_button = ttk.Button(frame, text="5. Exit", command=main_menu_window.destroy)

    # Arrange widgets in grid
    create_order_button.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    view_orders_button.grid(row=2, column=0, sticky='w', padx=5, pady=5)
    update_order_button.grid(row=3, column=0, sticky='w', padx=5, pady=5)
    cancel_order_button.grid(row=4, column=0, sticky='w', padx=5, pady=5)
    exit_button.grid(row=5, column=0, sticky='w', padx=5, pady=5)

# Main function to run the system
def main():
    
    # Create the main window
    root = tk.Tk()
    root.title("Menu Options")
    root.configure(bg='white')

    # Create a style
    style = ttk.Style(root)
    style.configure('TButton', font=('Arial', 20), background='blue')

    # Create buttons for the options
    register_button = ttk.Button(root, text="Register", command=register)
    login_button = ttk.Button(root, text="Login", command=login)
    create_sales_button = ttk.Button(root, text="Print Sales", command=print_sales)
    exit_button = ttk.Button(root, text="Exit", command=root.destroy)

    # Pack the buttons onto the window
    register_button.pack(ipadx=10, ipady=10, padx=20, pady=20)
    login_button.pack(ipadx=10, ipady=10, padx=20, pady=20)
    create_sales_button.pack(ipadx=10, ipady=10, padx=20, pady=20)
    exit_button.pack(ipadx=10, ipady=10, padx=20, pady=20)

    # Start the main loop
    root.mainloop()

main()