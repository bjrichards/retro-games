from turtle import right
import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, up_key, down_key, left_key, right_key):
        super().__init__(groups)
        self.image = pygame.Surface((settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
        self.image.fill(settings.PLAYER_COLOR)
        self.rect = self.image.get_rect(center=pos)

        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.right_key = right_key

        self.up_key_bool: bool = False
        self.down_key_bool: bool = False
        self.left_key_bool: bool = False
        self.right_key_bool: bool = False

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = settings.TILE_HEIGHT

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[self.up_key]:
            if not self.up_key_bool:
                self.direction.y = -1  # type:ignore
                self.up_key_bool = True
            else:
                self.direction.y = 0
        elif keys[self.down_key]:
            if not self.down_key_bool:
                self.direction.y = 1  # type:ignore
                self.down_key_bool = True
            else:
                self.direction.y = 0
        else:
            self.up_key_bool = False
            self.down_key_bool = False
            self.direction.y = 0

        if keys[self.left_key]:
            if not self.left_key_bool:
                self.direction.x = -1  # type:ignore
                self.left_key_bool = True
            else:
                self.direction.x = 0
        elif keys[self.right_key]:
            if not self.right_key_bool:
                self.direction.x = 1  # type:ignore
                self.right_key_bool = True
            else:
                self.direction.x = 0
        else:
            self.left_key_bool = False
            self.right_key_bool = False
            self.direction.x = 0

    def rectify_position(self):
        if self.rect.top < 0:  # type:ignore
            self.rect.center = (  # type:ignore
                self.rect.center[0],  # type:ignore
                settings.TILE_HEIGHT / 2,
            )  # type:ignore
        elif self.rect.bottom > settings.SCREEN_HEIGHT:  # type:ignore
            self.rect.center = (  # type:ignore
                self.rect.center[0],  # type:ignore
                (settings.SCREEN_HEIGHT - settings.TILE_HEIGHT / 2),
            )  # type:ignore

        if self.rect.left < 0:  # type:ignore
            self.rect.center = (  # type:ignore
                settings.TILE_WIDTH / 2,
                self.rect.center[1],  # type:ignore
            )
        elif self.rect.right > settings.SCREEN_WIDTH:  # type:ignore
            self.rect.center = (  # type:ignore
                (settings.SCREEN_WIDTH - settings.TILE_WIDTH / 2),
                self.rect.center[1],  # type:ignore
            )  # type:ignore

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed  # type:ignore
        self.rectify_position()
