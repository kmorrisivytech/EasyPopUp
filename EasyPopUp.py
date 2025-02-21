import tkinter as tk
from tkinter import messagebox

class EasyPopUpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EasyPopUp")
        self.total_sales = 0  # Track daily total sales
        self.transactions = []  # Store transactions
        self.create_main_menu()

    def create_main_menu(self):
        """Creates the main menu window."""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="EasyPopUp", font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Button(self.root, text="New Order", command=self.open_order_window).pack(pady=5)
        tk.Button(self.root, text="Checkout", command=self.open_checkout_window).pack(pady=5)
        tk.Button(self.root, text="Reports", command=self.open_reports_window).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)
    
    def open_order_window(self):
        """Opens the order entry window."""
        self.order_window = tk.Toplevel(self.root)
        self.order_window.title("New Order")
        tk.Label(self.order_window, text="Order Entry", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.order_window, text="Select Item:").pack()
        burger_button = tk.Button(self.order_window, text="Burger ($15)", command=lambda: self.add_item("Burger", 15))
        burger_button.pack(pady=5)
        
        chicken_button = tk.Button(self.order_window, text="Chicken Sandwich ($17)", command=lambda: self.add_item("Chicken Sandwich", 17))
        chicken_button.pack(pady=5)
        
        tk.Button(self.order_window, text="Back", command=self.order_window.destroy).pack(pady=5)
    
    def add_item(self, item, price):
        self.transactions.append((item, price))
        self.total_sales += price
        messagebox.showinfo("Item Added", f"Added {item} - ${price}")
    
    def open_checkout_window(self):
        """Opens the checkout window."""
        self.checkout_window = tk.Toplevel(self.root)
        self.checkout_window.title("Checkout")
        tk.Label(self.checkout_window, text="Checkout Summary", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.checkout_window, text=f"Total Sales: ${self.total_sales}", font=("Arial", 12)).pack(pady=5)
        
        tk.Button(self.checkout_window, text="Pay with Cash", command=self.pay_with_cash).pack(pady=5)
        tk.Button(self.checkout_window, text="Back", command=self.checkout_window.destroy).pack(pady=5)
    
    def pay_with_cash(self):
        """Handles cash payment processing."""
        messagebox.showinfo("Payment", "Payment received in cash. Order complete!")
        self.transactions.clear()
        self.total_sales = 0  # Reset total sales after payment
        if hasattr(self.order_window, 'destroy'):
            self.order_window.destroy()
        if hasattr(self.checkout_window, 'destroy'):
            self.checkout_window.destroy()
    
    def open_reports_window(self):
        """Opens the reports window."""
        reports_window = tk.Toplevel(self.root)
        reports_window.title("Reports")
        tk.Label(reports_window, text="Daily Reports", font=("Arial", 14)).pack(pady=10)
        tk.Label(reports_window, text=f"Total Sales for the Day: ${self.total_sales}", font=("Arial", 12)).pack(pady=5)
        
        transactions_text = "\n".join([f"{item}: ${price}" for item, price in self.transactions])
        tk.Label(reports_window, text=f"Transactions:\n{transactions_text}", font=("Arial", 12)).pack(pady=5)
        
        tk.Button(reports_window, text="Back", command=reports_window.destroy).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = EasyPopUpApp(root)
    root.mainloop()
