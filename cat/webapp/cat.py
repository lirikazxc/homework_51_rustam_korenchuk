from random import choice


class Cat:
    def __init__(self, name, age=1, fullness=40, happiness=40, sleeping=False):
        self.name = name
        self.age = age
        self.fullness = fullness
        self.happiness = happiness
        self.sleeping = sleeping

    def feed(self):
        if not self.sleeping:
            self.fullness = min(self.fullness + 15, 100)
            self.happiness = min(self.happiness + 5, 100)
            if self.fullness > 100:
                self.happiness = max(self.happiness - 30, 0)

    def play(self):
        if self.sleeping:
            self.happiness = max(self.happiness - 5, 0)
            self.sleeping = False
        else:
            if choice([True, False, False]):
                self.happiness = 0
            else:
                self.happiness = min(self.happiness + 15, 100)
            self.fullness = max(self.fullness - 10, 0)

    def sleep(self):
        self.sleeping = True
        self.happiness = min(self.happiness + 10, 100)

    def get_avatar(self):
        if self.happiness >= 70:
            return "happy_cat.png"
        elif self.happiness >= 40:
            return "neutral_cat.png"
        else:
            return "sad_cat.png"

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'fullness': self.fullness,
            'happiness': self.happiness,
            'sleeping': self.sleeping
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            age=data['age'],
            fullness=data['fullness'],
            happiness=data['happiness'],
            sleeping=data['sleeping']
        )