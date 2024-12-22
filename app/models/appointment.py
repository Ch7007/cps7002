class Appointment:
    def __init__(self, appointment_id, member_id, trainer_id, appointment_type, date_time, status):
        self.appointment_id = appointment_id
        self.member_id = member_id
        self.trainer_id = trainer_id
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.status = status

    def to_dict(self):
        return {
            'appointment_id': self.appointment_id,
            'member_id': self.member_id,
            'trainer_id': self.trainer_id,
            'appointment_type': self.appointment_type,
            'date_time': self.date_time,
            'status': self.status
        }

    def __repr__(self):
        return f"<Appointment {self.appointment_id} - {self.appointment_type}>"