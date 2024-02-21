import sys
import pygame
from random import choice


def init_menu():
    run = True
    while run:
        for menu_event in pygame.event.get():
            if menu_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x, y = pygame.mouse.get_pos()
        SCREEN.blit(MENU, (0, 0))
        pygame.display.flip()
        CLOCK.tick(FPS)

        for event_menu in pygame.event.get():
            if event_menu.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event_menu.type == pygame.MOUSEBUTTONDOWN:
                if x in range(321, 679) and y in range(376, 445):
                    return 1
                elif x in range(334, 666) and y in range(289, 352):
                    return 2
            elif x in range(334, 666) and y in range(289, 352) or x in range(321, 679) and y in range(376, 445):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def draw_object(object_to_draw):
    pygame.draw.rect(SCREEN, LIGHT_GREY, object_to_draw)


def draw_score():
    score_1 = FONT.render(f"{score_player_1}", True, DARK_GREY)
    SCREEN.blit(score_1, (40, 20))
    score_2 = FONT.render(f"{score_player_2}", True, DARK_GREY)
    SCREEN.blit(score_2, (SCREEN_WIDTH - score_2.get_width() - 40, 20))


def score_count(player):
    global score_player_1, score_player_2

    if player == 1:
        score_player_1 += 1
    else:
        score_player_2 += 1


def ball_reset():
    global ball_speed_x, ball_speed_y

    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ball_speed_x *= choice((1, -1))
    ball_speed_y *= choice((1, -1))


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Setting boundaries for the ball
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_reset()
        score_count(2)
    if ball.right >= SCREEN_WIDTH:
        ball_reset()
        score_count(1)

    # Adding collision with the players
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1


def solo_player_mode():
    keys = pygame.key.get_pressed()
    if player_1.top > ball.y:
        player_1.y -= 10
    if player_1.bottom < ball.y:
        player_1.y += 10
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= SCREEN_HEIGHT:
        player_1.bottom = SCREEN_HEIGHT

    if keys[pygame.K_LEFT] and player_2.top >= 0:
        player_2.y -= 10
    if keys[pygame.K_RIGHT] and player_2.bottom <= SCREEN_HEIGHT:
        player_2.y += 10


def players_animation():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and player_1.top >= 0:
        player_1.y -= 10
    if keys[pygame.K_a] and player_1.bottom <= SCREEN_HEIGHT:
        player_1.y += 10

    if keys[pygame.K_LEFT] and player_2.top >= 0:
        player_2.y -= 10
    if keys[pygame.K_RIGHT] and player_2.bottom <= SCREEN_HEIGHT:
        player_2.y += 10


FPS = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

BG_COLOR = pygame.Color('grey12')
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (105, 105, 105)

# Ball speed in each axis
ball_speed_x = 7
ball_speed_y = 7

# Players' score
score_player_1 = 0
score_player_2 = 0

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)
MENU = pygame.image.load("./menu.png")

# Rects for the ball, player 1 and player 2
ball = pygame.Rect(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 - 10, 20, 20)
player_1 = pygame.Rect(5, SCREEN_HEIGHT / 2 - 45, 10, 90)
player_2 = pygame.Rect(SCREEN_WIDTH - 15, SCREEN_HEIGHT / 2 - 45, 10, 90)

game_mode = init_menu()

running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_animation()
    if game_mode == 1:
        players_animation()
    else:
        solo_player_mode()

    # Set background color
    SCREEN.fill(BG_COLOR)

    # Drawing the dashed  central line
    for i in range(0, 40, 3):
        draw_object((SCREEN_WIDTH / 2 - 1.5, i * 15, 3, 15))

    # Drawing the ball
    draw_object(ball)
    # Drawing player 1
    draw_object(player_1)
    # Drawing player 2
    draw_object(player_2)

    draw_score()

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
