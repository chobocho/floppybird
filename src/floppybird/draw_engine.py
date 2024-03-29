import pygame


class DrawEngine:
    def __init__(self, canvas, parent):
        self.canvas = canvas
        self._load_background()
        self._init_font()
        self.engine_list = []
        self.parent = parent
        self.background_image = 0


    def _init_font(self):
        self.sysfont = pygame.font.SysFont(None, 30)
        self.bigfont = pygame.font.SysFont(None, 72)

    def _load_background(self):
        self.background = [0] * 6
        self.background[0] = pygame.image.load('./img/background01.jpg')
        self.background[1] = pygame.image.load('./img/background02.jpg')
        self.background[2] = pygame.image.load('./img/background03.png')
        self.background[3] = pygame.image.load('./img/background04.png')
        self.background[4] = pygame.image.load('./img/background05.png')
        self.background[5] = pygame.image.load('./img/background06.png')
        self.start_image = pygame.image.load('./img/start.png')
        self.energy_image = pygame.image.load('./img/bar.png')
        self.energy_image = pygame.transform.scale(self.energy_image, (204, 30))

    def _draw_background(self, score=0):
        if score > 0:
            image = (0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5)
            self.background_image = image[int(score/10000)] if score < 120000 else image[-1]
        self.canvas.blit(self.background[self.background_image], (0, 0))

    def _draw_score(self):
        score_image = self.sysfont.render(f"{self.parent.get_score()}".zfill(9), True, (255, 255, 255))
        self.canvas.blit(score_image, (680, 10))

    def _draw_energy(self):
        energy = self.parent.plane.get_energy() * 2
        startX = 790 - 204
        startY = 10
        height = 30
        self.canvas.blit(self.energy_image, (startX, startY))
        pygame.draw.rect(self.canvas, (0, 0, 0), (startX + 2 + 200 - (200 - energy), startY + 2, 200-energy, height-4))

    def _draw_message(self):
        font_color = (200, 200, 200)
        pause_image = self.sysfont.render("Press P to PAUSE", True, font_color)
        self.canvas.blit(pause_image, (600, 560))

    def add(self, engine):
        self.engine_list.append(engine)

    def draw(self, score=0):
        self._draw_background(score)
        for engine in self.engine_list:
            engine.draw()
        self._draw_message()
        self._draw_energy()
        self._draw_score()

    def draw_start_button(self):
        self.draw()
        self.canvas.blit(self.start_image, (250, 100))
        score_image = self.bigfont.render(f"{self.parent.get_high_score()}".zfill(9), True, (0, 0, 0))
        pygame.draw.rect(self.canvas, (255, 201, 14), (250, 300, 300, 100))
        self.canvas.blit(score_image, (270, 330))
