import unittest
from src.services.member_profile_service import MemberProfileService
from src.models.member_profile import MemberProfile


class TestMemberProfileService(unittest.TestCase):

    def setUp(self):
        self.service = MemberProfileService(csv_file='../data/members.csv')
        self.service.add_member('M001', 'John Doe', 'john@example.com', '1234567890', 'Regular', '2024-01-01')

    def test_add_member(self):
        self.service.add_member('M003', 'Jane Smith', 'jane@example.com', '0987654321', 'Premium', '2024-02-01')
        member = self.service.get_member_by_id('M003')
        self.assertIsNotNone(member)
        self.assertEqual(member.name, 'Jane Smith')

    def test_get_member_by_id(self):
        member = self.service.get_member_by_id('M001')
        self.assertIsNotNone(member)
        self.assertEqual(member.email, 'john@example.com')

    def test_update_member(self):
        self.service.update_member('M001', name='Johnathan Doe')
        member = self.service.get_member_by_id('M001')
        self.assertEqual(member.name, 'Johnathan Doe')

    def test_delete_member(self):
        self.service.delete_member('M003')
        member = self.service.get_member_by_id('M003')
        self.assertIsNone(member)


if __name__ == '__main__':
    unittest.main()