import pygame


class Log(pygame.sprite.Sprite):
    def __init__(
        self, pos, groups, width, height, color, speed, direction: pygame.math.Vector2
    ):
        super().__init__(groups)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect: pygame.rect.Rect = self.image.get_rect(center=pos)

        self.type: str = "log"

        # player movement
        self.direction: pygame.math.Vector2 = direction
        self.speed: pygame.math.Vector2 = speed

        self.pos: tuple = pos

    def update(self, dt):
        x = self.direction[0] * self.speed * dt + self.pos[0]
        y = self.direction[1] * self.speed * dt + self.pos[1]
        self.pos = (x, y)
        self.rect.center = (round(x), round(y))
