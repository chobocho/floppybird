import pygame


class PillarDrawEngine:
    def __init__(self, canvas, pillar):
        self.canvas = canvas
        self.pillars = pillar
        self.pillar_images = []
        self.food_images = []
        self._load_image()

    def _load_image(self):
        pillar_img_names = ['./img/tile01.png', './img/tile02.png', './img/tile03.png']
        food_img_names = ['./img/hamburg.png']
        self.pillar_images = [pygame.image.load(name) for name in pillar_img_names]
        self.food_images = [pygame.image.load(name) for name in food_img_names]

    def draw(self):
        food = self.pillars.get_food()
        pillar = self.pillars.get_pillar()
        for idx in range(0, len(pillar)):
            p = pillar[idx]
            x = p[0]
            if x > 800:
                continue
            for i in range(p[1]):
                self.canvas.blit(self.pillar_images[2], (x, i * 60))
            self.canvas.blit(self.pillar_images[0], (x, p[1] * 60))
            for i in range(p[2]):
                self.canvas.blit(self.pillar_images[2], (x, 540 - i * 60))
            self.canvas.blit(self.pillar_images[1], (x, 540 - p[2] * 60))

            if food[idx][0] > 0:
                self.canvas.blit(self.food_images[0], (food[idx][0], food[idx][1] * 60))
