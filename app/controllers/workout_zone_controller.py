from src.services.workout_zone_service import WorkoutZoneService

class WorkoutZoneController:
    def __init__(self):
        self.service = WorkoutZoneService()

    def add_workout_zone(self, zone_id, location_id, name, equipment_list):
        return self.service.add_workout_zone(zone_id, location_id, name, equipment_list)

    def get_all_workout_zones(self):
        return self.service.get_workout_zones()

    def get_workout_zone_by_id(self, zone_id):
        return self.service.get_workout_zone_by_id(zone_id)

    def update_workout_zone(self, zone_id, location_id=None, name=None, equipment_list=None):
        return self.service.update_workout_zone(zone_id, location_id, name, equipment_list)

    def remove_workout_zone(self, zone_id):
        return self.service.remove_workout_zone(zone_id)