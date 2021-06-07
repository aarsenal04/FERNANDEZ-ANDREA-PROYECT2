import pygame
import sys
from pygame.locals import *

# to delimit the movement of the frames
FPS = 60
clock = pygame.time.Clock()

# to execute pygame
pygame.init()

# main screen and size
screen1 = pygame.display.set_mode((1000, 650))

# icon and name
pygame.display.set_caption("M A R I O  I N V A S I O N")
icon = pygame.image.load("./images/black_bullet.png")
pygame.display.set_icon(icon)

# to start writing the name(name input)
namebox = ""

# images for backgrounds
mainscreen = ("./images/background.png")
instructiontext = ("./images/instructions.png")

# global for score 
score = 0

def menu():

    global namebox

    # loop that keeps the window active
    while True:

        # to delimit the movement of the frames
        clock.tick(FPS)

        # background
        background = pygame.image.load(mainscreen)
        screen1.blit(background, (0, 0))

        # font and fonts´sizes
        gamefont = pygame.font.Font("./images/mariofont.ttf", 50)
        gamefont2 = pygame.font.Font("./images/mariofont.ttf", 35)

        # caption background
        entryspace = pygame.image.load("./images/entryspace.png").convert_alpha()
        entryspace = pygame.transform.scale(entryspace, (800, 80))
        screen1.blit(entryspace, (95, 77))

        # displaying the name of the game
        gamename = gamefont.render("M A R I O  I N V A S I O N", 0, (255,255,255))
        screen1.blit(gamename, (110, 95))

        # entry space line
        entryspace = pygame.image.load("./images/entryspace.png").convert_alpha()
        entryspace = pygame.transform.scale(entryspace, (500, 5))
        screen1.blit(entryspace, (245, 230))

        # name box
        namebox1 = gamefont2.render(namebox, 0, (255, 255, 255))
        screen1.blit (namebox1, (500 - namebox1.get_width()//2, 200))

        # levels section
        levelsection = gamefont.render("levels", 0, (222, 89, 24))
        screen1.blit(levelsection, (160, 350))

        # about
        about = gamefont.render("about", 0, (222, 89, 24))
        screen1.blit(about, (640, 350))

        # mario image on menu to decorate
        marioright = pygame.image.load("./images/right_mario.png").convert_alpha()
        marioright = pygame.transform.scale(marioright, (150, 150))
        screen1.blit(marioright, (50, 180))
        marioleft = pygame.image.load("./images/left_mario.png").convert_alpha()
        marioleft = pygame.transform.scale(marioleft, (150, 150))
        screen1.blit(marioleft, (785, 180))

        # enemies on top of the menu to decorate
        greenturtle1 = pygame.image.load("./images/green_turtle1.png").convert_alpha()
        greenturtle1 = pygame.transform.scale(greenturtle1, (50, 50))
        screen1.blit(greenturtle1, (538, 10))
        grayturtle1 = pygame.image.load("./images/gray_turtle1.png").convert_alpha()
        grayturtle1 = pygame.transform.scale(grayturtle1, (50, 50))
        screen1.blit(grayturtle1, (418, 10))
        greenwizard = pygame.image.load("./images/green_cloud.png").convert_alpha()
        greenwizard = pygame.transform.scale(greenwizard, (50, 50))
        screen1.blit(greenwizard, (358, 10))
        brownturtle1 = pygame.image.load("./images/brown_turtle1.png").convert_alpha()
        brownturtle1 = pygame.transform.scale(brownturtle1, (50, 50))
        screen1.blit(brownturtle1, (298, 10))
        browncloud = pygame.image.load("./images/brown_cloud.png").convert_alpha()
        browncloud = pygame.transform.scale(browncloud, (50, 50))
        screen1.blit(browncloud, (478, 10))
        graycloud = pygame.image.load("./images/gray_cloud.png").convert_alpha()
        graycloud = pygame.transform.scale(graycloud, (50, 50))
        screen1.blit(graycloud, (598, 10))
        redturtle1 = pygame.image.load("./images/red_turtle1.png").convert_alpha()
        redturtle1 = pygame.transform.scale(redturtle1, (50, 50))
        screen1.blit(redturtle1, (658, 10))
        whitebullet = pygame.image.load("./images/white_bullet.png").convert_alpha()
        whitebullet = pygame.transform.scale(whitebullet, (50, 50))
        screen1.blit(whitebullet, (238, 10))
        cyanbullet = pygame.image.load("./images/cyan_bullet.png").convert_alpha()
        cyanbullet = pygame.transform.scale(cyanbullet, (50, 50))
        screen1.blit(cyanbullet, (718, 10))

        # images of the level buttons
        buttonlevel1 = gamefont2.render("level 1", 0, (255,255,255))
        screen1.blit(buttonlevel1, (180, 400))
        buttonlevel2 = gamefont2.render("level 2", 0, (255,255,255))
        screen1.blit(buttonlevel2, (180, 450))
        buttonlevel3 = gamefont2.render("level 3", 0, (255,255,255))
        screen1.blit(buttonlevel3, (185, 500))

        # checks if the player clicks the buttons
        for click in pygame.event.get():
             if click.type == KEYDOWN:
                if click.key == K_BACKSPACE:
                    namebox = namebox[:-1]
                else:
                    namebox += click.unicode
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the level 1 button
                 if mouse_x >= 180 and mouse_x <= 337:
                     if namebox != "":
                         if mouse_y >= 400 and mouse_y <= 428:
                             first_level(namebox)
                             flag = 0

                # get the click on the level 2 button
                 if mouse_x >= 180 and mouse_x <= 337:
                     if namebox!="":
                         if mouse_y >= 450 and mouse_y <= 478:
                             second_level(namebox)
                             flag = 0

                # get the click on the level 3 button
                 if mouse_x >= 185 and mouse_x <= 342:
                     if namebox != "":
                         if mouse_y >= 500 and mouse_y <= 528:
                             third_level(namebox)
                             flag = 0

                # prueba
                # prueba = pygame.image.load("./images/prueba.png").convert_alpha()
                # prueba = pygame.transform.scale(prueba, (157, 28)) #tamaño
                # screen1.blit(prueba, (185, 500)) #x, y

                # get the click on the instructions button
                 if mouse_x >= 590 and mouse_x <= 870:
                     if mouse_y >= 450 and mouse_y <= 478:
                         instructions()
                         flag = 0

                # get the click on the information button
                 if mouse_x >= 600 and mouse_x <= 880:
                     if mouse_y >= 400 and mouse_y <= 428:
                         information()
                         flag = 0

                # get the click on the leaderboard button
                 if mouse_x >= 608 and mouse_x <= 888:
                     if mouse_y >= 500 and mouse_y <= 528:
                         leader_board()
                         flag = 0

        # entry name label
        entryname = gamefont.render("entry name", 0, (255,255,255))
        screen1.blit(entryname, (320, 240))

        # info button
        infobutton = gamefont2.render("information", 0, (255,255,255))
        screen1.blit(infobutton, (600, 400))

        # instructions button
        instructionsbutton = gamefont2.render("instructions", 0, (255,255,255))
        screen1.blit(instructionsbutton, (590, 450))

        # leaderboard button
        leaderboard = gamefont2.render("leaderboard", 0, (255,255,255))
        screen1.blit(leaderboard, (608, 500))

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

menu()