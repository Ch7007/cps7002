import unittest
from src.services.payment_service import PaymentService

class TestPaymentService(unittest.TestCase):

    def setUp(self):
        self.service = PaymentService(csv_file='../data/payments.csv')
        self.service.add_payment('P001', 'M001', 100.0, '2024-12-01', 'Credit Card')

    def test_add_payment(self):
        self.service.add_payment('P002', 'M002', 150.0, '2024-12-05', 'Cash')
        payment = self.service.get_payment_by_id('P002')
        self.assertIsNotNone(payment)
        self.assertEqual(payment.amount, 150.0)

    def test_get_payment_by_id(self):
        payment = self.service.get_payment_by_id('P001')
        self.assertIsNotNone(payment)
        self.assertEqual(payment.method, 'Credit Card')

    def test_update_payment(self):
        self.service.update_payment('P001', amount=120.0)
        payment = self.service.get_payment_by_id('P001')
        self.assertEqual(payment.amount, 120.0)

    def test_remove_payment(self):
        self.service.remove_payment('P001')
        payment = self.service.get_payment_by_id('P001')
        self.assertIsNone(payment)

if __name__ == '__main__':
    unittest.main()