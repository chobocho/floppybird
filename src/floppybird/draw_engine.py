import pygame


class DrawEngine:
    def __init__(self, canvas, parent):
        self.canvas = canvas
        self._load_background()
        self._init_font()
        self.engine_list = []
        self.parent = parent

    def _init_font(self):
        self.sysfont = pygame.font.SysFont(None, 30)
        self.bigfont = pygame.font.SysFont(None, 72)

    def _load_background(self):
        self.background = pygame.image.load('./img/background01.jpg')
        self.start_image = pygame.image.load('./img/start.png')

    def _draw_background(self):
        self.canvas.blit(self.background, (0, 0))

    def _draw_score(self):
        socre_image = self.sysfont.render(f"{self.parent.get_score()}".zfill(9), True, (255, 255, 255))
        self.canvas.blit(socre_image, (680, 10))

    def _draw_message(self):
        font_color = (200, 200, 200)
        pause_image = self.sysfont.render("Press P to PAUSE", True, font_color)
        self.canvas.blit(pause_image, (600, 560))

    def add(self, engine):
        self.engine_list.append(engine)

    def draw(self):
        self._draw_background()
        for engine in self.engine_list:
            engine.draw()
        self._draw_message()
        self._draw_score()

    def draw_start_button(self):
        self.draw()
        self.canvas.blit(self.start_image, (250, 100))
        socre_image = self.bigfont.render(f"{self.parent.get_prev_score()}".zfill(9), True, (0, 0, 0))
        pygame.draw.rect(self.canvas, (255, 201, 14), (250, 300, 300, 100))
        self.canvas.blit(socre_image, (270, 330))
