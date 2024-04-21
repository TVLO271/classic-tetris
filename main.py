import pygame
import sys
from game import Game

pygame.init()

#create screen color
dark_blue = (44, 44, 127)

#create game window
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Classic Tetris")

clock = pygame.time.Clock()

#create game object
game = Game()

#adding game loop for consistency in all players
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #to detect block movement using keyboard,call game.py
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            
    #Drawing
    screen.fill(dark_blue)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)