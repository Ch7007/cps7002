from src.models.attendance_record import AttendanceRecord
from src.utils.csv_processor import CSVProcessor

class AttendanceService:
    def __init__(self, csv_file='data/attendance.csv'):
        self.csv_file = csv_file
        self.fieldnames = ['record_id', 'member_id', 'date_time', 'activity_type']
        self.attendance_records = self.load_attendance_records()

    def load_attendance_records(self):
        data = CSVProcessor.read_csv(self.csv_file)
        attendance_records = [AttendanceRecord(**record) for record in data]
        return attendance_records

    def save_attendance_records(self):
        data = [record.to_dict() for record in self.attendance_records]
        CSVProcessor.write_csv(self.csv_file, data, self.fieldnames)

    def log_attendance(self, record_id, member_id, date_time, activity_type):
        attendance = AttendanceRecord(record_id, member_id, date_time, activity_type)
        self.attendance_records.append(attendance)
        self.save_attendance_records()
        return attendance

    def get_all_attendance_records(self):
        return self.attendance_records

    def get_attendance_record_by_id(self, record_id):
        for record in self.attendance_records:
            if record.record_id == record_id:
                return record
        return None

    def update_attendance_record(self, record_id, member_id=None, date_time=None, activity_type=None):
        record = self.get_attendance_record_by_id(record_id)
        if record:
            if member_id: record.member_id = member_id
            if date_time: record.date_time = date_time
            if activity_type: record.activity_type = activity_type
            self.save_attendance_records()
            return record
        return None

    def get_attendance_by_date(self, date):
        return [record for record in self.attendance_records if record.date_time.date() == date]

    def get_class_popularity(self):
        class_attendance = [record for record in self.attendance_records if record.activity_type == 'class']
        popularity = {}
        for record in class_attendance:
            date = record.date_time.date()
            if date not in popularity:
                popularity[date] = 0
            popularity[date] += 1
        return popularity

    def save_class_popularity_report(self, report_file='data/class_popularity_report.csv'):
        popularity = self.get_class_popularity()
        report_data = [{'date': date, 'attendance_count': count} for date, count in popularity.items()]
        CSVProcessor.write_csv(report_file, report_data, ['date', 'attendance_count'])

    def get_peak_hours(self):
        hours = [record.date_time.hour for record in self.attendance_records]
        peak_hours = {}
        for hour in hours:
            if hour not in peak_hours:
                peak_hours[hour] = 0
            peak_hours[hour] += 1
        return peak_hours

    def save_peak_hours_report(self, report_file='data/peak_hours_report.csv'):
        peak_hours = self.get_peak_hours()
        report_data = [{'hour': hour, 'attendance_count': count} for hour, count in peak_hours.items()]
        CSVProcessor.write_csv(report_file, report_data, ['hour', 'attendance_count'])

    def remove_attendance_record(self, record_id):
        record = self.get_attendance_record_by_id(record_id)
        if record:
            self.attendance_records.remove(record)
            self.save_attendance_records()
            return True
        return False