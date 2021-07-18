import pygame
import os
import math
import time

pygame.init()

width = 1000
height = 600
bg_color = (255, 255, 255)
text_color = (227, 156, 134)
text_font = pygame.font.SysFont('comicsansms', 35)
ans_font = pygame.font.SysFont('comicsans', 90)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hang Man')

Ticks = 50
clock = pygame.time.Clock()
step = 0  # value for Hanging Status
gameloop = True
word = "TEST"
guessed_letters = []

radius = 25
offest = 20
btns = []
x_onset = round((width - (radius * 2 + offest) * 13) / 2)
y_onset = 450


# Fun fact: If you reading this I took the images and equation from TechWtiTim some video Lel

def load_imgs(folder: str):
    imgs = []

    for img in os.listdir(f'./{folder}'):
        img_surf = pygame.image.load(f'./{folder}/{img}')
        imgs.append(img_surf)

    return imgs


hang_surf = load_imgs('HangPos')


def hang_man(x, y):
    clock.tick(Ticks)
    screen.fill(bg_color)
    screen.blit(hang_surf[step], (x, y))


for let in range(26):
    x = x_onset + offest * 2 + ((radius * 2 + offest) * (let % 13))
    y = y_onset + ((let // 13) * (offest + radius * 2))

    btns.append([x, y, chr(65 + let), True])

def compose():

    show_wd = ''

    for char in btns:
        # print(char)
        x, y, letter, show = char

        if show:
            pygame.draw.circle(screen, text_color, (x, y), radius, 3)
            text = text_font.render(letter, 1, (0, 0, 0))
            screen.blit(text, (x - text.get_width() /
                        2, y - text.get_height() / 2))

    for letter in word:
        if letter in guessed_letters:
            show_wd += letter + ' '
        
        else:
            show_wd += '_ '

    txt = ans_font.render(show_wd, 1, (245, 213, 127))
    screen.blit(txt, (540, 215))

    

while gameloop:
    hang_man(100, 100)

    compose()

    for event in pygame.event.get():
        log = None

        if event.type == pygame.QUIT:
            gameloop = False
            print('QUIT')

            # Checking for quit event

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ms_x, ms_y = pygame.mouse.get_pos()

            for letter in btns:
                x, y, let, show = letter

                if show:
                    distance = math.sqrt((x - ms_x) ** 2 + (y - ms_y) ** 2)

                    if distance < radius:
                        letter[3] = False
                        guessed_letters.append(let)
                        
                        step += 1 if let not in word else 0
                        print(let, x, y)
                        

    pygame.display.update()