from src.services.appointment_service import AppointmentService

class AppointmentController:
    def __init__(self):
        self.service = AppointmentService()

    def add_appointment(self, appointment_id, member_id, trainer_id, appointment_type, date_time, status):
        return self.service.add_appointment(appointment_id, member_id, trainer_id, appointment_type, date_time, status)

    def get_appointments(self):
        return self.service.get_appointments()

    def get_appointment_by_id(self, appointment_id):
        return self.service.get_appointment_by_id(appointment_id)

    def update_appointment(self, appointment_id, member_id=None, trainer_id=None, appointment_type=None, date_time=None, status=None):
        return self.service.update_appointment(appointment_id, member_id, trainer_id, appointment_type, date_time, status)

    def remove_appointment(self, appointment_id):
        return self.service.remove_appointment(appointment_id)