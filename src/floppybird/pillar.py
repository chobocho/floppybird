import random


class Pillars:
    def __init__(self):
        self._initPillar()

    def _initPillar(self):
        self.pillars = []
        self.foods = [[0, 0]]
        self.pillars.append([200, 0, 0])
        for i in range(4):
            down = random.randint(0, 5)
            top = random.randint(0, 5 - down)
            self.pillars.append([400 + i * 200, top, down])
            if i < 3:
                self.foods.append([0, top+int((9-top-down)/2)])
            else:
                self.foods.append([400 + i * 200, top + int((9 - top - down) / 2)])

    def init(self):
        self._initPillar()

    def move(self, speed=1):
        for p in self.pillars:
            p[0] -= speed

        for f in self.foods:
            f[0] -=speed

        if self.pillars[0][0] < -60:
            self.make_new_pillar(speed)

    def make_new_pillar(self, speed):
        del self.pillars[0]
        speed = speed * 2 if speed > 5 else speed
        gap = 100 if speed * 2 > 100 else int(speed * 2)
        px = self.pillars[3][0] + 250 + random.randint(gap, 120 + gap)
        block = (5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
        block_count = block[int(speed)] if speed < 15 else 3
        down = random.randint(0, block_count)
        top = random.randint(0, block_count - down)
        self.pillars.append([px, top, down])

        del self.foods[0]
        food_y = top+int((9-top-down)/2)
        food_x = px if random.randint(0, 10) > 6 else -1
        self.foods.append([food_x, food_y])

    def get_pillar(self):
        return self.pillars

    def get_food(self):
        return self.foods