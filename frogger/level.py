import pygame
import settings
import grid, player


class Level:
    def __init__(self) -> None:

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.active_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.game_grid = grid.Grid()
        self.setup_level()

    def setup_level(self) -> None:
        player.Player(
            (
                ((settings.GRID_WIDTH_COUNT // 2) * settings.TILE_WIDTH)
                - settings.TILE_WIDTH / 2,
                (settings.GRID_HEIGHT_COUNT) * settings.TILE_HEIGHT
                - settings.TILE_HEIGHT / 2,
            ),
            [self.active_sprites, self.visible_sprites],
            up_key=pygame.K_UP,
            down_key=pygame.K_DOWN,
            left_key=pygame.K_LEFT,
            right_key=pygame.K_RIGHT,
        )

    def run(self) -> None:
        # run the entire game (level)
        self.active_sprites.update()

        self.game_grid.draw(self.display_surface)
        self.visible_sprites.draw(self.display_surface)
