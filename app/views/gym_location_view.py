import tkinter as tk
from tkinter import messagebox
from src.controllers.gym_location_controller import GymLocationController

class GymLocationView:
    def __init__(self, root):
        self.root = root
        self.controller = GymLocationController()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Location ID:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self.frame, text="City:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Manager Name:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Workout Zones:").grid(row=3, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Equipment:").grid(row=4, column=0, sticky=tk.E)
        tk.Label(self.frame, text="Amenities:").grid(row=5, column=0, sticky=tk.E)

        self.location_id_entry = tk.Entry(self.frame)
        self.city_entry = tk.Entry(self.frame)
        self.manager_name_entry = tk.Entry(self.frame)
        self.workout_zones_entry = tk.Entry(self.frame)
        self.equipment_entry = tk.Entry(self.frame)
        self.amenities_entry = tk.Entry(self.frame)

        self.location_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.city_entry.grid(row=1, column=1, padx=10, pady=5)
        self.manager_name_entry.grid(row=2, column=1, padx=10, pady=5)
        self.workout_zones_entry.grid(row=3, column=1, padx=10, pady=5)
        self.equipment_entry.grid(row=4, column=1, padx=10, pady=5)
        self.amenities_entry.grid(row=5, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Location", command=self.add_location)
        self.update_button = tk.Button(self.frame, text="Update Location", command=self.update_location)
        self.view_button = tk.Button(self.frame, text="View Location", command=self.view_location)
        self.delete_button = tk.Button(self.frame, text="Delete Location", command=self.delete_location)

        self.add_button.grid(row=6, column=0, pady=10)
        self.update_button.grid(row=6, column=1, pady=10)
        self.view_button.grid(row=7, column=0, pady=10)
        self.delete_button.grid(row=7, column=1, pady=10)

    def add_location(self):
        location_id = self.location_id_entry.get()
        city = self.city_entry.get()
        manager_name = self.manager_name_entry.get()
        workout_zones = self.workout_zones_entry.get()
        equipment = self.equipment_entry.get()
        amenities = self.amenities_entry.get()

        if not location_id or not city or not manager_name or not workout_zones or not equipment or not amenities:
            messagebox.showwarning("Input Error", "All fields must be filled out")
            return

        self.controller.add_gym_location(location_id, city, manager_name, workout_zones.split(','), equipment.split(','), amenities.split(','))
        messagebox.showinfo("Success", "Gym location added successfully")
        self.clear_entries()

    def update_location(self):
        location_id = self.location_id_entry.get()
        city = self.city_entry.get()
        manager_name = self.manager_name_entry.get()
        workout_zones = self.workout_zones_entry.get()
        equipment = self.equipment_entry.get()
        amenities = self.amenities_entry.get()

        if not location_id:
            messagebox.showwarning("Input Error", "Location ID must be provided")
            return

        self.controller.update_gym_location(location_id, city=city, manager_name=manager_name, workout_zones=workout_zones.split(','), equipment=equipment.split(','), amenities=amenities.split(','))
        messagebox.showinfo("Success", "Gym location updated successfully")
        self.clear_entries()

    def view_location(self):
        location_id = self.location_id_entry.get()
        if not location_id:
            messagebox.showwarning("Input Error", "Location ID must be provided")
            return

        location = self.controller.get_gym_location_by_id(location_id)
        if location:
            messagebox.showinfo("Gym Location Details", f"Location ID: {location.location_id}\nCity: {location.city}\nManager Name: {location.manager_name}\nWorkout Zones: {', '.join(location.workout_zones)}\nEquipment: {', '.join(location.equipment)}\nAmenities: {', '.join(location.amenities)}")
        else:
            messagebox.showwarning("Not Found", "Gym location not found")

    def delete_location(self):
        location_id = self.location_id_entry.get()
        if not location_id:
            messagebox.showwarning("Input Error", "Location ID must be provided")
            return

        self.controller.remove_gym_location(location_id)
        messagebox.showinfo("Success", "Gym location deleted successfully")
        self.clear_entries()

    def clear_entries(self):
        self.location_id_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.manager_name_entry.delete(0, tk.END)
        self.workout_zones_entry.delete(0, tk.END)
        self.equipment_entry.delete(0, tk.END)
        self.amenities_entry.delete(0, tk.END)
