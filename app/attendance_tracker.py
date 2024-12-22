import json
import os
from datetime import datetime

class AttendanceTracker:
    def __init__(self, data_file="data/attendance.json"):
        self.data_file = data_file
        self.attendance_records = self.load_data()

    def load_data(self):
        """Loads attendance records from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        """Saves attendance records to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.attendance_records, file, indent=4)

    def log_attendance(self, member_id, class_id=None, facility_use=False):
        """Logs attendance for a member."""
        record_id = f"{member_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.attendance_records[record_id] = {
            "member_id": member_id,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "class_id": class_id,
            "facility_use": facility_use
        }
        self.save_data()
        return f"Attendance logged successfully for member {member_id}."

    def get_attendance_for_member(self, member_id):
        """Retrieves attendance records for a specific member."""
        return {k: v for k, v in self.attendance_records.items() if v["member_id"] == member_id}

    def generate_report(self):
        """Generates an attendance report."""
        report = {}
        for record in self.attendance_records.values():
            member_id = record["member_id"]
            report[member_id] = report.get(member_id, 0) + 1
        return report
