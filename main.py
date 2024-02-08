import pygame


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Setting boundaries for the ball
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1


# Screen size
screen_width = 1000
screen_height = 600

# Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Ball speed in each direction
ball_speed_x = 7
ball_speed_y = 7

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

ball = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)
player_1 = pygame.Rect(10, screen_height / 2 - 45, 10, 90)
player_2 = pygame.Rect(screen_width - 20, screen_height / 2 - 45, 10, 90)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_animation()
    keys = pygame.key.get_pressed()

    # Set background color
    screen.fill(bg_color)

    # Central dashed line
    for i in range(0, 40, 3):
        pygame.draw.rect(screen, light_grey, (screen_width / 2 - 1.5, i * 15, 3, 15))

    # Drawing the ball
    pygame.draw.rect(screen, light_grey, ball)

    # Player 1
    pygame.draw.rect(screen, light_grey, player_1)
    if keys[pygame.K_d] and player_1.top >= 0:
        player_1.y -= 20
    if keys[pygame.K_a] and player_1.bottom <= screen_height:
        player_1.y += 20

    # Player 2
    pygame.draw.rect(screen, light_grey, player_2)
    if keys[pygame.K_RIGHT] and player_2.top >= 0:
        player_2.y -= 20
    if keys[pygame.K_LEFT] and player_2.bottom < screen_height:
        player_2.y += 20

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
