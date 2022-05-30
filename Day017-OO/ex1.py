class User:
    def __init__(self, user_id=None, name=None):
        self.name = name
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def fallow(self, user):
        self.following += 1
        user.followers += 1


user_01 = User('001', 'Lucas')

print(user_01.name)

user_02 = User()
user_02.user_id = '002'
user_02.name = 'Angela'

user_01.fallow(user_02)
print(user_01.followers)
print(user_01.following)
print(user_02.followers)
print(user_02.following)
