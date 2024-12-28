import tkinter as tk
from tkinter import messagebox
from src.controllers.attendance_controller import AttendanceController

class AttendanceView:
    def __init__(self, root):
        self.root = root
        self.controller = AttendanceController()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Record ID:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Member ID:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Date Time:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Activity Type:").grid(row=3, column=0, sticky=tk.E)

        self.record_id_entry = tk.Entry(self.frame)
        self.member_id_entry = tk.Entry(self.frame)
        self.date_time_entry = tk.Entry(self.frame)
        self.activity_type_entry = tk.Entry(self.frame)

        self.record_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.member_id_entry.grid(row=1, column=1, padx=10, pady=5)
        self.date_time_entry.grid(row=2, column=1, padx=10, pady=5)
        self.activity_type_entry.grid(row=3, column=1, padx=10, pady=5)

        self.log_button = tk.Button(self.frame, text="Log Attendance", command=self.log_attendance)
        self.update_button = tk.Button(self.frame, text="Update Attendance", command=self.update_attendance)
        self.view_button = tk.Button(self.frame, text="View Attendance", command=self.view_attendance)
        self.delete_button = tk.Button(self.frame, text="Delete Attendance", command=self.delete_attendance)
        self.class_popularity_button = tk.Button(self.frame, text="Class Popularity Report", command=self.save_class_popularity_report)
        self.peak_hours_button = tk.Button(self.frame, text="Peak Hours Report", command=self.save_peak_hours_report)

        self.log_button.grid(row=4, column=0, pady=10)
        self.update_button.grid(row=4, column=1, pady=10)
        self.view_button.grid(row=5, column=0, pady=10)
        self.delete_button.grid(row=5, column=1, pady=10)
        self.class_popularity_button.grid(row=6, column=0, pady=10)
        self.peak_hours_button.grid(row=6, column=1, pady=10)

    def log_attendance(self):
        record_id = self.record_id_entry.get()
        member_id = self.member_id_entry.get()
        date_time = self.date_time_entry.get()
        activity_type = self.activity_type_entry.get()

        if not record_id or not member_id or not date_time or not activity_type:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        self.controller.log_attendance(record_id, member_id, date_time, activity_type)
        messagebox.showinfo("Success", "Attendance logged successfully")
        self.clear_entries()

    def update_attendance(self):
        record_id = self.record_id_entry.get()
        member_id = self.member_id_entry.get()
        date_time = self.date_time_entry.get()
        activity_type = self.activity_type_entry.get()

        if not record_id:
            messagebox.showwarning("Input Error", "Record ID must be provided")
            return

        self.controller.update_attendance_record(record_id, member_id, date_time, activity_type)
        messagebox.showinfo("Success", "Attendance updated successfully")
        self.clear_entries()

    def view_attendance(self):
        record_id = self.record_id_entry.get()
        if not record_id:
            messagebox.showwarning("Input Error", "Record ID must be provided")
            return

        record = self.controller.get_attendance_record_by_id(record_id)
        if record:
            messagebox.showinfo("Attendance Details", f"Record ID: {record.record_id}\nMember ID: {record.member_id}\nDate Time: {record.date_time}\nActivity Type: {record.activity_type}")
        else:
            messagebox.showwarning("Not Found", "Attendance record not found")

    def delete_attendance(self):
        record_id = self.record_id_entry.get()
        if not record_id:
            messagebox.showwarning("Input Error", "Record ID must be provided")
            return

        self.controller.remove_attendance_record(record_id)
        messagebox.showinfo("Success", "Attendance record deleted successfully")
        self.clear_entries()

    def save_class_popularity_report(self):
        report_file = 'data/class_popularity_report.csv'
        self.controller.save_class_popularity_report(report_file)
        messagebox.showinfo("Success", f"Class popularity report saved to {report_file}")

    def save_peak_hours_report(self):
        report_file = 'data/peak_hours_report.csv'
        self.controller.save_peak_hours_report(report_file)
        messagebox.showinfo("Success", f"Peak hours report saved to {report_file}")

    def clear_entries(self):
        self.record_id_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.date_time_entry.delete(0, tk.END)
        self.activity_type_entry.delete(0, tk.END)

