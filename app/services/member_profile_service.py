from src.models.member_profile import MemberProfile
from src.utils.csv_processor import CSVProcessor

class MemberProfileService:
    def __init__(self, csv_file='data/members.csv'):
        self.csv_file = csv_file
        self.fieldnames = ['member_id', 'name', 'email', 'phone', 'membership_type', 'join_date']
        self.members = self.load_members()

    def load_members(self):
        data = CSVProcessor.read_csv(self.csv_file)
        return [MemberProfile(**record) for record in data]

    def save_members(self):
        data = [member.to_dict() for member in self.members]
        CSVProcessor.write_csv(self.csv_file, data, self.fieldnames)

    def add_member(self, member_id, name, email, phone, membership_type, join_date):
        member = MemberProfile(member_id, name, email, phone, membership_type, join_date)
        self.members.append(member)
        self.save_members()
        return member

    def get_all_members(self):
        return self.members

    def get_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def update_member(self, member_id, **kwargs):
        member = self.get_member_by_id(member_id)
        if member:
            for key, value in kwargs.items():
                if hasattr(member, key):
                    setattr(member, key, value)
            self.save_members()
            return member
        return None

    def delete_member(self, member_id):
        member = self.get_member_by_id(member_id)
        if member:
            self.members.remove(member)
            self.save_members()
            return True
        return False