import pygame
import random

def grid(window):
    for v in range(1,20):
        v *= 32
        pygame.draw.line(window,"black", (v,0) , (v,512))

    for h in range(1,16):
        h *= 32
        pygame.draw.line(window,"black", (0,h), (640,h))


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))


        mole_pos = (0,0)

        clock = pygame.time.Clock()
        running = True


        while running:
            screen.fill("light green")
            grid(screen)

            mole_dis_x = mole_pos[0] * 32
            mole_dis_y = mole_pos[1] * 32

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_dis_x, mole_dis_y)))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos_x = event.pos[0] // 32
                    mouse_pos_y = event.pos[1] // 32

                    if mouse_pos_x == mole_pos[0] and mouse_pos_y == mole_pos[1]:
                        new_x = random.randrange(0, 19)
                        new_y = random.randrange(0, 15)
                        mole_pos = (new_x, new_y)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
