import pygame

class DrawEngine:
    def __init__(self, canvas, parent):
        self.canvas = canvas
        self.__load_background()
        self.__init_font()
        self.engineList = []
        self.parent = parent

    def __init_font(self):
        self.sysfont = pygame.font.SysFont(None, 30)
        self.bigfont = pygame.font.SysFont(None, 72)

    def __load_background(self):
        self.background = pygame.image.load('./img/background01.jpg')
        self.startImage = pygame.image.load('./img/start.png')

    def __drawBackground(self):
        self.canvas.blit(self.background, (0, 0))

    def __drawScore(self):
        socreImage = self.sysfont.render(f"{self.parent.score()}".zfill(9), True, (255, 255, 255))
        self.canvas.blit(socreImage, (680, 10))

    def __drawMessage(self):
        fontColor = (200, 200, 200)
        pauseImage = self.sysfont.render("Press P to PAUSE", True, fontColor)
        self.canvas.blit(pauseImage, (600, 560))

    def add(self, engine):
        self.engineList.append(engine)

    def draw(self):
        self.__drawBackground()
        for engine in self.engineList:
            engine.draw()
        self.__drawMessage()
        self.__drawScore()

    def drawStart(self):
        self.draw()
        self.canvas.blit(self.startImage, (250, 100))
        socreImage = self.bigfont.render(f"{self.parent.prevScore()}".zfill(9), True, (0, 0, 0))
        pygame.draw.rect(self.canvas, (255, 201, 14), (250, 300, 300, 100))
        self.canvas.blit(socreImage, (270, 330))