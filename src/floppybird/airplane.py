class Airplane:
    def __init__(self, x=0, y=0, gravity=2, jump=50):
        self.x = x
        self.y = y
        self.defaultX = x
        self.defaultY = y
        self.gravity = gravity
        self.jump = jump
        self.width = 60
        self.height = 35

    def init(self):
        self.x = self.defaultX
        self.y = self.defaultY

    def down(self):
        self.y += self.gravity
        self.y =  self.y if self.y < 740 else 740
        return self.y

    def up(self):
        self.y -= self.jump
        self.y = self.y if self.y > 0 else 0
        return self.y

    def pos(self):
        return self.x, self.y

    def isUpCrash(self, x1, x2, y):
        if self.x + self.width < x1:
            return False
        if self.x > x2:
            return False
        if self.y + 10 > y:
            return False
        return True

    def isDownCrash(self, x1, x2, y):
        if self.x + self.width < x1:
            return False
        if self.x > x2:
            return False
        if self.y + self.height < y:
            return False
        return True