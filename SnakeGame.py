import pygame
import sys
import random

pygame.init()

#Dictionary

Colors = {
    "MintyGreen": (40,210,180),
    "Red": (255,0,0),
    "LightBlue":(0,120,255)
}

Config = {
    "ScreenX":800,
    "ScreenY":600,
    "ScreenTittle": "Momo's Snake Game",
    "Background": Colors["MintyGreen"],
    "BlockSize": 10, 
    "Speed": 15
}

Snake = {
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2, 
    "Direction": "none",
    "Color": Colors["Red"], 
    "length": 0 ,
    "tail": []
}

Food = {
    "X": 0,
    "Y": 0,
    "Color": Colors["LightBlue"]
}

def RandmoizeFoodlocation():
    Food["X"] = round(random.randrange(0,Config["ScreenX"]-Config["BlockSize"]),-1)
    Food["Y"] = round(random.randrange(0,Config["ScreenY"]-Config["BlockSize"]),-1)

def DrawGame(screen):
    #Frames stacking on top of each other
    screen.fill(Config["Background"])
    pygame.draw.rect(screen, Snake["Color"], [Snake["X"], Snake["Y"], Config["BlockSize"], Config["BlockSize"]])
    for tail in Snake["tail"]:
        pygame.draw.rect(screen, Snake["Color"], [tail[0], tail[1], Config["BlockSize"], Config["BlockSize"]])
    pygame.draw.rect(screen, Food["Color"], [Food["X"], Food["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()

def main():
    #Backgroup Setting
    screen = pygame.display.set_mode((Config["ScreenX"], Config["ScreenY"]))
    clock = pygame.time.Clock()
    pygame.display.set_caption(Config["ScreenTittle"])
    pygame.display.update()
    RandmoizeFoodlocation()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Adding Snake potection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if Snake["Direction"] != "right":
                        Snake["Direction"] = "left"
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if Snake["Direction"] != "left":
                        Snake["Direction"] = "right"
                    
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if Snake["Direction"] != "down":
                        Snake["Direction"] = "up"
                    
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if Snake["Direction"] != "up": 
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
        

        DrawGame(screen)
        
        #Check for wall collision
        if Snake["X"] < 0 or Snake["X"] >= Config["ScreenX"] or Snake["Y"] < 0 or Snake["Y"] >= Config["ScreenY"]:
            print("You hit the wall!!")
            break
        #Hit tail or not
        if [Snake["X"], Snake["Y"]] in Snake["tail"]:
            print("You hit your tail!!!")
            break

        if Snake["X"] == Food["X"] and Snake["Y"] == Food["Y"]:
            Snake["length"] += 1
            Snake["tail"].append([Snake["X"],Snake["Y"]])
            RandmoizeFoodlocation()

        Snake["tail"].append([Snake["X"],Snake["Y"]])
        if len(Snake["tail"]) > Snake["length"]:
            del Snake["tail"][0]
        
        #Control the refesh rate
        clock.tick(Config["Speed"])

    

if __name__ == "__main__":
    main()


