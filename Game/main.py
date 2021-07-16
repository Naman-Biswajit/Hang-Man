import pygame
import os

pygame.init()

width = 1000
height = 600
bg_color = (255, 255, 255)
text_color = (227, 156, 134)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hang Man')

Ticks = 50
clock = pygame.time.Clock()
step = 0 # value for Hanging Status
gameloop = True

radius = 25
offest = 20
btns = []
x_onset = round((width - (radius * 2 + offest) * 13) / 2)
y_onset = 450

for let in range(26):
    x = x_onset + offest * 2 +( (radius * 2 + offest) * (let % 13))
    y = y_onset + ((let // 13) * (offest + radius * 2))

    btns.append([x, y])

# Fun fact: If you reading this I took the images and equation from TechWtiTim some video Lel

def load_imgs(folder: str):
    imgs = []

    for img in os.listdir(f'./{folder}'):
        img_surf  = pygame.image.load(f'./{folder}/{img}')
        imgs.append(img_surf)
    
    return imgs

print(pygame.font.get_fonts())

hang_surf  = load_imgs('HangPos')

def hang_man(x, y):
    clock.tick(Ticks)
    screen.fill(bg_color)
    screen.blit(hang_surf[step], (x, y))

def compose():
    for char in btns:
        x, y = char
        pygame.draw.circle(screen, text_color, (x, y), radius, 3)

while gameloop:
    
    hang_man(100, 100)
    compose()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            gameloop = False
            print('Quit Event Emitted')
            
            # Checking for quit event

        if event.type == pygame.MOUSEBUTTONDOWN:
            cords = pygame.mouse.get_pos()
            print(cords)

    pygame.display.update()