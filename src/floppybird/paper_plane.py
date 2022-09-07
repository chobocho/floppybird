import random

from airplane import Airplane
from airplane_draw_engine import AirplaneDrawEngine
from draw_engine import DrawEngine
from pillar import Pillars
from pillar_draw_engine import PillarDrawEngine
from util import fileutil

PLAY_STATE = 0
RESUME_STATE = 1
GAME_OVER_STATE = 2


class PaperPlane:
    def __init__(self, canvas, high_score=0):
        self.reference_score = 20000
        self.start_score = 19000
        self.prev_high_score = high_score
        self.score = 0
        self.high_score = high_score
        self.game_state = GAME_OVER_STATE
        self.plane = Airplane(100, 200)
        self.pillars = Pillars()
        self.drawEngine = DrawEngine(canvas, self)
        self.pillarDrawEngine = PillarDrawEngine(canvas, self.pillars)
        self.drawEngine.add(self.pillarDrawEngine)
        self.planeDrawEngine = AirplaneDrawEngine(canvas, self.plane)
        self.drawEngine.add(self.planeDrawEngine)
        self.tick_count = 0
        self.space_count = 0

    def init(self):
        self.tick_count = 0
        self.space_count = 0
        self.plane.init()
        self.pillars.init()
        self._init_score()

    def _init_score(self):
        self.high_score = self.high_score if self.high_score > self.score else self.score
        self.score = 1

    def _increaseScore(self):
        self.score += 10 + random.randint(0, 5)

    def _add_score(self, value):
        self.score += value

    def move_up(self):
        if self.isPlayState():
            score = self.score + self.start_score
            acceleration = (score - self.reference_score) / 5000 if score > self.reference_score else 0
            gravity = (1, 1, 1, 1, 1, 1, 1, 1, 1.2, 1.5, 1.8, 2, 2.5, 2.5, 3)
            acceleration *= gravity[int(score/10000)] if score < 150000 else gravity[-1]
            self.plane.up(acceleration)

    def move(self):
        if not self.isPlayState():
            return
        self._increaseScore()
        self.tick_count += 1
        score = self.score + self.start_score
        acceleration = (score - self.reference_score) / 10000 if score > self.reference_score else 0
        self.plane.down(acceleration)
        self.planeDrawEngine.tick()

        self.pillars.move(1 + acceleration)
        self.check_eat_food()
        if not self.is_alive():
            self.game_state = GAME_OVER_STATE
            if self.prev_high_score < self.high_score:
                self.prev_high_score = self.high_score
                score_data = {'high_score': self.high_score}
                fileutil.save_as_json(score_data, "./floppybird.cfg")
        else:
            self.high_score = self.high_score if self.high_score > self.score else self.score

        if self.tick_count > 30:
            self.plane.decrease_energy(1)
            self.tick_count = 0

    def draw(self) -> None:
        if self.isPlayState():
            self.drawEngine.draw(self.score)
        else:
            if self.prev_high_score < self.high_score:
                self.prev_high_score = self.high_score
                score_data = {'high_score': self.high_score}
                fileutil.save_as_json(score_data, "./floppybird.cfg")
            self.drawEngine.draw_start_button()

    def is_alive(self) -> bool:
        if self.plane.get_energy() == 0:
            return False
        for p in self.pillars.get_pillar():
            if self.plane.is_up_crash(p[0], p[0] + 60, 60 + p[1] * 60) or \
                 self.plane.is_down_crash(p[0], p[0] + 60, 540 - p[2] * 60):
                return False
        return True

    def check_eat_food(self):
        for food in self.pillars.get_food():
            if self.plane.is_up_crash(food[0], food[0] + 60, food[1] * 60) or \
                 self.plane.is_down_crash(food[0], food[0] + 60, food[1] * 60 + 60):
                    self.plane.increase_energy(48)
                    food[0] = -1
                    self._add_score(2020)

    def isPlayState(self):
        return self.game_state == PLAY_STATE

    def get_score(self):
        return self.score

    def get_high_score(self):
        return self.high_score

    def start(self):
        if self.game_state == GAME_OVER_STATE:
            self.init()
        self.game_state = PLAY_STATE

    def resume(self):
        if self.isPlayState():
            self.game_state = RESUME_STATE
    def get_energy(self):
        return self.plane.get_energy()

    def use_energy(self):
        if self.game_state == PLAY_STATE:
            self.space_count += 1
            if self.space_count > 2:
                self.plane.decrease_energy(1)
                self.space_count = 0
