from src.services.member_profile_service import MemberProfileService

class MemberProfileController:
    def __init__(self):
        self.service = MemberProfileService()

    def add_member(self, member_id, name, email, membership_type, join_date):
        return self.service.add_member(member_id, name, email, membership_type, join_date)

    def get_all_members(self):
        return self.service.get_all_members()

    def get_member_by_id(self, member_id):
        return self.service.get_member_by_id(member_id)

    def update_member(self, member_id, **kwargs):
        return self.service.update_member(member_id, **kwargs)

    def delete_member(self, member_id):
        return self.service.delete_member(member_id)