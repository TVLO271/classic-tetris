import pygame
import sys
from grid import Grid
from blocks import *

pygame.init()

#create screen color
dark_blue = (44, 44, 127)

#create game window
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Classic Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

#create the L block-- says it is not created
block = TBlock()

#adding game loop for consistency in all players
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)
    
    pygame.display.update()
    clock.tick(60)