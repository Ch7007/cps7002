class Payment:
    def __init__(self, payment_id, member_id, amount, date, method):
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.date = date
        self.method = method

    def to_dict(self):
        return {
            'payment_id': self.payment_id,
            'member_id': self.member_id,
            'amount': self.amount,
            'date': self.date,
            'method': self.method
        }

    def __repr__(self):
        return f"<Payment {self.payment_id} - {self.amount}>"