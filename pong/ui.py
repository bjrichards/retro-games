import pygame
import settings


class UI:
    def __init__(self, display):
        self.score = [0, 0]
        self.display = display

        self.font = pygame.font.SysFont(settings.FONT, settings.FONT_SIZE)
        self.font_color = settings.FONT_COLOR

    def increase_score(self, player: int):
        self.score[player] += 1

    def draw(self):
        score_1 = self.font.render(str(self.score[0]), True, self.font_color)
        score_2 = self.font.render(str(self.score[1]), True, self.font_color)

        self.display.blit(score_1, settings.SCORE_1_POS)
        self.display.blit(score_2, settings.SCORE_2_POS)
