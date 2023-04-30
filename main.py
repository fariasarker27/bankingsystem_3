import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class Account:
    def __init__(self, acc_num, pin, name):
        self.acc_num = acc_num
        self.pin = pin
        self.name = name
        self.balance = 0.0

class OnlineBankingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Banking System")

        self.accounts = {"123456": Account("123456", "1234", "John Doe"), "789012": Account("789012", "5678", "Jane Smith")}  # dictionary to store account information

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
        self.withdrawal_button = tk.Button(self.master, text="Withdraw", command=self)
        self.withdrawal_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for account creation
        self.create_account_label = tk.Label(self.master, text="Create account:")
        self.create_account_label.grid(row=8, column=0, padx=10, pady=10)
        self.create_account_entry = tk.Entry(self.master)
        self.create_account_entry.grid(row=8, column=1, padx=10, pady=10)


    def validate_login(self):
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
    
        # Login successful
        self.current_account = account
        self.balance_label.config(text=f"Balance: ${self.current_account.balance:.2f}")
        self.deposit_entry.delete(0, tk.END)
        self.withdrawal_entry.delete(0, tk.END)
        self.create_account_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Welcome, {self.current_account.name}!")
        return True
    


    def deposit_funds(self):
        # Get the deposit amount from the entry field
        deposit_amount = float(self.deposit_entry.get())
    
        # Check if the deposit amount is valid (i.e., positive)
        if deposit_amount <= 0:
            messagebox.showerror("Error", "Deposit amount must be greater than zero.")
            return
    
        # Add the deposit amount to the account balance
        self.accounts[self.current_user].balance += deposit_amount
    
        # Update the balance label
        self.update_balance_label()
    
        # Show a success message
        messagebox.showinfo("Success", f"Deposit of ${deposit_amount:.2f} successful.")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineBankingApp(root)
    root.mainloop()




              
            
