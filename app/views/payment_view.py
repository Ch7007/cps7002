import tkinter as tk
from tkinter import messagebox
from src.controllers.payment_controller import PaymentController

class PaymentView:
    def __init__(self, root):
        self.root = root
        self.controller = PaymentController()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Payment ID:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Member ID:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Amount:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Date:").grid(row=3, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Method:").grid(row=4, column=0, sticky=tk.E)

        self.payment_id_entry = tk.Entry(self.frame)
        self.member_id_entry = tk.Entry(self.frame)
        self.amount_entry = tk.Entry(self.frame)
        self.date_entry = tk.Entry(self.frame)
        self.method_entry = tk.Entry(self.frame)

        self.payment_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.member_id_entry.grid(row=1, column=1, padx=10, pady=5)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)
        self.date_entry.grid(row=3, column=1, padx=10, pady=5)
        self.method_entry.grid(row=4, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Payment", command=self.add_payment)
        self.update_button = tk.Button(self.frame, text="Update Payment", command=self.update_payment)
        self.view_button = tk.Button(self.frame, text="View Payment", command=self.view_payment)
        self.delete_button = tk.Button(self.frame, text="Delete Payment", command=self.delete_payment)

        self.add_button.grid(row=5, column=0, pady=10)
        self.update_button.grid(row=5, column=1, pady=10)
        self.view_button.grid(row=6, column=0, pady=10)
        self.delete_button.grid(row=6, column=1, pady=10)

    def add_payment(self):
        payment_id = self.payment_id_entry.get()
        member_id = self.member_id_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        method = self.method_entry.get()

        if not payment_id or not member_id or not amount or not date or not method:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        self.controller.add_payment(payment_id, member_id, amount, date, method)
        messagebox.showinfo("Success", "Payment added successfully")
        self.clear_entries()

    def update_payment(self):
        payment_id = self.payment_id_entry.get()
        member_id = self.member_id_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        method = self.method_entry.get()

        if not payment_id:
            messagebox.showwarning("Input Error", "Payment ID must be provided")
            return

        self.controller.update_payment(payment_id, member_id=member_id, amount=amount, date=date, method=method)
        messagebox.showinfo("Success", "Payment updated successfully")
        self.clear_entries()

    def view_payment(self):
        payment_id = self.payment_id_entry.get()
        if not payment_id:
            messagebox.showwarning("Input Error", "Payment ID must be provided")
            return

        payment = self.controller.get_payment_by_id(payment_id)
        if payment:
            messagebox.showinfo("Payment Details", f"Payment ID: {payment.payment_id}\nMember ID: {payment.member_id}\nAmount: {payment.amount}\nDate: {payment.date}\nMethod: {payment.method}")
        else:
            messagebox.showwarning("Not Found", "Payment not found")

    def delete_payment(self):
        payment_id = self.payment_id_entry.get()
        if not payment_id:
            messagebox.showwarning("Input Error", "Payment ID must be provided")
            return

        self.controller.remove_payment(payment_id)
        messagebox.showinfo("Success", "Payment deleted successfully")
        self.clear_entries()

    def clear_entries(self):
        self.payment_id_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.method_entry.delete(0, tk.END)
