import pygame
import sys

pygame.init()

#Dictionary
Config = {
    "ScreenX":800,
    "ScreenY":600,
    "ScreenTittle": "Momo's Snake Game",
    "MintyGreen": (40,210,180),
    "Red": (255,0,0),
    "BlockSize": 10
}

Snake = {
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2
}

#Backgroup Setting
screen = pygame.display.set_mode((Config["ScreenX"], Config["ScreenY"]))
pygame.display.set_caption(Config["ScreenTittle"])
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #More than one case
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Snake["X"] -= Config["BlockSize"]
            if event.key == pygame.K_RIGHT:
                Snake["X"] += Config["BlockSize"]
            if event.key == pygame.K_UP:
                Snake["Y"] -= Config["BlockSize"]
            if event.key == pygame.K_DOWN:
                Snake["Y"] += Config["BlockSize"]
            
            #Only for one case    
            match event.key:
                case pygame.K_d:
                    Snake["X"] += Config["BlockSize"]
                case pygame.K_w:
                    Snake["Y"] -= Config["BlockSize"]
                case pygame.K_s:
                    Snake["Y"] += Config["BlockSize"]

    #frames stacking on top of each other
    screen.fill(Config["MintyGreen"])
    pygame.draw.rect(screen, Config["Red"], [Snake["X"], Snake["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()
    

