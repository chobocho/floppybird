class Airplane:
    def __init__(self, x=0, y=0, gravity=3, jump=60, bottom=600):
        self.x = x
        self.y = y
        self.defaultX = x
        self.defaultY = y
        self.gravity = gravity
        self.jump = jump
        self.core_rect = (18, 14, 48, 32)
        self.bottom = bottom
        self.energy = 100

    def init(self):
        self.x = self.defaultX
        self.y = self.defaultY
        self.energy = 100

    def down(self, acceleration):
        self.y += self.gravity + acceleration
        self.y = self.y if self.y < self.bottom else self.bottom
        return self.y

    def up(self, accceleration):
        self.y -= self.jump + accceleration
        self.y = self.y if self.y > 0 else 0
        return self.y

    def pos(self):
        return self.x, self.y

    def is_up_crash(self, x1, x2, y):
        if self.y < 0:
            return True
        if self.x + self.core_rect[2] < x1:
            return False
        if self.x + self.core_rect[0] > x2:
            return False
        if self.y + self.core_rect[1] > y:
            return False
        return True

    def is_down_crash(self, x1, x2, y):
        if self.y + self.core_rect[3] > self.bottom:
            return True
        if self.x + self.core_rect[2] < x1:
            return False
        if self.x + self.core_rect[0] > x2:
            return False
        if self.y + self.core_rect[3] < y:
            return False
        return True

    def increase_energy(self, val):
        self.energy += val
        self.energy = self.energy if self.energy < 100 else 100

    def decrease_energy(self, val):
        self.energy -= val
        self.energy = self.energy if self.energy > 0 else 0

    def get_energy(self):
        return self.energy
