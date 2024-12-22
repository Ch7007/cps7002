class SubscriptionPlan:
    def __init__(self, plan_id, name, duration, price):
        self.plan_id = plan_id
        self.name = name
        self.duration = duration
        self.price = price

    def to_dict(self):
        return {
            'plan_id': self.plan_id,
            'name': self.name,
            'duration': self.duration,
            'price': self.price
        }

    def __repr__(self):
        return f"<SubscriptionPlan {self.plan_id} - {self.name}>"