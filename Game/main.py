import pygame
import os

pygame.init()

width = 1000
height = 600
bg_color = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hang Man')

Ticks = 50
clock = pygame.time.Clock()

gameloop = True


def load_imgs(folder: str):
    imgs = []

    for img in os.listdir(f'./{folder}'):
        img_surf  = pygame.image.load(f'./{folder}/{img}')
        imgs.append(img_surf)
    
    return imgs


hang_surf  = load_imgs('HangPos')

while gameloop:
    step = 0 # value for Hanging Status

    clock.tick(Ticks)
    screen.fill(bg_color)
    screen.blit(hang_surf[step], (100, 100))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            gameloop = False
            print('Quit Event Emitted')
            
            # Checking for quit event

        if event.type == pygame.MOUSEBUTTONDOWN:
            cords = pygame.mouse.get_pos()
            print(cords)

    pygame.display.update()