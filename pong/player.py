import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, up_key, down_key):
        super().__init__(groups)
        self.image = pygame.Surface((settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
        self.image.fill(settings.PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=pos)

        self.up_key = up_key
        self.down_key = down_key

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[self.up_key]:
            self.direction.y = -1  # type:ignore
        elif keys[self.down_key]:
            self.direction.y = 1  # type:ignore
        else:
            self.direction.y = 0

    def rectify_position(self):
        if self.rect.top < 0:  # type:ignore
            self.rect.top = 0  # type:ignore
        elif self.rect.bottom > settings.SCREEN_HEIGHT:  # type:ignore
            self.rect.bottom = settings.SCREEN_HEIGHT  # type:ignore

    def update(self):
        self.input()
        self.rect.topleft += self.direction * self.speed  # type:ignore
        self.rectify_position()
