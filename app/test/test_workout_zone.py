import unittest
from src.services.workout_zone_service import WorkoutZoneService

class TestWorkoutZoneService(unittest.TestCase):

    def setUp(self):
        self.service = WorkoutZoneService(csv_file='../data/workout_zones.csv')
        self.service.add_workout_zone('Z001', 'L001', 'Cardio Zone', ['Treadmill', 'Bike'])

    def test_add_workout_zone(self):
        self.service.add_workout_zone('Z002', 'L001', 'Strength Zone', ['Dumbbells', 'Bench'])
        zone = self.service.get_workout_zone_by_id('Z002')
        self.assertIsNotNone(zone)
        self.assertEqual(zone.name, 'Strength Zone')

    def test_get_workout_zone_by_id(self):
        zone = self.service.get_workout_zone_by_id('Z001')
        self.assertIsNotNone(zone)
        self.assertEqual(zone.name, 'Cardio Zone')

    def test_update_workout_zone(self):
        self.service.update_workout_zone('Z001', name='Cardio and HIIT Zone')
        zone = self.service.get_workout_zone_by_id('Z001')
        self.assertEqual(zone.name, 'Cardio and HIIT Zone')

    def test_remove_workout_zone(self):
        self.service.remove_workout_zone('Z001')
        zone = self.service.get_workout_zone_by_id('Z001')
        self.assertIsNone(zone)

if __name__ == '__main__':
    unittest.main()