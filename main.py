import tkinter as tk

class OnlineBankingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Banking System")

        # Create a label for the balance
        self.balance_label = tk.Label(self.master, text="Balance: $0.00")
        self.balance_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for the deposit amount
        self.deposit_label = tk.Label(self.master, text="Deposit amount:")
        self.deposit_label.grid(row=1, column=0, padx=10, pady=10)
        self.deposit_entry = tk.Entry(self.master)
        self.deposit_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create a button to deposit funds
        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit_funds)
        self.deposit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create a label and entry for the withdrawal amount
        self.withdrawal_label = tk.Label(self.master, text="Withdrawal amount:")
        self.withdrawal_label.grid(row=3, column=0, padx=10, pady=10)
        self.withdrawal_entry = tk.Entry(self.master)
        self.withdrawal_entry.grid(row=3, column=1, padx=10, pady=10)

        # Create a button to withdraw funds
        self.withdrawal_button = tk.Button(self.master, text="Withdraw", command=self.withdraw_funds)
        self.withdrawal_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def deposit_funds(self):
        amount = float(self.deposit_entry.get())
        self.balance += amount
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
        self.deposit_entry.delete(0, tk.END)

    def withdraw_funds(self):
        amount = float(self.withdrawal_entry.get())
        if amount <= self.balance:
            self.balance -= amount
            self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
        else:
            tk.messagebox.showerror("Error", "Insufficient funds")
        self.withdrawal_entry.delete(0, tk.END)
      # Create a label and entry for account number to close account
        self.close_account_label = tk.Label(self.master, text="Enter Account Number to Close:")
        self.close_account_label.grid(row=5, column=0, padx=10, pady=10)
        self.close_account_entry = tk.Entry(self.master)
        self.close_account_entry.grid(row=5, column=1, padx=10, pady=10)
      # Create a button to close an account
        self.close_account_button = tk.Button(self.master, text="Close Account", command=self.close_account)
        self.close_account_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineBankingApp(root)
    root.mainloop()



              
            
