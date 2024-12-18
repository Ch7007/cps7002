# member_manager.py

import json
import os
import uuid

class MemberManager:
    def __init__(self, data_file="data/members.json"):
        self.data_file = data_file
        self.members = self.load_data()

    def load_data(self):
        """Loads member data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        """Saves member data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.members, file, indent=4)

    def add_member(self, name, age, membership_type, health_info=None):
        """Adds a new member to the system."""
        member_id = str(uuid.uuid4())
        self.members[member_id] = {
            "name": name,
            "age": age,
            "membership_type": membership_type,
            "health_info": health_info or {},
            "attendance": []
        }
        self.save_data()
        return f"Member {name} added successfully with ID {member_id}."

    def update_member(self, member_id, **updates):
        """Updates member information."""
        if member_id not in self.members:
            return f"Member with ID {member_id} does not exist."
        self.members[member_id].update(updates)
        self.save_data()
        return f"Member {member_id} updated successfully."

    def delete_member(self, member_id):
        """Deletes a member from the system."""
        if member_id not in self.members:
            return f"Member with ID {member_id} does not exist."
        del self.members[member_id]
        self.save_data()
        return f"Member {member_id} deleted successfully."

    def get_member(self, member_id):
        """Retrieves a specific member's information."""
        return self.members.get(member_id, f"Member with ID {member_id} does not exist.")

    def get_all_members(self):
        """Returns all members."""
        return self.members
