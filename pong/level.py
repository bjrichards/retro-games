import pygame
import settings
import player
import ball
import ui


class Level:
    def __init__(self):

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.active_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # ui
        self.ui = ui.UI(self.display_surface)

        self.setup_level()

    def setup_level(self):
        # Player 1
        player.Player(
            (68, (settings.SCREEN_HEIGHT / 2) - settings.PLAYER_HEIGHT / 2),
            [self.visible_sprites, self.active_sprites, self.collision_sprites],
            up_key=pygame.K_w,
            down_key=pygame.K_s,
        )

        # Player 2
        player.Player(
            (1180, (settings.SCREEN_HEIGHT / 2) - settings.PLAYER_HEIGHT / 2),
            [self.visible_sprites, self.active_sprites, self.collision_sprites],
            up_key=pygame.K_UP,
            down_key=pygame.K_DOWN,
        )

        # Ball
        ball.Ball(
            (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2),
            [self.visible_sprites, self.active_sprites],
            self.collision_sprites,
            self.ui
        )

    def run(self):
        # run the entire game (level)
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.ui.draw()
