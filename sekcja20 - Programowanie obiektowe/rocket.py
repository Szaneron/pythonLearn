from random import randint
from math import sqrt


class Rocket:
    nextId = 1

    def __init__(self, speed=1):
        self.altitude = 0
        self.speed = speed
        self.x = 0
        self.id = Rocket.nextId
        Rocket.nextId += 1

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta o id: " + str(self.id) + " jest aktualnie na wysyokosci: " + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].move_up()

        for rocket in self.rockets:
            print(rocket, rocket.id)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1, rocket2):
        ac = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ac + bc)

    def __len__(self):
        return len(self.rockets)
