from operator import attrgetter
from common.seperator import delimiter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)


# Example
users = [User(23), User(3), User(99)]
print(users)
delimiter()

# Sort it by user-id, ascending

print("Sort it by user-id, ascending")
print(sorted(users, key=attrgetter("user_id")))
delimiter()

# Sort it by user-id, descending
print("Sort it by user-id, descending")
print(sorted(users, key=attrgetter("user_id"), reverse=True))
