from src.services.payment_service import PaymentService

class PaymentController:
    def __init__(self):
        self.service = PaymentService()

    def add_payment(self, payment_id, member_id, amount, date, method):
        return self.service.add_payment(payment_id, member_id, amount, date, method)

    def get_all_payments(self):
        return self.service.get_payments()

    def get_payment_by_id(self, payment_id):
        return self.service.get_payment_by_id(payment_id)

    def update_payment(self, payment_id, member_id=None, amount=None, date=None, method=None):
        return self.service.update_payment(payment_id, member_id, amount, date, method)

    def remove_payment(self, payment_id):
        return self.service.remove_payment(payment_id)