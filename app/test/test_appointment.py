import unittest
from src.services.appointment_service import AppointmentService

class TestAppointmentService(unittest.TestCase):

    def setUp(self):
        self.service = AppointmentService(csv_file='../data/appointments.csv')
        self.service.add_appointment('A001', 'M001', 'T001', 'Training', '2024-12-20 08:00', 'Scheduled')

    def test_add_appointment(self):
        self.service.add_appointment('A002', 'M002', 'T002', 'Consultation', '2024-12-21 10:00', 'Scheduled')
        appointment = self.service.get_appointment_by_id('A002')
        self.assertIsNotNone(appointment)
        self.assertEqual(appointment.appointment_type, 'Consultation')

    def test_get_appointment_by_id(self):
        appointment = self.service.get_appointment_by_id('A001')
        self.assertIsNotNone(appointment)
        self.assertEqual(appointment.status, 'Scheduled')

    def test_update_appointment(self):
        self.service.update_appointment('A001', status='Completed')
        appointment = self.service.get_appointment_by_id('A001')
        self.assertEqual(appointment.status, 'Completed')

    def test_remove_appointment(self):
        self.service.remove_appointment('A001')
        appointment = self.service.get_appointment_by_id('A001')
        self.assertIsNone(appointment)

if __name__ == '__main__':
    unittest.main()