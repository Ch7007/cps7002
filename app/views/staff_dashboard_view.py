import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.staff_dashboard_controller import StaffDashboardController

class StaffDashboardView:
    def __init__(self, root):
        self.controller = StaffDashboardController()
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)

        self.membership_growth_frame = ttk.Frame(self.notebook)
        self.revenue_trends_frame = ttk.Frame(self.notebook)
        self.trainer_schedules_frame = ttk.Frame(self.notebook)
        self.equipment_maintenance_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.membership_growth_frame, text="Membership Growth")
        self.notebook.add(self.revenue_trends_frame, text="Revenue Trends")
        self.notebook.add(self.trainer_schedules_frame, text="Trainer Schedules")
        self.notebook.add(self.equipment_maintenance_frame, text="Equipment Maintenance")

        self.notebook.pack(expand=1, fill="both")

        self.create_membership_growth_widgets()
        self.create_revenue_trends_widgets()
        self.create_trainer_schedules_widgets()
        self.create_equipment_maintenance_widgets()

    def create_membership_growth_widgets(self):
        self.month_label = tk.Label(self.membership_growth_frame, text="Month")
        self.month_entry = tk.Entry(self.membership_growth_frame)
        self.new_members_label = tk.Label(self.membership_growth_frame, text="New Members")
        self.new_members_entry = tk.Entry(self.membership_growth_frame)
        self.cancellations_label = tk.Label(self.membership_growth_frame, text="Cancellations")
        self.cancellations_entry = tk.Entry(self.membership_growth_frame)
        self.add_growth_button = tk.Button(self.membership_growth_frame, text="Add Growth Record", command=self.add_membership_growth)
        self.view_growth_button = tk.Button(self.membership_growth_frame, text="View Growth Records", command=self.view_membership_growth)

        self.month_label.grid(row=0, column=0, padx=10, pady=5)
        self.month_entry.grid(row=0, column=1, padx=10, pady=5)
        self.new_members_label.grid(row=1, column=0, padx=10, pady=5)
        self.new_members_entry.grid(row=1, column=1, padx=10, pady=5)
        self.cancellations_label.grid(row=2, column=0, padx=10, pady=5)
        self.cancellations_entry.grid(row=2, column=1, padx=10, pady=5)
        self.add_growth_button.grid(row=3, column=0, padx=10, pady=10)
        self.view_growth_button.grid(row=3, column=1, padx=10, pady=10)

    def create_revenue_trends_widgets(self):
        self.revenue_month_label = tk.Label(self.revenue_trends_frame, text="Month")
        self.revenue_month_entry = tk.Entry(self.revenue_trends_frame)
        self.revenue_label = tk.Label(self.revenue_trends_frame, text="Revenue")
        self.revenue_entry = tk.Entry(self.revenue_trends_frame)
        self.add_revenue_button = tk.Button(self.revenue_trends_frame, text="Add Revenue Record", command=self.add_revenue_trend)
        self.view_revenue_button = tk.Button(self.revenue_trends_frame, text="View Revenue Records", command=self.view_revenue_trends)

        self.revenue_month_label.grid(row=0, column=0, padx=10, pady=5)
        self.revenue_month_entry.grid(row=0, column=1, padx=10, pady=5)
        self.revenue_label.grid(row=1, column=0, padx=10, pady=5)
        self.revenue_entry.grid(row=1, column=1, padx=10, pady=5)
        self.add_revenue_button.grid(row=2, column=0, padx=10, pady=10)
        self.view_revenue_button.grid(row=2, column=1, padx=10, pady=10)

    def create_trainer_schedules_widgets(self):
        self.trainer_id_label = tk.Label(self.trainer_schedules_frame, text="Trainer ID")
        self.trainer_id_entry = tk.Entry(self.trainer_schedules_frame)
        self.trainer_name_label = tk.Label(self.trainer_schedules_frame, text="Trainer Name")
        self.trainer_name_entry = tk.Entry(self.trainer_schedules_frame)
        self.schedule_label = tk.Label(self.trainer_schedules_frame, text="Schedule (date, time, session_type)")
        self.schedule_entry = tk.Entry(self.trainer_schedules_frame)
        self.add_schedule_button = tk.Button(self.trainer_schedules_frame, text="Add Schedule", command=self.add_trainer_schedule)
        self.view_schedules_button = tk.Button(self.trainer_schedules_frame, text="View Schedules", command=self.view_trainer_schedules)

        self.trainer_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.trainer_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.trainer_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.trainer_name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.schedule_label.grid(row=2, column=0, padx=10, pady=5)
        self.schedule_entry.grid(row=2, column=1, padx=10, pady=5)
        self.add_schedule_button.grid(row=3, column=0, padx=10, pady=10)
        self.view_schedules_button.grid(row=3, column=1, padx=10, pady=10)

    def create_equipment_maintenance_widgets(self):
        self.equipment_id_label = tk.Label(self.equipment_maintenance_frame, text="Equipment ID")
        self.equipment_id_entry = tk.Entry(self.equipment_maintenance_frame)
        self.equipment_name_label = tk.Label(self.equipment_maintenance_frame, text="Equipment Name")
        self.equipment_name_entry = tk.Entry(self.equipment_maintenance_frame)
        self.maintenance_date_label = tk.Label(self.equipment_maintenance_frame, text="Maintenance Date")
        self.maintenance_date_entry = tk.Entry(self.equipment_maintenance_frame)
        self.status_label = tk.Label(self.equipment_maintenance_frame, text="Status")
        self.status_entry = tk.Entry(self.equipment_maintenance_frame)
        self.add_maintenance_button = tk.Button(self.equipment_maintenance_frame, text="Add Maintenance Record", command=self.add_equipment_maintenance)
        self.view_maintenance_button = tk.Button(self.equipment_maintenance_frame, text="View Maintenance Records", command=self.view_equipment_maintenance)

        self.equipment_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.equipment_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.equipment_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.equipment_name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.maintenance_date_label.grid(row=2, column=0, padx=10, pady=5)
        self.maintenance_date_entry.grid(row=2, column=1, padx=10, pady=5)
        self.status_label.grid(row=3, column=0, padx=10, pady=5)
        self.status_entry.grid(row=3, column=1, padx=10, pady=5)
        self.add_maintenance_button.grid(row=4, column=0, padx=10, pady=10)
        self.view_maintenance_button.grid(row=4, column=1, padx=10, pady=10)

    def add_membership_growth(self):
        month = self.month_entry.get()
        new_members = int(self.new_members_entry.get())
        cancellations = int(self.cancellations_entry.get())

        self.controller.create_membership_growth(month, new_members, cancellations)
        messagebox.showinfo("Success", "Membership Growth Record Added Successfully")

    def view_membership_growth(self):
        growth_records = self.controller.get_membership_growth()
        growth_str = "\n".join([f"{record.month}: +{record.new_members}, -{record.cancellations}" for record in growth_records])
        messagebox.showinfo("Membership Growth Records", growth_str)

    def add_revenue_trend(self):
        month = self.revenue_month_entry.get()
        revenue = float(self.revenue_entry.get())

        self.controller.create_revenue_trend(month, revenue)
        messagebox.showinfo("Success", "Revenue Trend Record Added Successfully")

    def view_revenue_trends(self):
        revenue_records = self.controller.get_revenue_trends()
        revenue_str = "\n".join([f"{record.month}: ${record.revenue}" for record in revenue_records])
        messagebox.showinfo("Revenue Trend Records", revenue_str)

    def add_trainer_schedule(self):
        trainer_id = self.trainer_id_entry.get()
        trainer_name = self.trainer_name_entry.get()
        schedule = eval(self.schedule_entry.get())

        self.controller.create_trainer_schedule(trainer_id, trainer_name, schedule)
        messagebox.showinfo("Success", "Trainer Schedule Added Successfully")

    def view_trainer_schedules(self):
        schedules = self.controller.get_trainer_schedules()
        schedules_str = "\n".join([f"{schedule.trainer_name} ({schedule.trainer_id}): {schedule.schedule}" for schedule in schedules])
        messagebox.showinfo("Trainer Schedules", schedules_str)

    def add_equipment_maintenance(self):
        equipment_id = self.equipment_id_entry.get()
        equipment_name = self.equipment_name_entry.get()
        maintenance_date = self.maintenance_date_entry.get()
        status = self.status_entry.get()

        self.controller.create_equipment_maintenance(equipment_id, equipment_name, maintenance_date, status)
        messagebox.showinfo("Success", "Equipment Maintenance Record Added Successfully")

    def view_equipment_maintenance(self):
        maintenance_records = self.controller.get_equipment_maintenance()
        maintenance_str = "\n".join([f"{record.equipment_name} ({record.equipment_id}) - {record.maintenance_date}: {record.status}" for record in maintenance_records])
        messagebox.showinfo("Equipment Maintenance Records", maintenance_str)