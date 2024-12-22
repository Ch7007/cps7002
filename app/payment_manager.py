import json
import os
from datetime import datetime, timedelta


class PaymentManager:
    """Handles payment processing, tracking, and subscription management."""

    def __init__(self, data_path="app/data/payments.json"):
        self.data_path = data_path
        self.payments = self._load_data()

    def _load_data(self):
        """Loads payment data from the JSON file."""
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as file:
                return json.load(file)
        return []

    def _save_data(self):
        """Saves payment data back to the JSON file."""
        with open(self.data_path, "w") as file:
            json.dump(self.payments, file, indent=4)

    def process_payment(self, member_id, amount, payment_date=None, duration="Monthly"):
        """
        Processes a payment for a member.

        Args:
            member_id (str): The ID of the member making the payment.
            amount (float): The payment amount.
            payment_date (str, optional): Date of payment. Defaults to today.
            duration (str, optional): Duration of subscription. Defaults to "Monthly".
                Valid values: "Monthly", "Quarterly", "Annually".

        Returns:
            dict: Payment record if successful.
        """
        if not payment_date:
            payment_date = datetime.now().strftime("%Y-%m-%d")

        # Calculate subscription expiry based on duration
        duration_mapping = {"Monthly": 30, "Quarterly": 90, "Annually": 365}
        expiry_date = (datetime.strptime(payment_date, "%Y-%m-%d") +
                       timedelta(days=duration_mapping.get(duration, 30))).strftime("%Y-%m-%d")

        payment_record = {
            "member_id": member_id,
            "amount": amount,
            "payment_date": payment_date,
            "expiry_date": expiry_date,
            "duration": duration
        }

        self.payments.append(payment_record)
        self._save_data()
        return payment_record

    def get_payment_history(self, member_id):
        """
        Retrieves the payment history for a specific member.

        Args:
            member_id (str): The ID of the member.

        Returns:
            list: List of payment records for the member.
        """
        return [payment for payment in self.payments if payment["member_id"] == member_id]

    def check_membership_status(self, member_id):
        """
        Checks if a member's subscription is active.

        Args:
            member_id (str): The ID of the member.

        Returns:
            bool: True if membership is active, False otherwise.
        """
        payment_history = self.get_payment_history(member_id)
        if not payment_history:
            return False

        # Check the latest payment expiry date
        latest_payment = max(payment_history, key=lambda x: x["expiry_date"])
        current_date = datetime.now().strftime("%Y-%m-%d")
        return latest_payment["expiry_date"] >= current_date

    def get_overdue_members(self):
        """
        Identifies members with overdue payments.

        Returns:
            list: List of member IDs with overdue payments.
        """
        overdue_members = []
        current_date = datetime.now().strftime("%Y-%m-%d")

        for payment in self.payments:
            if payment["expiry_date"] < current_date and payment["member_id"] not in overdue_members:
                overdue_members.append(payment["member_id"])

        return overdue_members

    def generate_revenue_report(self):
        """
        Generates a revenue report based on payments.

        Returns:
            dict: Total revenue and breakdown by duration.
        """
        revenue = {"Total": 0, "Monthly": 0, "Quarterly": 0, "Annually": 0}

        for payment in self.payments:
            revenue["Total"] += payment["amount"]
            revenue[payment["duration"]] += payment["amount"]

        return revenue
