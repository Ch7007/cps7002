class AttendanceRecord:
    def __init__(self, record_id, member_id, date_time, activity_type):
        self.record_id = record_id
        self.member_id = member_id
        self.date_time = date_time
        self.activity_type = activity_type
    def to_dict(self):
        return {
            'record_id': self.record_id,
            'member_id': self.member_id,
            'date_time': self.date_time,
            'activity_type': self.activity_type
        }

    def __repr__(self):
        return f"<AttendanceRecord {self.record_id} - {self.member_id} - {self.activity_type}>"