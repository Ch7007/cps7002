import tkinter as tk
from tkinter import messagebox
from src.controllers.workout_zone_controller import WorkoutZoneController

class WorkoutZoneView:
    def __init__(self, root):
        self.root = root
        self.controller = WorkoutZoneController()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Zone ID:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Location ID:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Name:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Equipment List:").grid(row=3, column=0, sticky=tk.E)

        self.zone_id_entry = tk.Entry(self.frame)
        self.location_id_entry = tk.Entry(self.frame)
        self.name_entry = tk.Entry(self.frame)
        self.equipment_list_entry = tk.Entry(self.frame)

        self.zone_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.location_id_entry.grid(row=1, column=1, padx=10, pady=5)
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)
        self.equipment_list_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Zone", command=self.add_zone)
        self.update_button = tk.Button(self.frame, text="Update Zone", command=self.update_zone)
        self.view_button = tk.Button(self.frame, text="View Zone", command=self.view_zone)
        self.delete_button = tk.Button(self.frame, text="Delete Zone", command=self.delete_zone)

        self.add_button.grid(row=4, column=0, pady=10)
        self.update_button.grid(row=4, column=1, pady=10)
        self.view_button.grid(row=5, column=0, pady=10)
        self.delete_button.grid(row=5, column=1, pady=10)

    def add_zone(self):
        zone_id = self.zone_id_entry.get()
        location_id = self.location_id_entry.get()
        name = self.name_entry.get()
        equipment_list = self.equipment_list_entry.get().split(',')

        if not zone_id or not location_id or not name or not equipment_list:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        self.controller.add_workout_zone(zone_id, location_id, name, equipment_list)
        messagebox.showinfo("Success", "Workout zone added successfully")
        self.clear_entries()

    def update_zone(self):
        zone_id = self.zone_id_entry.get()
        location_id = self.location_id_entry.get()
        name = self.name_entry.get()
        equipment_list = self.equipment_list_entry.get().split(',')

        if not zone_id:
            messagebox.showwarning("Input Error", "Zone ID must be provided")
            return

        self.controller.update_workout_zone(zone_id, location_id=location_id, name=name, equipment_list=equipment_list)
        messagebox.showinfo("Success", "Workout zone updated successfully")
        self.clear_entries()

    def view_zone(self):
        zone_id = self.zone_id_entry.get()
        if not zone_id:
            messagebox.showwarning("Input Error", "Zone ID must be provided")
            return

        zone = self.controller.get_workout_zone_by_id(zone_id)
        if zone:
            equipment_list = ', '.join(zone.equipment_list)
            messagebox.showinfo("Workout Zone Details", f"Zone ID: {zone.zone_id}\nLocation ID: {zone.location_id}\nName: {zone.name}\nEquipment List: {equipment_list}")
        else:
            messagebox.showwarning("Not Found", "Workout zone not found")

    def delete_zone(self):
        zone_id = self.zone_id_entry.get()
        if not zone_id:
            messagebox.showwarning("Input Error", "Zone ID must be provided")
            return

        self.controller.remove_workout_zone(zone_id)
        messagebox.showinfo("Success", "Workout zone deleted successfully")
        self.clear_entries()

    def clear_entries(self):
        self.zone_id_entry.delete(0, tk.END)
        self.location_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.equipment_list_entry.delete(0, tk.END)
