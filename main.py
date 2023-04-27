import tkinter as tk
import tkinter.messagebox as messagebox
import mysql.connector

class OnlineBankingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Banking System")
        
        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="banking"
        )
        self.cursor = self.db.cursor()

        # Create a label for the user ID
        self.user_id_label = tk.Label(self.master, text="User ID:")
        self.user_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.user_id_entry = tk.Entry(self.master)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create a label for the user's balance
        self.balance_label = tk.Label(self.master, text="Balance: $0.00")
        self.balance_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for the deposit amount
        self.deposit_label = tk.Label(self.master, text="Deposit amount:")
        self.deposit_label.grid(row=2, column=0, padx=10, pady=10)
        self.deposit_entry = tk.Entry(self.master)
        self.deposit_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create a button to deposit funds
        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit_funds)
        self.deposit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for the withdrawal amount
        self.withdrawal_label = tk.Label(self.master, text="Withdrawal amount:")
        self.withdrawal_label.grid(row=4, column=0, padx=10, pady=10)
        self.withdrawal_entry = tk.Entry(self.master)
        self.withdrawal_entry.grid(row=4, column=1, padx=10, pady=10)

        # Create a button to withdraw funds
        self.withdrawal_button = tk.Button(self.master, text="Withdraw", command=self.withdraw_funds)
        self.withdrawal_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for the user's name
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.grid(row=6, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=6, column=1, padx=10, pady=10)

        # Create a label and entry for the user's PIN
        self.pin_label = tk.Label(self.master, text="PIN:")
        self.pin_label.grid(row=7, column=0, padx=10, pady=10)
        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.grid(row=7, column=1, padx=10, pady=10)

        # Create a button to create a new account
        self.create_button = tk.Button(self.master, text="Create Account", command=self.create_account)

              
            
