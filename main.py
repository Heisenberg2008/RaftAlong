from random import random, randrange
import sys
import pygame

# Setup here
clock = pygame.time.Clock()
fps = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Raft Along")

# Defining some colors
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (43,192,255)

# Game variables
player_image = pygame.image.load('img/Boat.png')
rock_image = pygame.image.load('img/Rock.png')
x = SCREEN_WIDTH / 2
y = 100
rock_x = randrange(6, SCREEN_WIDTH - 52)
rock_y = SCREEN_HEIGHT - 25

# Functions
def player_render(player_image, x, y):
    display.blit(player_image, (x, y))

def move(x):
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        # facing = 'left'
        return 1

    if key_input[pygame.K_RIGHT]:
        # facing = 'right'
        return 2
    
    else: return 0

def rock_move(rock_y):
    rock_y -= 4
    return rock_y

def rock_draw(rock_x, rock_y):
    display.blit(rock_image, (rock_x, rock_y))

def game_over(player_rect, rock_rect):
    if pygame.Rect.colliderect(player_rect, rock_rect) == True:
        return True

# Game Loop
while True:
    player_rect = pygame.Rect(x, y, 46, 41)
    rock_rect = pygame.Rect(rock_x + 40, rock_y, 320, 280)

    display.fill(blue)
    player_render(player_image, x, y)
    rock_y = rock_move(rock_y)
    rock_draw(rock_x, rock_y)
    if rock_y < -300:
        rock_x = randrange(6, SCREEN_WIDTH - 700)
        rock_y = SCREEN_HEIGHT - 25

    if move(x) == 1:
        if x > 6:
            x -= 5
    if move(x) == 2:
        if x < SCREEN_WIDTH - 52:
            x += 5
    elif move(x) == 0:
        pass

    if game_over(player_rect, rock_rect) == True:
        pygame.QUIT
        sys.exit()

    # For Debugging
    pygame.draw.rect(display, white, (player_rect), 2)
    pygame.draw.rect(display, red, (rock_rect), 2)

    # Display update stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    clock.tick(fps)