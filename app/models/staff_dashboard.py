class StaffDashboard:
    def __init__(self, total_members, active_members, total_revenue, monthly_revenue, trainer_schedules, equipment_maintenance):
        self.total_members = total_members
        self.active_members = active_members
        self.total_revenue = total_revenue
        self.monthly_revenue = monthly_revenue
        self.trainer_schedules = trainer_schedules
        self.equipment_maintenance = equipment_maintenance

    def to_dict(self):
        return {
            'total_members': self.total_members,
            'active_members': self.active_members,
            'total_revenue': self.total_revenue,
            'monthly_revenue': self.monthly_revenue,
            'trainer_schedules': self.trainer_schedules,
            'equipment_maintenance': self.equipment_maintenance
        }

    def __repr__(self):
        return f"<StaffDashboard Total Members: {self.total_members}>"