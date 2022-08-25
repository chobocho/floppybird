import pygame


class AirplaneDrawEngine:
    def __init__(self, canvas, bird):
        self.canvas = canvas
        self.plane = bird
        self.plane_images = []
        self._load_image()
        self.tick_count = 0
        self.image_index = 0

    def _load_image(self):
        plane_img_names = ['./img/airplain01.png', './img/airplain02.png']
        self.plane_images = [pygame.image.load(name) for name in plane_img_names]

    def draw(self):
        self.canvas.blit(self.plane_images[self.image_index], (self.plane.x, self.plane.y))

    def tick(self):
        self.tick_count = (self.tick_count + 1) % 20
        self.image_index = int(self.tick_count / 10)
