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
        screen.blit(menu, (0, 0))
        pygame.display.flip()
        clock.tick(fps)

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


def draw_objects(object_to_draw):
    pygame.draw.rect(screen, light_grey, object_to_draw)


def draw_score():
    score_1 = font.render(f"{score_player_1}", True, darker_grey)
    screen.blit(score_1, (40, 20))
    score_2 = font.render(f"{score_player_2}", True, darker_grey)
    screen.blit(score_2, (screen_width - score_2.get_width() - 40, 20))


def score_count(player):
    global score_player_1, score_player_2

    if player == 1:
        score_player_1 += 1
    else:
        score_player_2 += 1


def ball_reset():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= choice((1, -1))
    ball_speed_y *= choice((1, -1))


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Setting boundaries for the ball
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_reset()
        score_count(2)
    if ball.right >= screen_width:
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
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height

    if keys[pygame.K_LEFT] and player_2.top >= 0:
        player_2.y -= 10
    if keys[pygame.K_RIGHT] and player_2.bottom <= screen_height:
        player_2.y += 10


def players_animation():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and player_1.top >= 0:
        player_1.y -= 10
    if keys[pygame.K_a] and player_1.bottom <= screen_height:
        player_1.y += 10

    if keys[pygame.K_LEFT] and player_2.top >= 0:
        player_2.y -= 10
    if keys[pygame.K_RIGHT] and player_2.bottom <= screen_height:
        player_2.y += 10


# Frames
fps = 60

# Screen size
screen_width = 1000
screen_height = 600

# Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
darker_grey = (105, 105, 105)

# Ball speed in each axis
ball_speed_x = 7
ball_speed_y = 7

# Players' score
score_player_1 = 0
score_player_2 = 0

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
menu = pygame.image.load("./menu.png")

# Rects for the ball, player 1 and player 2
ball = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)
player_1 = pygame.Rect(5, screen_height / 2 - 45, 10, 90)
player_2 = pygame.Rect(screen_width - 15, screen_height / 2 - 45, 10, 90)

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
    screen.fill(bg_color)

    # Drawing the dashed  central line
    for i in range(0, 40, 3):
        draw_objects((screen_width / 2 - 1.5, i * 15, 3, 15))

    # Drawing the ball
    draw_objects(ball)
    # Drawing player 1
    draw_objects(player_1)
    # Drawing player 2
    draw_objects(player_2)

    draw_score()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
