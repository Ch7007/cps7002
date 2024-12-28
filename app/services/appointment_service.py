from src.models.appointment import Appointment
from src.utils.csv_processor import CSVProcessor

class AppointmentService:
    def __init__(self, csv_file='data/appointments.csv'):
        self.csv_file = csv_file
        self.fieldnames = ['appointment_id', 'member_id', 'trainer_id', 'appointment_type', 'date_time', 'status']
        self.appointments = self.load_appointments()

    def load_appointments(self):
        data = CSVProcessor.read_csv(self.csv_file)
        appointments = [Appointment(**record) for record in data]
        return appointments

    def save_appointments(self):
        data = [appointment.to_dict() for appointment in self.appointments]
        CSVProcessor.write_csv(self.csv_file, data, self.fieldnames)

    def add_appointment(self, appointment_id, member_id, trainer_id, appointment_type, date_time, status):
        appointment = Appointment(appointment_id, member_id, trainer_id, appointment_type, date_time, status)
        self.appointments.append(appointment)
        self.save_appointments()
        return appointment

    def get_appointments(self):
        return self.appointments

    def get_appointment_by_id(self, appointment_id):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        return None

    def update_appointment(self, appointment_id, member_id=None, trainer_id=None, appointment_type=None, date_time=None, status=None):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            if member_id: appointment.member_id = member_id
            if trainer_id: appointment.trainer_id = trainer_id
            if appointment_type: appointment.appointment_type = appointment_type
            if date_time: appointment.date_time = date_time
            if status: appointment.status = status
            self.save_appointments()
            return appointment
        return None

    def remove_appointment(self, appointment_id):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            self.appointments.remove(appointment)
            self.save_appointments()
            return True
        return False