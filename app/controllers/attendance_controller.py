from src.services.attendance_service import AttendanceService

class AttendanceController:
    def __init__(self):
        self.service = AttendanceService()

    def log_attendance(self, record_id, member_id, date_time, activity_type):
        return self.service.log_attendance(record_id, member_id, date_time, activity_type)

    def get_all_attendance_records(self):
        return self.service.get_all_attendance_records()

    def get_attendance_record_by_id(self, record_id):
        return self.service.get_attendance_record_by_id(record_id)

    def update_attendance_record(self, record_id, member_id=None, date_time=None, activity_type=None):
        return self.service.update_attendance_record(record_id, member_id, date_time, activity_type)

    def get_attendance_by_date(self, date):
        return self.service.get_attendance_by_date(date)

    def get_class_popularity(self):
        return self.service.get_class_popularity()

    def save_class_popularity_report(self, report_file='data/class_popularity_report.csv'):
        self.service.save_class_popularity_report(report_file)

    def get_peak_hours(self):
        return self.service.get_peak_hours()

    def save_peak_hours_report(self, report_file='data/peak_hours_report.csv'):
        self.service.save_peak_hours_report(report_file)

    def remove_attendance_record(self, record_id):
        return self.service.remove_attendance_record(record_id)