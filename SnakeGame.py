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
    "BlockSize": 10, 
    "Speed": 20
}

Snake = {
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2, 
    "Direction": "none"
}

#Backgroup Setting
screen = pygame.display.set_mode((Config["ScreenX"], Config["ScreenY"]))
clock = pygame.time.Clock()
pygame.display.set_caption(Config["ScreenTittle"])
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #More than one case
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Snake["Direction"] = "left"
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Snake["Direction"] = "right"
                
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Snake["Direction"] = "up"
                
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Snake["Direction"] = "down"
                
    #If we don't set a clock for speed, it will move super fast like computer XD
    if Snake["Direction"] == "left":
        Snake["X"] -= Config["BlockSize"]
    if Snake["Direction"] == "right":
        Snake["X"] += Config["BlockSize"]
    if Snake["Direction"] == "up":
        Snake["Y"] -= Config["BlockSize"]
    if Snake["Direction"] == "down":
        Snake["Y"] += Config["BlockSize"]
                    
            

    #frames stacking on top of each other
    screen.fill(Config["MintyGreen"])
    pygame.draw.rect(screen, Config["Red"], [Snake["X"], Snake["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()
    clock.tick(Config["Speed"])

