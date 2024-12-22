class MemberProfile:
    def __init__(self, member_id, name, email, phone, membership_type, join_date):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type
        self.join_date = join_date

    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'membership_type': self.membership_type,
            'join_date': self.join_date
        }

    def __repr__(self):
        return f"<MemberProfile {self.member_id} - {self.name}>"