from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    User('John', 43),
    User('shaun', 5),
    User('Luna', 13),
    User('Bobby', 53),
    User('Sunny', 33),
    User('kirk', 23),
]

for user in users:
    print(user)

print('----------------xx------------')

for user in sorted(users, key=attrgetter('name')):
    print(user)

print('----------------xx------------')

for user in sorted(users, key=attrgetter('user_id')):
    print(user)

