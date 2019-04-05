import pygame

screen_width = 800
screen_height = 600
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)
black = (0, 0, 0)


def button(name, inactive_color, active_color, x_position, y_position, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_position+width > mouse[0] > x_position and y_position+height > mouse[1] > y_position:
        pygame.draw.rect(screen, inactive_color, (x_position, y_position, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, active_color, (x_position, y_position, width, height))

    text = pygame.font.SysFont("timenewroman", 20)
    text_surface = text.render(name, True, black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((x_position+(width/2)), (y_position+(height/2)))
    screen.blit(text_surface, text_rect)
