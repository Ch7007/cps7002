from src.utils.csv_processor import CSVProcessor

class StaffDashboardService:
    def __init__(self, members_csv='data/members.csv', payments_csv='data/payments.csv', trainer_schedules_csv='data/trainer_schedules.csv', equipment_maintenance_csv='data/equipment_maintenance.csv'):
        self.members_csv = members_csv
        self.payments_csv = payments_csv
        self.trainer_schedules_csv = trainer_schedules_csv
        self.equipment_maintenance_csv = equipment_maintenance_csv

    def get_membership_growth(self):
        data = CSVProcessor.read_csv(self.members_csv)
        growth = {}
        for record in data:
            month = record['join_date'].split('-')[1]
            if month not in growth:
                growth[month] = {'new_members': 0, 'cancellations': 0}
            growth[month]['new_members'] += 1
        return growth

    def get_revenue_trends(self):
        data = CSVProcessor.read_csv(self.payments_csv)
        revenue = {}
        for record in data:
            month = record['date'].split('-')[1]
            if month not in revenue:
                revenue[month] = 0
            revenue[month] += float(record['amount'])
        return revenue

    def get_trainer_schedules(self):
        data = CSVProcessor.read_csv(self.trainer_schedules_csv)
        schedules = {}
        for record in data:
            trainer_id = record['trainer_id']
            if trainer_id not in schedules:
                schedules[trainer_id] = []
            schedules[trainer_id].append(record)
        return schedules

    def get_equipment_maintenance(self):
        data = CSVProcessor.read_csv(self.equipment_maintenance_csv)
        maintenance = {}
        for record in data:
            equipment_id = record['equipment_id']
            if equipment_id not in maintenance:
                maintenance[equipment_id] = []
            maintenance[equipment_id].append(record)
        return maintenance