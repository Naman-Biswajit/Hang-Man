import pygame
# import os

pygame.init()

width = 1000
height = 600
bg_color = (255, 255, 255)

screen_1 = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hang Man')
screen_1.fill(bg_color)

Ticks = 50
clock = pygame.time.Clock()

gameloop = True

while gameloop:
    clock.tick(Ticks)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            gameloop = False
            print('Quit Event Emitted')
            
            # Checking for quit event

        if event.type == pygame.MOUSEBUTTONDOWN:
            cords = pygame.mouse.get_pos()
            print(cords)