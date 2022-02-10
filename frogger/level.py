import pygame
import grid

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
        pass

    def run(self) -> None:
        # run the entire game (level)
        self.active_sprites.update()
        
        self.game_grid.draw(self.display_surface)
        self.visible_sprites.draw(self.display_surface)
        