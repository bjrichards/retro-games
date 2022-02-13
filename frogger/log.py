import pygame


class Log(pygame.sprite.Sprite):
    def __init__(
        self, pos, groups, width, height, color, speed, direction: pygame.math.Vector2
    ):
        super().__init__(groups)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

        self.type = "log"

        # player movement
        self.direction = direction
        self.speed = speed

        self.pos = pos

    def update(self, dt):
        x = self.direction[0] * self.speed * dt + self.pos[0]
        y = self.direction[1] * self.speed * dt + self.pos[1]
        self.pos = (x, y)
        self.rect.center = round(x), round(y)  # type:ignore
