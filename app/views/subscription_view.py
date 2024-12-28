import tkinter as tk
from tkinter import messagebox
from src.controllers.subscription_controller import SubscriptionController

class SubscriptionView:
    def __init__(self, root):
        self.root = root
        self.controller = SubscriptionController()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Subscription ID:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Member ID:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Plan ID:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Start Date:").grid(row=3, column=0, sticky=tk.E)
        tk.Label(self.frame, text="End Date:").grid(row=4, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Status:").grid(row=5, column=0, sticky=tk.E)

        self.subscription_id_entry = tk.Entry(self.frame)
        self.member_id_entry = tk.Entry(self.frame)
        self.plan_id_entry = tk.Entry(self.frame)
        self.start_date_entry = tk.Entry(self.frame)
        self.end_date_entry = tk.Entry(self.frame)
        self.status_entry = tk.Entry(self.frame)

        self.subscription_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.member_id_entry.grid(row=1, column=1, padx=10, pady=5)
        self.plan_id_entry.grid(row=2, column=1, padx=10, pady=5)
        self.start_date_entry.grid(row=3, column=1, padx=10, pady=5)
        self.end_date_entry.grid(row=4, column=1, padx=10, pady=5)
        self.status_entry.grid(row=5, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Subscription", command=self.add_subscription)
        self.update_button = tk.Button(self.frame, text="Update Subscription", command=self.update_subscription)
        self.view_button = tk.Button(self.frame, text="View Subscription", command=self.view_subscription)
        self.delete_button = tk.Button(self.frame, text="Delete Subscription", command=self.delete_subscription)

        self.add_button.grid(row=6, column=0, pady=10)
        self.update_button.grid(row=6, column=1, pady=10)
        self.view_button.grid(row=7, column=0, pady=10)
        self.delete_button.grid(row=7, column=1, pady=10)

    def add_subscription(self):
        subscription_id = self.subscription_id_entry.get()
        member_id = self.member_id_entry.get()
        plan_id = self.plan_id_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        status = self.status_entry.get()

        if not subscription_id or not member_id or not plan_id or not start_date or not end_date or not status:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        self.controller.add_subscription(subscription_id, member_id, plan_id, start_date, end_date, status)
        messagebox.showinfo("Success", "Subscription added successfully")
        self.clear_entries()

    def update_subscription(self):
        subscription_id = self.subscription_id_entry.get()
        member_id = self.member_id_entry.get()
        plan_id = self.plan_id_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        status = self.status_entry.get()

        if not subscription_id:
            messagebox.showwarning("Input Error", "Subscription ID must be provided")
            return

        self.controller.update_subscription(subscription_id, member_id=member_id, plan_id=plan_id, start_date=start_date, end_date=end_date, status=status)
        messagebox.showinfo("Success", "Subscription updated successfully")
        self.clear_entries()

    def view_subscription(self):
        subscription_id = self.subscription_id_entry.get()
        if not subscription_id:
            messagebox.showwarning("Input Error", "Subscription ID must be provided")
            return

        subscription = self.controller.get_subscription_by_id(subscription_id)
        if subscription:
            messagebox.showinfo("Subscription Details", f"Subscription ID: {subscription.subscription_id}\nMember ID: {subscription.member_id}\nPlan ID: {subscription.plan_id}\nStart Date: {subscription.start_date}\nEnd Date: {subscription.end_date}\nStatus: {subscription.status}")
        else:
            messagebox.showwarning("Not Found", "Subscription not found")

    def delete_subscription(self):
        subscription_id = self.subscription_id_entry.get()
        if not subscription_id:
            messagebox.showwarning("Input Error", "Subscription ID must be provided")
            return

        self.controller.delete_subscription(subscription_id)
        messagebox.showinfo("Success", "Subscription deleted successfully")
        self.clear_entries()

    def clear_entries(self):
        self.subscription_id_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.plan_id_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
