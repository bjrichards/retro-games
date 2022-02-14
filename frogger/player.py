import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(
        self, pos, groups, collision_sprites, up_key, down_key, left_key, right_key
    ) -> None:
        super().__init__(groups)
        self.image: pygame.Surface = pygame.Surface(
            (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT)
        )
        self.image.fill(settings.PLAYER_COLOR)
        self.rect: pygame.rect.Rect = self.image.get_rect(center=pos)

        self.up_key: int = up_key
        self.down_key: int = down_key
        self.left_key: int = left_key
        self.right_key: int = right_key

        self.up_key_bool: bool = False
        self.down_key_bool: bool = False
        self.left_key_bool: bool = False
        self.right_key_bool: bool = False

        self.is_on_log: bool = False
        self.log_position: tuple = (0, 0)

        self.collision_sprites: pygame.sprite.Group = collision_sprites

        self.is_dead: bool = False

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = settings.TILE_HEIGHT

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        # UP/DOWN movement
        if keys[self.up_key]:
            if not self.up_key_bool:
                self.direction.y = -1
                self.up_key_bool = True
            else:
                self.direction.y = 0
        elif keys[self.down_key]:
            if not self.down_key_bool:
                self.direction.y = 1
                self.down_key_bool = True
            else:
                self.direction.y = 0
        else:
            self.up_key_bool = False
            self.down_key_bool = False
            self.direction.y = 0

        # LEFT/RIGHT movement
        if keys[self.left_key]:
            if not self.left_key_bool:
                self.direction.x = -1
                self.left_key_bool = True
            else:
                self.direction.x = 0
        elif keys[self.right_key]:
            if not self.right_key_bool:
                self.direction.x = 1
                self.right_key_bool = True
            else:
                self.direction.x = 0
        else:
            self.left_key_bool = False
            self.right_key_bool = False
            self.direction.x = 0

    def rectify_position(self) -> None:
        if self.rect.top < 0:
            self.rect.center = (
                int(self.rect.center[0]),
                int(settings.TILE_HEIGHT / 2),
            )
        elif self.rect.bottom > settings.SCREEN_HEIGHT:
            self.rect.center = (
                int(self.rect.center[0]),
                int(settings.SCREEN_HEIGHT - settings.TILE_HEIGHT / 2),
            )

        if self.rect.left < 0:
            self.rect.center = (
                int(settings.TILE_WIDTH / 2),
                int(self.rect.center[1]),
            )
        elif self.rect.right > settings.SCREEN_WIDTH:
            self.rect.center = (
                int(settings.SCREEN_WIDTH - settings.TILE_WIDTH / 2),
                int(self.rect.center[1]),
            )

        # Rectify horizontal position
        if not self.is_on_log:
            if ((self.rect.center[0] - settings.PLAYER_WIDTH / 2) % self.speed) != 0:
                take_closest = lambda num, collection: min(
                    collection, key=lambda x: abs(x - num)
                )
                self.rect.center = (
                    take_closest(
                        self.rect.center[0],
                        [
                            self.rect.center[0] - self.rect.center[0] % self.speed,
                            self.rect.center[0] + self.rect.center[0] % self.speed,
                        ],
                    )
                    + self.speed / 2,
                    self.rect.center[1],
                )

    def collisions(self):
        for sprite in self.collision_sprites.sprites():
            sprite: pygame.Sprite.sprite = sprite
            if sprite.rect.colliderect(self.rect):
                if sprite.type == "log":
                    self.is_on_log = True
                    self.log_position = sprite.rect.center

                    return
                else:
                    self.is_on_log = False
            else:
                self.is_on_log = False

    def update(self, dt):
        self.input()
        self.rect.center += self.direction * self.speed  # type: ignore
        self.collisions()
        if self.is_on_log:
            self.rect.center = self.log_position
        self.rectify_position()
