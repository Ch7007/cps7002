from src.models.payment import Payment
from src.utils.csv_processor import CSVProcessor

class PaymentService:
    def __init__(self, csv_file='data/payments.csv'):
        self.csv_file = csv_file
        self.fieldnames = ['payment_id', 'member_id', 'amount', 'date', 'method']
        self.payments = self.load_payments()

    def load_payments(self):
        data = CSVProcessor.read_csv(self.csv_file)
        payments = [Payment(**record) for record in data]
        return payments

    def save_payments(self):
        data = [payment.to_dict() for payment in self.payments]
        CSVProcessor.write_csv(self.csv_file, data, self.fieldnames)

    def add_payment(self, payment_id, member_id, amount, date, method):
        payment = Payment(payment_id, member_id, amount, date, method)
        self.payments.append(payment)
        self.save_payments()
        return payment

    def get_payments(self):
        return self.payments

    def get_payment_by_id(self, payment_id):
        for payment in self.payments:
            if payment.payment_id == payment_id:
                return payment
        return None

    def update_payment(self, payment_id, member_id=None, amount=None, date=None, method=None):
        payment = self.get_payment_by_id(payment_id)
        if payment:
            if member_id: payment.member_id = member_id
            if amount: payment.amount = amount
            if date: payment.date = date
            if method: payment.method = method
            self.save_payments()
            return payment
        return None

    def remove_payment(self, payment_id):
        payment = self.get_payment_by_id(payment_id)
        if payment:
            self.payments.remove(payment)
            self.save_payments()
            return True
        return False