import pygame


class PillarDrawEngine:
    def __init__(self, canvas, pillar):
        self.canvas = canvas
        self.pillars = pillar
        self.pillarImages = []
        self.__load_image()

    def __load_image(self):
        pillarImgNames = ['./img/tile01.png', './img/tile02.png', './img/tile03.png']
        self.pillarImages = [ pygame.image.load(name) for name in pillarImgNames]

    def draw(self):
        for p in self.pillars.get():
            x = p[0]
            if (x > 800):
                continue
            for i in range(p[1]):
                self.canvas.blit(self.pillarImages[2], (x, i * 60))
            self.canvas.blit(self.pillarImages[0], (x, p[1] * 60))
            for i in range(p[2]):
                self.canvas.blit(self.pillarImages[2], (x, 540 - i * 60))
            self.canvas.blit(self.pillarImages[1], (x, 540 - p[2] * 60))