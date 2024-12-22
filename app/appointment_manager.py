import json
import os
import uuid
from datetime import datetime

class AppointmentManager:
    def __init__(self, data_file="data/appointments.json"):
        self.data_file = data_file
        self.appointments = self.load_data()

    def load_data(self):
        """Loads appointment data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        """Saves appointment data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.appointments, file, indent=4)

    def book_appointment(self, member_id, trainer_id, date, time, appointment_type):
        """Books a new appointment."""
        appointment_id = str(uuid.uuid4())
        appointment_datetime = f"{date} {time}"
        if not self.validate_datetime(appointment_datetime):
            return f"Invalid date or time format. Expected 'YYYY-MM-DD' and 'HH:MM'."

        self.appointments[appointment_id] = {
            "member_id": member_id,
            "trainer_id": trainer_id,
            "datetime": appointment_datetime,
            "type": appointment_type,
            "status": "Scheduled"
        }
        self.save_data()
        return f"Appointment booked successfully with ID {appointment_id}."

    def cancel_appointment(self, appointment_id):
        """Cancels an existing appointment."""
        if appointment_id not in self.appointments:
            return f"Appointment with ID {appointment_id} does not exist."
        self.appointments[appointment_id]["status"] = "Canceled"
        self.save_data()
        return f"Appointment {appointment_id} canceled successfully."

    def get_appointments_for_member(self, member_id):
        """Retrieves all appointments for a specific member."""
        return {k: v for k, v in self.appointments.items() if v["member_id"] == member_id}

    def get_all_appointments(self):
        """Returns all appointments."""
        return self.appointments

    @staticmethod
    def validate_datetime(appointment_datetime):
        """Validates the date and time format."""
        try:
            datetime.strptime(appointment_datetime, "%Y-%m-%d %H:%M")
            return True
        except ValueError:
            return False
