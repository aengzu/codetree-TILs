class User:
    def __init__(self, user_id='', level=0):
        self.user_id= user_id
        self.level = level

user1 = User()

user1.user_id = "codetree"
user1.level = 10

user2_id, level2 = tuple(input().split())

user2 = User()
user2.user_id = user2_id
user2.level = int(level2)

print(f'user {user1.user_id} lv {user1.level}')

print(f'user {user2.user_id} lv {user2.level}')