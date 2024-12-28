import tkinter as tk
from tkinter import ttk
from src.views.gym_location_view import GymLocationView
from src.views.workout_zone_view import WorkoutZoneView
from src.views.member_profile_view import MemberProfileView
from src.views.appointment_view import AppointmentView
from src.views.attendance_view import AttendanceView
from src.views.payment_view import PaymentView
from src.views.subscription_view import SubscriptionView
from src.views.staff_dashboard_view import StaffDashboardView

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("St Mary's Fitness Management System")

        self.tab_control = ttk.Notebook(root)

        self.gym_location_tab = ttk.Frame(self.tab_control)
        self.workout_zone_tab = ttk.Frame(self.tab_control)
        self.member_profile_tab = ttk.Frame(self.tab_control)
        self.appointment_tab = ttk.Frame(self.tab_control)
        self.attendance_tab = ttk.Frame(self.tab_control)
        self.payment_tab = ttk.Frame(self.tab_control)
        self.subscription_tab = ttk.Frame(self.tab_control)
        self.staff_dashboard_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.gym_location_tab, text="Gym Locations")
        self.tab_control.add(self.workout_zone_tab, text="Workout Zones")
        self.tab_control.add(self.member_profile_tab, text="Member Profiles")
        self.tab_control.add(self.appointment_tab, text="Appointments")
        self.tab_control.add(self.attendance_tab, text="Attendance")
        self.tab_control.add(self.payment_tab, text="Payments")
        self.tab_control.add(self.subscription_tab, text="Subscriptions")
        self.tab_control.add(self.staff_dashboard_tab, text="Staff Dashboard")

        self.tab_control.pack(expand=1, fill="both")

        self.gym_location_view = GymLocationView(self.gym_location_tab)
        self.workout_zone_view = WorkoutZoneView(self.workout_zone_tab)
        self.member_profile_view = MemberProfileView(self.member_profile_tab)
        self.appointment_view = AppointmentView(self.appointment_tab)
        self.attendance_view = AttendanceView(self.attendance_tab)
        self.payment_view = PaymentView(self.payment_tab)
        self.subscription_view = SubscriptionView(self.subscription_tab)
        self.staff_dashboard_view = StaffDashboardView(self.staff_dashboard_tab)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()