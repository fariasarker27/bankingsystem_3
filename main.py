import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

connection = sqlite3.connect("OnlineBankingApp")
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS My_library (account_number INTEGER PRIMARY KEY, PIN INTEGER, name TEXT, balance_amt REAL)')
cursor.execute("INSERT OR IGNORE INTO My_library (account_number, PIN, name, balance_amt) VALUES (123456, 1234, 'Mary Lee', 2.00)")
cursor.execute("INSERT OR IGNORE INTO My_library (account_number, PIN, name, balance_amt) VALUES (567890, 5678, 'Tim Smith', 10000.00)")
cursor.execute("INSERT OR IGNORE INTO My_library (account_number, PIN, name, balance_amt) VALUES (234567, 2355, 'Jane Doe', 23.45)")



connection.commit()



class Account:
    def __init__(self, acc_num, pin, name, balance_amt):
        self.acc_num = acc_num
        self.pin = pin
        self.name = name
        self.balance = balance_amt

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
      # Retrieve account number and PIN from entries
        acc_num = self.acc_num_entry.get()
        pin = self.pin_entry.get()
    
        # Query database for account number
        cursor = connection.execute(f"SELECT * FROM My_library WHERE account_number={acc_num}")
        account = cursor.fetchone()
    
        # Check if account exists and PIN is correct
        if account is not None and int(pin) == account[1]:
            messagebox.showinfo("Welcome", f"Welcome {account[2]}!")
            self.balance_label.config(text=f"Balance: ${account[3]:.2f}")
        else:
            messagebox.showerror("Error", "Invalid account number or PIN.")
        
    def deposit_funds(self):
        # Get the deposit amount from the entry box
        deposit_amount = self.deposit_entry.get()

        # Check if the deposit amount is a valid number
        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid deposit amount.")
            return

        # Check if the deposit amount is positive
        if deposit_amount <= 0:
            messagebox.showerror("Error", "Deposit amount must be positive.")
            return
        acc_num = self.acc_num_entry.get()
        cursor = connection.execute(f"SELECT * FROM My_library WHERE account_number={acc_num}")
        
        # Update the balance in the database
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE My_library SET balance_amt = balance_amt + ? WHERE account_number = ?", (deposit_amount, acc_num))
            connection.commit()
            messagebox.showinfo("Sucess", "Deposit sucessful!")
        except sqlite3.Error as error:
            messagebox.showerror("Error", "Error connection to SQLite.", error)
        finally:
            if (connection):
                connection.close()
        # Update the balance label
        self.update_balance_label()

    
    def withdraw_funds(self):
        # Get the deposit amount from the entry box
        withdraw_amount = self.withdrawal_entry.get()

        # Check if the deposit amount is a valid number
        try:
            withdraw_amount = float(withdraw_amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount.")
            return

        # Check if the deposit amount is positive
        if withdraw_amount <= 0:
            messagebox.showerror("Error", "Withdrawal amount must be positive.")
            return
        acc_num = self.acc_num_entry.get()
        cursor = connection.execute(f"SELECT * FROM My_library WHERE account_number={acc_num}")
        
        # Update the balance in the database
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE My_library SET balance_amt = balance_amt - ? WHERE account_number = ?", (withdraw_amount, acc_num))
            connection.commit()
            messagebox.showinfo("Sucess", "Withdrawal sucessful!")
        except sqlite3.Error as error:
            messagebox.showerror("Error", "Error connection to SQLite.", error)
        finally:
            if (connection):
                connection.close()
        # Update the balance label
        self.update_balance_label()
  
  
    def create_account(self):
        connection = sqlite3.connect("OnlineBankingApp")
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
               "VALUES (pin, acc_num, name)")
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
              return False
          self.current_account = account
          self.balance_label.config(text=f"Balance: ${self.current_account.balance:.2f}")
          self.deposit_entry.delete(0, tk.END)
          self.withdrawal_entry.delete(0, tk.END)
          self.create_account_entry.delete(0, tk.END)
          messagebox.showinfo("Success", f"Welcome, {self.current_account.name}!")
          return True
  
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
          connection.execute("DELETE from My_library WHERE account_number = ?;")
          connection.execute("DELETE from My_library WHERE PIN = ? ;")
          connection.execute("DELETE from My_library WHERE name = ?")
          connection.execute("DELETE from My_library WHERE balance_amt = ?")
          connection.commit()
          
  
          messagebox.showinfo("Success", "Account closed successfully.")
          return True
        else:
            return False

    def update_balance_label(self):
        # Get the current balance from the database
        cursor.execute("SELECT balance_amt FROM My_library WHERE account_number = ?", (self.acc_num,))
        balance = cursor.fetchone()[0]

        # Update the balance label
        self.balance_label.config(text="Balance: ${:.2f}".format(balance))
  

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineBankingApp(root)
    root.mainloop()




              
            
