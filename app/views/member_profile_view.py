import tkinter as tk
from tkinter import messagebox
from src.controllers.member_profile_controller import MemberProfileController


class MemberProfileView:
    def __init__(self, root):
        self.root = root
        self.controller = MemberProfileController()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Member ID:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Name:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Email:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Membership Type:").grid(row=3, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Join Date:").grid(row=4, column=0, sticky=tk.E)

        self.member_id_entry = tk.Entry(self.frame)
        self.name_entry = tk.Entry(self.frame)
        self.email_entry = tk.Entry(self.frame)
        self.membership_type_entry = tk.Entry(self.frame)
        self.join_date_entry = tk.Entry(self.frame)

        self.member_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.membership_type_entry.grid(row=3, column=1, padx=10, pady=5)
        self.join_date_entry.grid(row=4, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Member", command=self.add_member)
        self.update_button = tk.Button(self.frame, text="Update Member", command=self.update_member)
        self.view_button = tk.Button(self.frame, text="View Member", command=self.view_member)
        self.delete_button = tk.Button(self.frame, text="Delete Member", command=self.delete_member)

        self.add_button.grid(row=5, column=0, pady=10)
        self.update_button.grid(row=5, column=1, pady=10)
        self.view_button.grid(row=6, column=0, pady=10)
        self.delete_button.grid(row=6, column=1, pady=10)

    def add_member(self):
        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        membership_type = self.membership_type_entry.get()
        join_date = self.join_date_entry.get()

        if not member_id or not name or not email or not membership_type or not join_date:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        self.controller.add_member(member_id, name, email, membership_type, join_date)
        self.clear_entries()

    def update_member(self):
        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        membership_type = self.membership_type_entry.get()
        join_date = self.join_date_entry.get()

        if not member_id:
            messagebox.showwarning("Input Error", "Member ID must be provided")
            return

        self.controller.update_member(member_id, name=name, email=email, membership_type=membership_type,
                                      join_date=join_date)
        self.clear_entries()

    def view_member(self):
        member_id = self.member_id_entry.get()
        if not member_id:
            messagebox.showwarning("Input Error", "Member ID must be provided")
            return

        member = self.controller.get_member_by_id(member_id)
        if member:
            messagebox.showinfo("Member Details",
                                f"Member ID: {member.member_id}\nName: {member.name}\nEmail: {member.email}\nMembership Type: {member.membership_type}\nJoin Date: {member.join_date}")
        else:
            messagebox.showwarning("Not Found", "Member not found")

    def delete_member(self):
        member_id = self.member_id_entry.get()
        if not member_id:
            messagebox.showwarning("Input Error", "Member ID must be provided")
            return

        self.controller.delete_member(member_id)
        self.clear_entries()

    def clear_entries(self):
        self.member_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.membership_type_entry.delete(0, tk.END)
        self.join_date_entry.delete(0, tk.END)

