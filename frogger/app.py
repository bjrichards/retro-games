import pygame, sys
import settings
from level import Level


def main() -> None:
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption(settings.WINDOW_TITLE)
    clock = pygame.time.Clock()

    level = Level()

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(settings.BG_COLOR)
        level.run()

        # drawing logic
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
