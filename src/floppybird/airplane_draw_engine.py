import pygame

class AirplaneDrawEngine:
    def __init__(self, canvas, bird):
        self.canvas = canvas
        self.plane = bird
        self.planeImages = []
        self.__load_image()
        self.__tick = 0
        self.__imageIndex = 0

    def __load_image(self):
        planeImgNames = ['./img/airplain01.png', './img/airplain02.png']
        self.planeImages = [pygame.image.load(name) for name in planeImgNames]

    def draw(self):
        self.canvas.blit(self.planeImages[self.__imageIndex], (self.plane.x, self.plane.y))

    def tick(self):
        self.__tick = (self.__tick + 1) % 20
        self.__imageIndex = int(self.__tick / 10)