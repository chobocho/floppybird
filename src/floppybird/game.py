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
    floppy_bird = PaperPlane(canvas)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    floppy_bird.move_up()
                elif event.key == pygame.K_p:
                    floppy_bird.resume()
                elif event.key == pygame.K_s:
                    floppy_bird.start()

        floppy_bird.move()
        floppy_bird.draw()
        pygame.display.update()
        fps_clock.tick(30)

if __name__ == '__main__':
    main()