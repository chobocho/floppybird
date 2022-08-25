import random

from airplane import Airplane
from airplane_draw_engine import AirplaneDrawEngine
from draw_engine import DrawEngine
from pillar import Pillars
from pillar_draw_engine import PillarDrawEngine

PLAY_STATE = 0
RESUME_STATE = 1
GAME_OVER_STATE = 2

class PaperPlane:
    def __init__(self, canvas):
        self.score = 0
        self.prev_score = 0
        self.game_state = GAME_OVER_STATE
        self.plane = Airplane(100, 200)
        self.pillars = Pillars()

        self.drawEngine = DrawEngine(canvas, self)
        self.planeDrawEngine = AirplaneDrawEngine(canvas, self.plane)
        self.drawEngine.add(self.planeDrawEngine)
        self.pillarDrawEngine = PillarDrawEngine(canvas, self.pillars)
        self.drawEngine.add(self.pillarDrawEngine)

    def init(self):
        self.plane.init()
        self.pillars.init()
        self._init_score()

    def _init_score(self):
        self.prev_score = self.score
        self.score = 0

    def _increaseScore(self):
        self.score += 10 + random.randint(0, 5)

    def move_up(self):
        if self.isPlayState():
            self.plane.up()

    def move(self):
        if not self.isPlayState():
            return

        self._increaseScore()

        self.plane.down()
        self.planeDrawEngine.tick()

        self.pillars.move()
        self.isAlive()

    def draw(self):
        if self.isPlayState():
            self.drawEngine.draw()
        else:
            self.drawEngine.drawStart()

    def isAlive(self):
        for p in self.pillars.get():
            if self.plane.isUpCrash(p[0], p[0] + 60, 60 + p[1] * 60) or \
               self.plane.isDownCrash(p[0], p[0] + 60, 540 - p[2] * 60):
                 self.game_state = GAME_OVER_STATE
                 return False
        return True

    def isPlayState(self):
        return self.game_state == PLAY_STATE

    def get_score(self):
        return self.score

    def get_prev_score(self):
        return self.prev_score

    def start(self):
        if self.game_state == GAME_OVER_STATE:
            self.init()
        self.game_state = PLAY_STATE

    def resume(self):
        if self.isPlayState():
            self.game_state = RESUME_STATE