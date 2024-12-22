class WorkoutZone:
    def __init__(self, zone_id, location_id, name, equipment_list):
        self.zone_id = zone_id
        self.location_id = location_id
        self.name = name
        self.equipment_list = equipment_list

    def to_dict(self):
        return {
            'zone_id': self.zone_id,
            'location_id': self.location_id,
            'name': self.name,
            'equipment_list': ','.join(self.equipment_list)
        }

    def __repr__(self):
        return f"<WorkoutZone {self.zone_id} - {self.name}>"