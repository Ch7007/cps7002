from src.services.subscription_service import SubscriptionService

class SubscriptionController:
    def __init__(self):
        self.service = SubscriptionService()

    def add_subscription_plan(self, plan_id, name, duration, price):
        return self.service.add_subscription_plan(plan_id, name, duration, price)

    def get_all_subscription_plans(self):
        return self.service.get_all_subscription_plans()

    def add_subscription(self, subscription_id, member_id, plan_id, start_date, end_date, status):
        return self.service.add_subscription(subscription_id, member_id, plan_id, start_date, end_date, status)

    def get_all_subscriptions(self):
        return self.service.get_all_subscriptions()

    def update_subscription(self, subscription_id, **kwargs):
        return self.service.update_subscription(subscription_id, **kwargs)

    def delete_subscription(self, subscription_id):
        return self.service.delete_subscription(subscription_id)