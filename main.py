import pygame
import sys
import random

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

# Classes
class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('img/Boat.png')
        self.rect = self.image.get_rect()
    
    def draw(self):
        pygame.draw.rect(display, white, self.rect, 2)

class Rocks:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('img/Rock.png')
        self.rect = self.image.get_rect()

# Game variables
player = Player(SCREEN_WIDTH / 2, 50)
rock = Rocks(random.randrange(50 ,SCREEN_WIDTH - 50), SCREEN_HEIGHT)
x = SCREEN_WIDTH / 2
y = 200
facing = 'right'
temp_image = player.image
rock_x = int
rock_y = int

# Functions
def move(facing):
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        facing = 'left'
        player.x -= 3

    if key_input[pygame.K_RIGHT]:
        facing = 'right'
        player.x += 3
    
    return facing

def wrap(x):
    if x + 46 <= 0:
        return 'WrapToRight'
    if x >= SCREEN_WIDTH:
        return 'WrapToLeft'

def spawn(rock):
    rock = random.randrange(50, SCREEN_WIDTH - 50)
    return rock

# Game Loop
while True:
    # Drawing Screen
    display.fill(blue)
    player.draw()

    if rock.y == -20:
        rock = spawn(rock)

    player.rect = (player.x - 23, player.y, 46,41)
    rock.rect = (rock.x, rock.y, 20,20)

    if wrap(player.x) == 'WrapToRight':
        player.x =  SCREEN_WIDTH - 1
    if wrap(player.x) == 'WrapToLeft':
        player.x = -45

    if move(facing) == 'left': 
        temp_image = pygame.transform.flip(player.image, True, False)
        display.blit(temp_image, (player.x -23, player.y))

    if move(facing) == 'right': display.blit(player.image, (player.x-23, player.y))

    # Display update stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    clock.tick(fps)