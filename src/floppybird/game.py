import pygame
from paper_plane import PaperPlane

def initGame():
    pygame.init()
    pygame.key.set_repeat(0)
    canvas = pygame.display.set_mode((800, 600))
    fps_clock = pygame.time.Clock()
    return canvas, fps_clock

def main():
    canvas, fps_clock = initGame()
    floppyBird = PaperPlane(canvas)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    floppyBird.move_up()
                elif event.key == pygame.K_p:
                    floppyBird.resume()
                elif event.key == pygame.K_s:
                    floppyBird.start()

        floppyBird.move()
        floppyBird.draw()
        pygame.display.update()
        fps_clock.tick(30)

if __name__ == '__main__':
    main()