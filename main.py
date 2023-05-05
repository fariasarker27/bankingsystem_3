import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

connection = sqlite3.connect("OnlineBankingApp")
connection.execute("CREATE TABLE IF NOT EXISTS My_library (account_number INTEGER PRIMARY KEY, PIN INTEGER, name STRING);")
connection.execute("INSERT INTO My_library (PIN, account_number, name) "
             "VALUES (1234, 123456,'Mary Lee'), (5678, 567890, 'Tim Smith'), (2355, 234567, 'Jane Doe')")

class Account:
    def __init__(self, acc_num, pin, name):
        self.acc_num = acc_num
        self.pin = pin
        self.name = name
        self.balance = 0.0

class OnlineBankingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ABC Online Banking System")

        # Create labels and entries for login information
        self.acc_num_label = tk.Label(self.master, text="Account number:")
        self.acc_num_label.grid(row=0, column=0, padx=10, pady=10)
        self.acc_num_entry = tk.Entry(self.master)
        self.acc_num_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pin_label = tk.Label(self.master, text="PIN:")
        self.pin_label.grid(row=1, column=0, padx=10, pady=10)
        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create a button to log in
        self.login_button = tk.Button(self.master, text="Log in", command=self.validate_login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
 

        # Create a label for the balance
        self.balance_label = tk.Label(self.master, text="Balance: $0.00")
        self.balance_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for the deposit amount
        self.deposit_label = tk.Label(self.master, text="Deposit amount:")
        self.deposit_label.grid(row=4, column=0, padx=10, pady=10)
        self.deposit_entry = tk.Entry(self.master)
        self.deposit_entry.grid(row=4, column=1, padx=10, pady=10)

        # Create a button to deposit funds
        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit_funds)
        self.deposit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for the withdrawal amount
        self.withdrawal_label = tk.Label(self.master, text="Withdrawal amount:")
        self.withdrawal_label.grid(row=6, column=0, padx=10, pady=10)
        self.withdrawal_entry = tk.Entry(self.master)
        self.withdrawal_entry.grid(row=6, column=1, padx=10, pady=10)

        # Create a button to withdraw funds
        self.withdrawal_button = tk.Button(self.master, text="Withdraw", command=self.withdraw_funds)
        self.withdrawal_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for account creation (PIN, account number)
        self.create_account_pin_label = tk.Label(self.master, text="Create account PIN:")
        self.create_account_pin_label.grid(row=0, column=2, padx=10, pady=10)
        self.create_account_pin_entry = tk.Entry(self.master)
        self.create_account_pin_entry.grid(row=0, column=3, padx=10, pady=10)
        self.create_account_num_label= tk.Label(self.master, text="Create account number:")
        self.create_account_num_label.grid(row=1, column=2, padx=10, pady=10)
        self.create_account_num_entry = tk.Entry(self.master)
        self.create_account_num_entry.grid(row=1, column=3, padx=10, pady=10)
      # Create label and entry for name of account holder
        self.create_account_name_label = tk.Label(self.master, text="Enter your name:")
        self.create_account_name_label.grid(row=2, column=2, padx=10, pady=10)
        self.create_account_name_entry = tk.Entry(self.master)
        self.create_account_name_entry.grid(row=2, column=3, padx=10, pady=10)
      
        # Create a button to create account
        self.create_account_button = tk.Button(self.master, text="Create account", command=self.create_account)
        self.create_account_button.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

      # Create a button to modify account
        self.create_modify_account_button = tk.Button(self.master, text="Modify account", command=self.modify_account)
        self.create_modify_account_button.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

      #Create a button to close account
        self.create_close_account_button = tk.Button(self.master, text="Close account", command=self.close_account)
        self.create_close_account_button.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
        


    def validate_login(self):
        acc_num = self.acc_num_entry.get()
        pin = self.pin_entry.get()
        connection = sqlite3.connect("OnlineBankingApp")
        connection.execute("CREATE TABLE IF NOT EXISTS My_library (account_number INTEGER PRIMARY KEY, PIN INTEGER, name STRING);")
        connection.execute("INSERT INTO My_library (PIN, account_number, name) "
             "VALUES (1234, 123456,'Mary Lee'), (5678, 567890, 'Tim Smith'), (2355, 234567, 'Jane Doe')")
    
        if acc_num == "" or pin == "":
            # Empty fields
            messagebox.showerror("Error", "Please enter both account number and PIN.")
            return False
    
        if acc_num not in self.accounts:
            # Account not found
            messagebox.showerror("Error", "Account not found.")
            return False
    
        account = self.accounts[acc_num]
        if account.pin != pin:
            # Incorrect PIN
            messagebox.showerror("Error", "Incorrect PIN.")
            return False
    
        # Login successful
        self.current_account = account
        self.balance_label.config(text=f"Balance: ${self.current_account.balance:.2f}")
        self.deposit_entry.delete(0, tk.END)
        self.withdrawal_entry.delete(0, tk.END)
        self.create_account_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Welcome, {self.current_account.name}!")
        return True
    


    def deposit_funds(self):
      connection = sqlite3.connect("OnlineBankingApp")
      connection.execute("CREATE TABLE IF NOT EXISTS My_library (account_number INTEGER PRIMARY KEY, PIN INTEGER, name STRING);")
      connection.execute("INSERT INTO My_library (PIN, account_number, name) "
             "VALUES (1234, 123456,'Mary Lee'), (5678, 567890, 'Tim Smith'), (2355, 234567, 'Jane Doe')")
       # Get the deposit amount from the entry field
      deposit_amount = float(self.deposit_entry.get())
    # Check if the deposit amount is valid (i.e., positive)
      if deposit_amount <= 0:
          messagebox.showerror("Error", "Deposit amount must be greater than zero.")
          return
    
    # Add the deposit amount to the account balance
      self.current_account.balance += deposit_amount
    
    # Update the balance label
      self.balance_label.config(text=f"Balance: ${self.current_account.balance:.2f}")
    
    # Show a success message
      messagebox.showinfo("Success", f"Deposit of ${deposit_amount:.2f} successful.")


    def withdraw_funds(self):
    # Get the withdrawal amount from the entry field
     withdrawal_amount = float(self.withdrawal_entry.get())

    # Check if the withdrawal amount is valid (i.e., positive and less than or equal to the account balance)
     if withdrawal_amount <= 0:
          messagebox.showerror("Error", "Withdrawal amount must be greater than zero.")
          return

     if withdrawal_amount > self.current_account.balance:
          messagebox.showerror("Error", "Insufficient funds.")
          return

    # Subtract the withdrawal amount from the account balance
     self.current_account.balance -= withdrawal_amount

    # Update the balance label
     self.balance_label.config(text=f"Balance: ${self.current_account.balance:.2f}")

    # Show a success message
     messagebox.showinfo("Success", f"Withdrawal of ${withdrawal_amount:.2f} successful.")


    def create_account(self):
      connection = sqlite3.connect("OnlineBankingApp")
      connection.execute("CREATE TABLE IF NOT EXISTS My_library (account_number INTEGER PRIMARY KEY, PIN INTEGER, name STRING);")
      connection.execute("INSERT INTO My_library (PIN, account_number, name) "
             "VALUES (1234, 123456,'Mary Lee'), (5678, 567890, 'Tim Smith'), (2355, 234567, 'Jane Doe')")
    # Get the PIN and account number from the entry fields
      pin = self.create_account_pin_entry.get()
      acc_num = self.create_account_num_entry.get()
      name = self.create_account_name_entry.get()

    # Check if either field is empty
      if not pin or not acc_num:
          messagebox.showerror("Error", "Please enter both a PIN and an account number.")
          return

    # Check if the account number is already taken
      if acc_num in self.accounts:
          messagebox.showerror("Error", "Account number already taken.")
          return

    # Create a new account and add it to the dictionary
      connection.execute('INSERT INTO My_library (account_number, PIN, name)'
             "VALUES (0987, '098765','John Thomas')")
      connection.commit()
      connection.close()

    # Clear the entry fields and show a success message
      self.create_account_pin_entry.delete(0, tk.END)
      self.create_account_num_entry.delete(0, tk.END)
      messagebox.showinfo("Success", f"Account {acc_num} successfully created for {name}.")

    def modify_account(self):
        acc_num = simpledialog.askstring("Modify Account", "Enter account number:")
        if acc_num == "":
            # Empty account number
            messagebox.showerror("Error", "Please enter an account number.")
            return
        
        if acc_num not in self.accounts:
            # Account not found
            messagebox.showerror("Error", "Account not found.")
            return
        
        account = self.accounts[acc_num]
        new_pin = simpledialog.askstring("Modify Account", "Enter new PIN:")
        if new_pin == "":
            # Empty PIN
            messagebox.showerror("Error", "Please enter a new PIN.")
            return
        

      

        messagebox.showinfo("Account Modified", "Account modified successfully.")

    def close_account(self):
      acc_num = self.acc_num_entry.get()
      pin = self.pin_entry.get()

      if acc_num == "" or pin == "":
        # Empty fields
          messagebox.showerror("Error", "Please enter both account number and PIN.")
          return False

      if acc_num not in self.accounts:
        # Account not found
          messagebox.showerror("Error", "Account not found.")
          return False

      account = self.accounts[acc_num]
      if account.pin != pin:
        # Incorrect PIN
          messagebox.showerror("Error", "Incorrect PIN.")
          return False

    # Confirm account closure
      confirm = messagebox.askyesno("Confirmation", "Are you sure you want to close your account?")

      if confirm:
        connection.execute("DELETE from My_library WHERE account_number = x;")
        connection.execute("DELETE from My_library WHERE PIN = 1234 ;")
        connection.execute("DELETE from My_library WHERE name = 'Jane Doe'")
        connection.commit()
        connection.close()

        messagebox.showinfo("Success", "Account closed successfully.")
        return True
      else:
          return False


if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineBankingApp(root)
    root.mainloop()




              
            
