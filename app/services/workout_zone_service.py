from src.models.workout_zone import WorkoutZone
from src.utils.csv_processor import CSVProcessor

class WorkoutZoneService:
    def __init__(self, csv_file='data/workout_zones.csv'):
        self.csv_file = csv_file
        self.fieldnames = ['zone_id', 'location_id', 'name', 'equipment_list']
        self.workout_zones = self.load_workout_zones()

    def load_workout_zones(self):
        data = CSVProcessor.read_csv(self.csv_file)
        zones = []
        for record in data:
            record['equipment_list'] = record['equipment_list'].split(',')
            zones.append(WorkoutZone(**record))
        return zones

    def save_workout_zones(self):
        data = [zone.to_dict() for zone in self.workout_zones]
        CSVProcessor.write_csv(self.csv_file, data, self.fieldnames)

    def add_workout_zone(self, zone_id, location_id, name, equipment_list):
        workout_zone = WorkoutZone(zone_id, location_id, name, equipment_list)
        self.workout_zones.append(workout_zone)
        self.save_workout_zones()
        return workout_zone

    def get_workout_zones(self):
        return self.workout_zones

    def get_workout_zone_by_id(self, zone_id):
        for zone in self.workout_zones:
            if zone.zone_id == zone_id:
                return zone
        return None

    def update_workout_zone(self, zone_id, location_id=None, name=None, equipment_list=None):
        workout_zone = self.get_workout_zone_by_id(zone_id)
        if workout_zone:
            if location_id: workout_zone.location_id = location_id
            if name: workout_zone.name = name
            if equipment_list: workout_zone.equipment_list = equipment_list
            self.save_workout_zones()
            return workout_zone
        return None

    def remove_workout_zone(self, zone_id):
        workout_zone = self.get_workout_zone_by_id(zone_id)
        if workout_zone:
            self.workout_zones.remove(workout_zone)
            self.save_workout_zones()
            return True
        return False