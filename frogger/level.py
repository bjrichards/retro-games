import pygame
import settings
import grid, player, road, river


class Level:
    def __init__(self) -> None:

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.active_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()
        self.vehicle_sprites = pygame.sprite.Group()
        self.transport_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.player_sprites = pygame.sprite.Group()

        self.game_grid = grid.Grid()
        self.setup_level()

    def setup_level(self) -> None:
        river.River(
            [self.background_sprites, self.active_sprites],
            2,
            ["LOG_1"],
            [self.active_sprites, self.transport_sprites, self.collision_sprites],
            1,
            1,
        )
        river.River(
            [self.background_sprites, self.active_sprites],
            3,
            ["LOG_1"],
            [self.active_sprites, self.transport_sprites, self.collision_sprites],
            1,
            -1,
        )

        road.Road(
            [self.background_sprites, self.active_sprites],
            6,
            ["CAR_1"],
            [self.active_sprites, self.vehicle_sprites, self.collision_sprites],
            1,
            1,
        )
        road.Road(
            [self.background_sprites, self.active_sprites],
            7,
            ["CAR_1"],
            [self.active_sprites, self.vehicle_sprites, self.collision_sprites],
            1,
            -1,
        )
        road.Road(
            [self.background_sprites, self.active_sprites],
            8,
            ["CAR_1"],
            [self.active_sprites, self.vehicle_sprites, self.collision_sprites],
            1,
            1,
        )

        player.Player(
            (
                ((settings.GRID_WIDTH_COUNT // 2) * settings.TILE_WIDTH)
                - settings.TILE_WIDTH / 2,
                (settings.GRID_HEIGHT_COUNT) * settings.TILE_HEIGHT
                - settings.TILE_HEIGHT / 2,
            ),
            [self.player_sprites, self.active_sprites],
            self.collision_sprites,
            up_key=pygame.K_UP,
            down_key=pygame.K_DOWN,
            left_key=pygame.K_LEFT,
            right_key=pygame.K_RIGHT,
        )

    def run(self, dt) -> None:

        # run the entire game (level)
        self.active_sprites.update(dt)

        self.game_grid.draw(self.display_surface)
        self.background_sprites.draw(self.display_surface)
        self.transport_sprites.draw(self.display_surface)
        self.player_sprites.draw(self.display_surface)
        self.vehicle_sprites.draw(self.display_surface)
