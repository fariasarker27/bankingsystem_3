import tkinter as tk
import tkinter.messagebox as messagebox
import mysql.connector

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Banking System - Login")
        
        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="banking"
        )
        self.cursor = self.db.cursor()

        # Create a label for the username
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create a label for the password
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create a button to log in
        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        # Get the username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are valid
        self.cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = self.cursor.fetchone()
        if user is None:
            messagebox.showerror("Error", "Invalid username or password")
        else:
            # Open the main banking window
            self.master.destroy()
            BankingWindow(user)

class BankingWindow:
    def __init__(self, user):
        self.user = user
        self.master = tk.Tk()
        self.master.title("Online Banking System - Welcome " + user[1])
        
        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="banking"
        )
        self.cursor = self.db.cursor()

        # Create a label for the user ID
        self.user_id_label = tk.Label(self.master, text="User ID: " + str(self.user[0]))
        self.user_id_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a label for the user's balance
        self.balance_label = tk.Label(self.master, text="Balance: $" + str(self.user[3]))
        self.balance_label.grid(row=1, column=0, padx=10, pady=10)

        # Create a label and entry for the deposit amount
        self.deposit_label = tk.Label(self.master, text="Deposit amount:")
        self.deposit_label.grid(row=2, column=0, padx=10, pady=10)
        self.deposit_entry = tk.Entry(self.master)
        self.deposit_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create a button to deposit funds
        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit_funds)
        self.deposit_button.grid(row=3, column=0, columnspan=2,)




              
            
