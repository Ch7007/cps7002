import unittest
from src.services.gym_location_service import GymLocationService

class TestGymLocationService(unittest.TestCase):

    def setUp(self):
        self.service = GymLocationService(csv_file='../data/gym_locations.csv')
        self.service.add_gym_location('L001', 'New York', 'Alice', ['Cardio', 'Weights'], ['Treadmill', 'Dumbbells'], ['Sauna', 'Pool'])

    def test_add_gym_location(self):
        self.service.add_gym_location('L002', 'Los Angeles', 'Bob', ['Yoga', 'Crossfit'], ['Mats', 'Kettlebells'], ['Steam Room'])
        location = self.service.get_gym_location_by_id('L002')
        self.assertIsNotNone(location)
        self.assertEqual(location.city, 'Los Angeles')

    def test_get_gym_location_by_id(self):
        location = self.service.get_gym_location_by_id('L001')
        self.assertIsNotNone(location)
        self.assertEqual(location.manager_name, 'Alice')

    def test_update_gym_location(self):
        self.service.update_gym_location('L001', city='San Francisco')
        location = self.service.get_gym_location_by_id('L001')
        self.assertEqual(location.city, 'San Francisco')

    def test_remove_gym_location(self):
        self.service.remove_gym_location('L002')
        location = self.service.get_gym_location_by_id('L002')
        self.assertIsNone(location)

if __name__ == '__main__':
    unittest.main()