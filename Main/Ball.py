import pygame
import random

ball_color = (2, 252, 132)
screen_width = 800
screen_height = 600
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)


class Balls:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 4
        self.speed = 2


def new_ball():
    ball = Balls()
    ball.x = random.randrange(ball.size, screen_width - ball.size)
    ball.y = random.randrange(ball.size, screen_height - ball.size)
    return ball
