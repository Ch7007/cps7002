from src.models.gym_location import GymLocation
from src.utils.csv_processor import CSVProcessor

class GymLocationService:
    def __init__(self, csv_file='data/gym_locations.csv'):
        self.csv_file = csv_file
        self.fieldnames = ['location_id', 'city', 'manager_name', 'workout_zones', 'equipment', 'amenities']
        self.gym_locations = self.load_gym_locations()

    def load_gym_locations(self):
        data = CSVProcessor.read_csv(self.csv_file)
        locations = []
        for record in data:
            record['workout_zones'] = record['workout_zones'].split(',')
            record['equipment'] = record['equipment'].split(',')
            record['amenities'] = record['amenities'].split(',')
            locations.append(GymLocation(**record))
        return locations

    def save_gym_locations(self):
        data = [location.to_dict() for location in self.gym_locations]
        CSVProcessor.write_csv(self.csv_file, data, self.fieldnames)

    def add_gym_location(self, location_id, city, manager_name, workout_zones, equipment, amenities):
        gym_location = GymLocation(location_id, city, manager_name, workout_zones, equipment, amenities)
        self.gym_locations.append(gym_location)
        self.save_gym_locations()
        return gym_location

    def get_gym_locations(self):
        return self.gym_locations

    def get_gym_location_by_id(self, location_id):
        for location in self.gym_locations:
            if location.location_id == location_id:
                return location
        return None

    def update_gym_location(self, location_id, city=None, manager_name=None, workout_zones=None, equipment=None, amenities=None):
        gym_location = self.get_gym_location_by_id(location_id)
        if gym_location:
            if city: gym_location.city = city
            if manager_name: gym_location.manager_name = manager_name
            if workout_zones: gym_location.workout_zones = workout_zones
            if equipment: gym_location.equipment = equipment
            if amenities: gym_location.amenities = amenities
            self.save_gym_locations()
            return gym_location
        return None

    def remove_gym_location(self, location_id):
        gym_location = self.get_gym_location_by_id(location_id)
        if gym_location:
            self.gym_locations.remove(gym_location)
            self.save_gym_locations()
            return True
        return False