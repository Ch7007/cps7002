import tkinter as tk
from tkinter import messagebox
from src.controllers.appointment_controller import AppointmentController

class AppointmentView:
    def __init__(self, root):
        self.root = root
        self.controller = AppointmentController()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Appointment ID:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Member ID:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Trainer ID:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Appointment Type:").grid(row=3, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Date Time:").grid(row=4, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Status:").grid(row=5, column=0, sticky=tk.E)

        self.appointment_id_entry = tk.Entry(self.frame)
        self.member_id_entry = tk.Entry(self.frame)
        self.trainer_id_entry = tk.Entry(self.frame)
        self.appointment_type_entry = tk.Entry(self.frame)
        self.date_time_entry = tk.Entry(self.frame)
        self.status_entry = tk.Entry(self.frame)

        self.appointment_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.member_id_entry.grid(row=1, column=1, padx=10, pady=5)
        self.trainer_id_entry.grid(row=2, column=1, padx=10, pady=5)
        self.appointment_type_entry.grid(row=3, column=1, padx=10, pady=5)
        self.date_time_entry.grid(row=4, column=1, padx=10, pady=5)
        self.status_entry.grid(row=5, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Appointment", command=self.add_appointment)
        self.update_button = tk.Button(self.frame, text="Update Appointment", command=self.update_appointment)
        self.view_button = tk.Button(self.frame, text="View Appointment", command=self.view_appointment)
        self.delete_button = tk.Button(self.frame, text="Delete Appointment", command=self.delete_appointment)

        self.add_button.grid(row=6, column=0, pady=10)
        self.update_button.grid(row=6, column=1, pady=10)
        self.view_button.grid(row=7, column=0, pady=10)
        self.delete_button.grid(row=7, column=1, pady=10)

    def add_appointment(self):
        appointment_id = self.appointment_id_entry.get()
        member_id = self.member_id_entry.get()
        trainer_id = self.trainer_id_entry.get()
        appointment_type = self.appointment_type_entry.get()
        date_time = self.date_time_entry.get()
        status = self.status_entry.get()

        if not appointment_id or not member_id or not trainer_id or not appointment_type or not date_time or not status:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        self.controller.add_appointment(appointment_id, member_id, trainer_id, appointment_type, date_time, status)
        self.clear_entries()

    def update_appointment(self):
        appointment_id = self.appointment_id_entry.get()
        member_id = self.member_id_entry.get()
        trainer_id = self.trainer_id_entry.get()
        appointment_type = self.appointment_type_entry.get()
        date_time = self.date_time_entry.get()
        status = self.status_entry.get()

        if not appointment_id:
            messagebox.showwarning("Input Error", "Appointment ID must be provided")
            return

        self.controller.update_appointment(appointment_id, member_id=member_id, trainer_id=trainer_id, appointment_type=appointment_type, date_time=date_time, status=status)
        self.clear_entries()

    def view_appointment(self):
        appointment_id = self.appointment_id_entry.get()
        if not appointment_id:
            messagebox.showwarning("Input Error", "Appointment ID must be provided")
            return

        appointment = self.controller.get_appointment_by_id(appointment_id)
        if appointment:
            messagebox.showinfo("Appointment Details", f"Appointment ID: {appointment.appointment_id}\nMember ID: {appointment.member_id}\nTrainer ID: {appointment.trainer_id}\nAppointment Type: {appointment.appointment_type}\nDate Time: {appointment.date_time}\nStatus: {appointment.status}")
        else:
            messagebox.showwarning("Not Found", "Appointment not found")

    def delete_appointment(self):
        appointment_id = self.appointment_id_entry.get()
        if not appointment_id:
            messagebox.showwarning("Input Error", "Appointment ID must be provided")
            return

        self.controller.remove_appointment(appointment_id)
        self.clear_entries()

    def clear_entries(self):
        self.appointment_id_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.trainer_id_entry.delete(0, tk.END)
        self.appointment_type_entry.delete(0, tk.END)
        self.date_time_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)

