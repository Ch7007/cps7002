from src.services.staff_dashboard_service import StaffDashboardService

class StaffDashboardController:
    def __init__(self):
        self.service = StaffDashboardService()

    def create_membership_growth(self, month, new_members, cancellations):
        return self.service.add_membership_growth(month, new_members, cancellations)

    def create_revenue_trend(self, month, revenue):
        return self.service.add_revenue_trend(month, revenue)

    def create_trainer_schedule(self, trainer_id, trainer_name, schedule):
        return self.service.add_trainer_schedule(trainer_id, trainer_name, schedule)

    def create_equipment_maintenance(self, equipment_id, equipment_name, maintenance_date, status):
        return self.service.add_equipment_maintenance(equipment_id, equipment_name, maintenance_date, status)

    def get_membership_growth(self):
        return self.service.get_membership_growth()

    def get_revenue_trends(self):
        return self.service.get_revenue_trends()

    def get_trainer_schedules(self):
        return self.service.get_trainer_schedules()

    def get_equipment_maintenance(self):
        return self.service.get_equipment_maintenance()