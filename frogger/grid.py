import pygame
import settings
import tile


class Grid:
    def __init__(self) -> None:
        # sprite group setup
        self.tiles = pygame.sprite.Group()

        self.setup_level()

    def setup_level(self) -> None:
        for i in range(0, settings.GRID_HEIGHT_COUNT):
            for j in range(0, settings.GRID_WIDTH_COUNT):
                tile.Tile(
                    (i * settings.TILE_HEIGHT, j * settings.TILE_WIDTH), self.tiles
                )

    def draw(self, display_surface) -> None:
        self.tiles.draw(display_surface)
