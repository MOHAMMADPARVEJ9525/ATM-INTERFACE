import tkinter as tk
from tkinter import messagebox

class ATMInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("1520x820")
        self.root.configure(bg="#f2f2f2")

        self.balance = 1000.0
        self.pin = "1111"

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Welcome to ATM", font=("Helvetica", 20, "bold"), bg="#f2f2f2")
        title.pack(pady=50)

        label = tk.Label(self.root, text="Enter your PIN:", font=("Helvetica", 14), bg="#f2f2f2")
        label.pack(pady=10)

        self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 14), width=20)
        self.pin_entry.pack(pady=10)

        login_button = tk.Button(self.root, text="Login", font=("Helvetica", 14), width=20, height=2, command=self.check_pin, bg="#4CAF50", fg="white")
        login_button.pack(pady=20)

    def check_pin(self):
        if self.pin_entry.get() == self.pin:
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN. Try again.")

    def show_main_menu(self):
        self.clear_screen()
        title = tk.Label(self.root, text="ATM Main Menu", font=("Helvetica", 20, "bold"), bg="#f2f2f2")
        title.pack(pady=30)

        tk.Button(self.root, text="Check Balance", font=("Helvetica", 14), width=40, height=2, command=self.show_balance, bg="#2196F3", fg="white").pack(pady=10)
        tk.Button(self.root, text="Deposit", font=("Helvetica", 14), width=40, height=2, command=self.deposit_amount, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Withdraw", font=("Helvetica", 14), width=40, height=2, command=self.withdraw_amount, bg="#FF5722", fg="white").pack(pady=10)
        tk.Button(self.root, text="Logout", font=("Helvetica", 14), width=40, height=2, command=self.create_login_screen, bg="#607D8B", fg="white").pack(pady=10)

    def show_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is ${self.balance:.2f}")

    def deposit_amount(self):
        self.clear_screen()
        tk.Label(self.root, text="Deposit Amount", font=("Helvetica", 20, "bold"), bg="#f2f2f2").pack(pady=30)

        tk.Label(self.root, text="Enter amount to deposit:", font=("Helvetica", 14), bg="#f2f2f2").pack(pady=10)
        self.deposit_entry = tk.Entry(self.root, font=("Helvetica", 14), width=20)
        self.deposit_entry.pack(pady=10)

        tk.Button(self.root, text="Deposit", font=("Helvetica", 14), width=20, height=2, command=self.process_deposit, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Back", font=("Helvetica", 14), width=20, height=2, command=self.show_main_menu, bg="#607D8B", fg="white").pack(pady=5)

    def process_deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            messagebox.showinfo("Success", f"Deposit successful!\nNew Balance: ${self.balance:.2f}")
            self.show_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def withdraw_amount(self):
        self.clear_screen()
        tk.Label(self.root, text="Withdraw Amount", font=("Helvetica", 20, "bold"), bg="#f2f2f2").pack(pady=30)

        tk.Label(self.root, text="Enter amount to withdraw:", font=("Helvetica", 14), bg="#f2f2f2").pack(pady=10)
        self.withdraw_entry = tk.Entry(self.root, font=("Helvetica", 14), width=20)
        self.withdraw_entry.pack(pady=10)

        tk.Button(self.root, text="Withdraw", font=("Helvetica", 14), width=20, height=2, command=self.process_withdraw, bg="#FF5722", fg="white").pack(pady=10)
        tk.Button(self.root, text="Back", font=("Helvetica", 14), width=20, height=2, command=self.show_main_menu, bg="#607D8B", fg="white").pack(pady=5)

    def process_withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount <= 0:
                raise ValueError
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"Withdrawal successful!\nNew Balance: ${self.balance:.2f}")
                self.show_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the ATM GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMInterface(root)
    root.mainloop()
