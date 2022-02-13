import pygame
import random
import settings
import log


class River(pygame.sprite.Sprite):
    def __init__(
        self,
        groups,
        y_position,
        log_types,
        log_groups,
        log_frequency,
        log_direction,
    ):
        super().__init__(groups)
        self.image = pygame.Surface((settings.RIVER_WIDTH, settings.RIVER_HEIGHT))
        self.image.fill(settings.RIVER_COLOR)
        self.rect = self.image.get_rect(
            center=(
                settings.RIVER_WIDTH / 2,
                y_position * settings.TILE_HEIGHT - (settings.TILE_HEIGHT / 2),
            )
        )

        self.log_types = log_types
        self.log_groups = log_groups
        self.log_frequency = log_frequency
        self.log_direction = log_direction

        if self.log_direction == 1:
            self.log_spawn_x = 0
        else:
            self.log_spawn_x = self.rect.right

        self.time_since_last_spawn = 0
        self.next_spawn_time = random.randrange(2000, 5000, 100)

    def spawn_log(self, dt):
        self.time_since_last_spawn += dt
        if self.time_since_last_spawn > self.next_spawn_time:
            log_type = random.choice(self.log_types)
            if self.log_spawn_x == 0:
                log_spawn_x = self.log_spawn_x - (
                    getattr(settings, str(log_type) + "_WIDTH") / 2
                )
            else:
                log_spawn_x = self.log_spawn_x + (
                    getattr(settings, str(log_type) + "_WIDTH") / 2
                )
            log.Log(
                (log_spawn_x, self.rect.centery),  # type:ignore
                self.log_groups,
                getattr(settings, str(log_type) + "_WIDTH"),
                getattr(settings, str(log_type) + "_HEIGHT"),
                getattr(settings, str(log_type) + "_COLOR"),
                getattr(settings, str(log_type) + "_SPEED"),
                pygame.math.Vector2(self.log_direction, 0),
            )

            self.time_since_last_spawn = 0
            self.next_spawn_time = random.randrange(700, 5000, 100)

    def update(self, dt):
        self.spawn_log(dt)
