import pygame
import random

growth_ball_color = (252, 3, 132)
screen_width = 800
screen_height = 600
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 2


def new_food():
    food = Food()
    food.x = random.randrange(food.size, screen_width - food.size)
    food.y = random.randrange(food.size, screen_height - food.size)
    return food
