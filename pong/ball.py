import pygame
import settings
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, ui):
        super().__init__(groups)
        self.image = pygame.Surface((settings.BALL_RADIUS, settings.BALL_RADIUS))
        self.color = settings.BALL_COLOR
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=pos)

        # player movement
        self.direction = pygame.math.Vector2(-1, 0)
        self.speed = 8
        self.collision_sprites = collision_sprites

        self.ui = ui

    def rectify_position(self):
        if self.rect.top <= 0:  # type:ignore
            self.rect.top = 0  # type:ignore
            self.direction.y = 1  # type:ignore
        elif self.rect.bottom >= settings.SCREEN_HEIGHT:  # type:ignore
            self.rect.bottom = settings.SCREEN_HEIGHT  # type:ignore
            self.direction.y = -1  # type:ignore

    def collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.calculate_ball_reflection(sprite)

    def check_score_condition(self):
        if self.rect.left < 0:  # type:ignore
            self.rect.center = (  # type:ignore
                settings.SCREEN_WIDTH / 2,
                settings.SCREEN_HEIGHT / 2,
            )
            self.direction = pygame.math.Vector2(-1, 0)
            self.ui.increase_score(1)
        elif self.rect.right > settings.SCREEN_WIDTH:  # type:ignore
            self.rect.center = (  # type:ignore
                settings.SCREEN_WIDTH / 2,
                settings.SCREEN_HEIGHT / 2,
            )
            self.direction = pygame.math.Vector2(1, 0)
            self.ui.increase_score(0)

    def calculate_ball_reflection(self, sprite):
        relative_intersect_y = (
            sprite.rect.y + (settings.PLAYER_HEIGHT / 2)
        ) - self.rect.y  # type:ignore

        normalized_relative_intersect_y = relative_intersect_y / (
            settings.PLAYER_HEIGHT / 2
        )
        bounce_angle = normalized_relative_intersect_y * settings.MAX_BOUNCE_ANGLE

        dir_correction = -1
        if self.rect.x < settings.SCREEN_WIDTH / 2:  # type:ignore
            dir_correction = 1

        self.direction.x = math.cos(bounce_angle) * dir_correction
        self.direction.y = -math.sin(bounce_angle)

    def update(self):
        self.check_score_condition()
        self.collisions()
        self.rect.topleft += self.direction * self.speed  # type:ignore
        self.rectify_position()
