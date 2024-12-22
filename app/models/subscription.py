class Subscription:
    def __init__(self, subscription_id, member_id, plan_id, start_date, end_date, status):
        self.subscription_id = subscription_id
        self.member_id = member_id
        self.plan_id = plan_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def to_dict(self):
        return {
            'subscription_id': self.subscription_id,
            'member_id': self.member_id,
            'plan_id': self.plan_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'status': self.status
        }

    def __repr__(self):
        return f"<Subscription {self.subscription_id} - {self.status}>"