import pygame
import settings


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((settings.TILE_WIDTH, settings.TILE_HEIGHT))
        self.image.fill(
            settings.TILE_OUTLINE_COLOR,
            rect=pygame.Rect(0, 0, settings.TILE_HEIGHT - 1, settings.TILE_WIDTH - 1),
        )
        self.rect = self.image.get_rect(topleft=pos)
