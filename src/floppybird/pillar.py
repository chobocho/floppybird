import random


class Pillars():
    def __init__(self):
        self.__initPillar()

    def __initPillar(self):
        self.pillars = []
        self.pillars.append([200, 0, 0])
        for i in range(4):
            down = random.randint(0, 5)
            top = random.randint(0, 5 - down)
            self.pillars.append([400 + i * 200, top, down])

    def init(self):
        self.__initPillar()

    def move(self):
        for p in self.pillars:
            p[0] = p[0] - 1

        if self.pillars[0][0] < -60:
            del self.pillars[0]
            px = self.pillars[3][0] + 180 + random.randint(0, 30)
            down = random.randint(0, 5)
            top = random.randint(0, 5 - down)
            self.pillars.append([px, top, down])

    def get(self):
        return self.pillars