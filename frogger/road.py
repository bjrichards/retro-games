import pygame
import random
import settings
import vehicle


class Road(pygame.sprite.Sprite):
    def __init__(
        self,
        groups,
        y_position,
        vehicle_types,
        vehicle_groups,
        vehicle_frequency,
        vehicle_direction,
    ):
        super().__init__(groups)
        self.image = pygame.Surface((settings.ROAD_WIDTH, settings.ROAD_HEIGHT))
        self.image.fill(settings.ROAD_COLOR)
        self.rect = self.image.get_rect(
            center=(
                settings.ROAD_WIDTH / 2,
                y_position * settings.TILE_HEIGHT - (settings.TILE_HEIGHT / 2),
            )
        )

        self.time_since_last_spawn = 0
        self.next_spawn_time = random.randrange(2000, 5000, 100)

        self.vehicle_direction = vehicle_direction
        if self.vehicle_direction == 1:
            self.car_spawn_x = 0
        else:
            self.car_spawn_x = self.rect.right

        self.vehicle_groups = vehicle_groups
        self.vehicle_types = vehicle_types

    def spawn_vehicle(self, dt):
        self.time_since_last_spawn += dt
        if self.time_since_last_spawn > self.next_spawn_time:

            vehicle_type = random.choice(self.vehicle_types)
            if self.car_spawn_x == 0:
                car_spawn_x = self.car_spawn_x - (
                    getattr(settings, str(vehicle_type) + "_WIDTH") / 2
                )
            else:
                car_spawn_x = self.car_spawn_x + (
                    getattr(settings, str(vehicle_type) + "_WIDTH") / 2
                )
            vehicle.Vehicle(
                (car_spawn_x, self.rect.centery),  # type:ignore
                self.vehicle_groups,
                getattr(settings, str(vehicle_type) + "_WIDTH"),
                getattr(settings, str(vehicle_type) + "_HEIGHT"),
                getattr(settings, str(vehicle_type) + "_COLOR"),
                getattr(settings, str(vehicle_type) + "_SPEED"),
                pygame.math.Vector2(self.vehicle_direction, 0),
            )

            self.time_since_last_spawn = 0
            self.next_spawn_time = random.randrange(700, 5000, 100)

    def update(self, dt):
        self.spawn_vehicle(dt)
