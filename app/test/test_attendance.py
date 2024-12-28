import unittest
from src.services.attendance_service import AttendanceService

class TestAttendanceService(unittest.TestCase):

    def setUp(self):
        self.service = AttendanceService(csv_file='../data/attendance.csv')
        self.service.log_attendance('R001', 'M001', '2024-12-10 09:00', 'Workout')

    def test_log_attendance(self):
        self.service.log_attendance('R002', 'M002', '2024-12-11 10:00', 'Class')
        record = self.service.get_attendance_record_by_id('R002')
        self.assertIsNotNone(record)
        self.assertEqual(record.activity_type, 'Class')

    def test_get_attendance_record_by_id(self):
        record = self.service.get_attendance_record_by_id('R001')
        self.assertIsNotNone(record)
        self.assertEqual(record.date_time, '2024-12-10 09:00')

    def test_update_attendance_record(self):
        self.service.update_attendance_record('R001', activity_type='Class')
        record = self.service.get_attendance_record_by_id('R001')
        self.assertEqual(record.activity_type, 'Class')

    def test_remove_attendance_record(self):
        self.service.remove_attendance_record('R001')
        record = self.service.get_attendance_record_by_id('R001')
        self.assertIsNone(record)

if __name__ == '__main__':
    unittest.main()