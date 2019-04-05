from Main.Ball import *
from Main.Food import *
from Main.Button import *

# color
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
orange = (200, 110, 0)
light_red = (255, 0, 0)
light_green = (0, 255, 0)
light_orange = (255, 165, 0)

# time
clock = pygame.time.Clock()

# init objects
balls = new_ball()
food = new_food()


def start_screen():
    pygame.init()
    pygame.display.set_caption("Suck My Balls")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        button("Start", green, light_green, 650, 250, 100, 50, game_screen)
        button("Help", orange, light_orange, 650, 350, 100, 50, tutorial)
        button("Quit", red, light_red, 650, 450, 100, 50, quit)

        text = pygame.font.SysFont("comicsansms", 115)
        text_surface = text.render("Suck My Balls", True, black)
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width/2, screen_height/2-200)
        screen.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(15)


def tutorial():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        button("Start", green, light_green, 650, 250, 100, 50, game_screen)
        button("Help", orange, light_orange, 650, 350, 100, 50, tutorial)
        button("Quit", red, light_red, 650, 450, 100, 50, quit)

        text = pygame.font.SysFont("Arial", 20)
        text_surface = text.render("* Use arrow key to move your ball and eat others to survive", True, black)
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width/2, screen_height/2-200)
        screen.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(15)


def game_screen():
    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False

    while True:
        screen.fill(white)
        pygame.draw.circle(screen, ball_color, [balls.x, balls.y], balls.size)
        pygame.draw.circle(screen, growth_ball_color, [food.x, food.y], food.size)

        if balls.x == food.x:
            food.x = random.randrange(5, 795)
            food.y = random.randrange(5, 595)
            balls.size += 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pressed_left = True
                elif event.key == pygame.K_RIGHT:
                    pressed_right = True
                elif event.key == pygame.K_UP:
                    pressed_up = True
                elif event.key == pygame.K_DOWN:
                    pressed_down = True

            elif event.type == pygame.KEYUP:            # check for key releases
                if event.key == pygame.K_LEFT:        # left arrow turns left
                    pressed_left = False
                elif event.key == pygame.K_RIGHT:     # right arrow turns right
                    pressed_right = False
                elif event.key == pygame.K_UP:    # up arrow goes up
                    pressed_up = False
                elif event.key == pygame.K_DOWN:     # down arrow goes down
                    pressed_down = False

        if pressed_up:
            balls.y -= balls.speed
        if pressed_down:
            balls.y += balls.speed
        if pressed_left:
            balls.x -= balls.speed
        if pressed_right:
            balls.x += balls.speed

        if balls.x >= screen_width:
            balls.x = 1
        if balls.x <= 0:
            balls.x = screen_width-1
        if balls.y >= screen_height:
            balls.y = 1
        if balls.y <= 0:
            balls.y = screen_height-1

        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    start_screen()
