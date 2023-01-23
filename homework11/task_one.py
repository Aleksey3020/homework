import random
AVAILABLE_NAMES = [
    'John', 'Jane', 'Mary', 'David', 'Alex',
    'Max', 'Nick', 'Anastasia', 'Leo']
AVAILABLE_COLORS = ['blue', 'green', 'brown', 'grey', 'black']


class User:
    def __init__(self, name, nickname, age, eyes_color):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.eyes_color = eyes_color

    @property
    def info(self):
        return {
            'Name': self.name, 'Nickname': self.nickname,
            'Age': self.age, 'Eyes_color': self.eyes_color}

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age


def users_generator(number):
    first_user = 1
    while first_user <= number:
        name = random.choice(AVAILABLE_NAMES)
        num = random.sample(range(9), 5)
        nickname = name + (''.join(map(str, num)))
        age = random.choice(range(100))
        eyes_color = random.choice(AVAILABLE_COLORS)
        user = User(name, nickname, age, eyes_color)
        yield user
        first_user += 1


gen = users_generator(1000000)
for user in gen:
    print(user.info)