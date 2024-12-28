from src.models.subscription_plan import SubscriptionPlan
from src.models.subscription import Subscription
from src.utils.csv_processor import CSVProcessor

class SubscriptionService:
    def __init__(self, plans_csv='data/subscription_plans.csv', subscriptions_csv='data/subscriptions.csv'):
        self.plans_csv = plans_csv
        self.subscriptions_csv = subscriptions_csv
        self.plan_fieldnames = ['plan_id', 'name', 'duration', 'price']
        self.subscription_fieldnames = ['subscription_id', 'member_id', 'plan_id', 'start_date', 'end_date', 'status']
        self.plans = self.load_subscription_plans()
        self.subscriptions = self.load_subscriptions()

    def load_subscription_plans(self):
        data = CSVProcessor.read_csv(self.plans_csv)
        return [SubscriptionPlan(**record) for record in data]

    def load_subscriptions(self):
        data = CSVProcessor.read_csv(self.subscriptions_csv)
        return [Subscription(**record) for record in data]

    def save_subscription_plans(self):
        data = [plan.to_dict() for plan in self.plans]
        CSVProcessor.write_csv(self.plans_csv, data, self.plan_fieldnames)

    def save_subscriptions(self):
        data = [subscription.to_dict() for subscription in self.subscriptions]
        CSVProcessor.write_csv(self.subscriptions_csv, data, self.subscription_fieldnames)

    def add_subscription_plan(self, plan_id, name, duration, price):
        plan = SubscriptionPlan(plan_id, name, duration, price)
        self.plans.append(plan)
        self.save_subscription_plans()
        return plan

    def get_all_subscription_plans(self):
        return self.plans

    def add_subscription(self, subscription_id, member_id, plan_id, start_date, end_date, status):
        subscription = Subscription(subscription_id, member_id, plan_id, start_date, end_date, status)
        self.subscriptions.append(subscription)
        self.save_subscriptions()
        return subscription

    def get_all_subscriptions(self):
        return self.subscriptions

    def update_subscription(self, subscription_id, **kwargs):
        subscription = self.get_subscription_by_id(subscription_id)
        if subscription:
            for key, value in kwargs.items():
                if hasattr(subscription, key):
                    setattr(subscription, key, value)
            self.save_subscriptions()
            return subscription
        return None

    def delete_subscription(self, subscription_id):
        subscription = self.get_subscription_by_id(subscription_id)
        if subscription:
            self.subscriptions.remove(subscription)
            self.save_subscriptions()
            return True
        return False