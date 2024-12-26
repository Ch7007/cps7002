from src.services.gym_location_service import GymLocationService

class GymLocationController:
    def __init__(self):
        self.service = GymLocationService()

    def add_gym_location(self, location_id, city, manager_name, workout_zones, equipment, amenities):
        return self.service.add_gym_location(location_id, city, manager_name, workout_zones, equipment, amenities)

    def get_all_gym_locations(self):
        return self.service.get_gym_locations()

    def get_gym_location_by_id(self, location_id):
        return self.service.get_gym_location_by_id(location_id)

    def update_gym_location(self, location_id, city=None, manager_name=None, workout_zones=None, equipment=None, amenities=None):
        return self.service.update_gym_location(location_id, city, manager_name, workout_zones, equipment, amenities)

    def remove_gym_location(self, location_id):
        return self.service.remove_gym_location(location_id)