import pygame
import sys
import random
from pygame.locals import *

# to delimit the movement of the frames
FPS = 60
clock = pygame.time.Clock()

# to execute pygame
pygame.init()

# to execute the music
pygame.mixer.init()

# main screen and size
screen1 = pygame.display.set_mode((1000, 650))

# icon and name
pygame.display.set_caption("M A R I O  I N V A S I O N")
icon = pygame.image.load("./images/gray_cloud.png")
pygame.display.set_icon(icon)

# to start writing the name(name input)
namebox = ""

# player´s life from the beggining of each level
life = 3

# images for backgrounds
mainscreen = ("./images/background.png")
level1_screen = ("./images/background.png")
level2_screen = ("./images/level2bg.jpg")
level3_screen = ("./images/level3bg.png")
finalscreen = ("./images/finalbg.png")
instructiontext = ("./images/instructions.png")
infoscreen = ("./images/information.png")
endgamescreen = ("./images/finalbg.png")

# characters
mario1 = pygame.image.load("./images/right_mario.png")
mario2 = pygame.image.load("./images/left_mario.png")
marioright = pygame.image.load("./images/right_mario.png").convert_alpha()
marioright = pygame.transform.scale(marioright, (150, 150))
greenwizard = pygame.image.load("./images/green_cloud.png").convert_alpha()
greenwizard = pygame.transform.scale(greenwizard, (50, 50))
browncloud = pygame.image.load("./images/brown_cloud.png").convert_alpha()
browncloud = pygame.transform.scale(browncloud, (50, 50))
graycloud = pygame.image.load("./images/gray_cloud.png").convert_alpha()
graycloud = pygame.transform.scale(graycloud, (50, 50))
marioleft = pygame.image.load("./images/left_mario.png").convert_alpha()
marioleft = pygame.transform.scale(marioleft, (150, 150))

# hit sound
hits = pygame.mixer.Sound("./images/hit.mp3")

#global for score 
score = 0

# menu screen (first screen)
def menu():

    #music for screen
    pygame.mixer.music.load("./images/entertainer.mp3")
    pygame.mixer.music.play(-1,0,0)

    # global for the player to write the game
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
        cpfont = pygame.font.Font("./images/mariofont.ttf", 20)

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

        # name box
        namebox1 = gamefont2.render(namebox, 0, (255, 255, 255))
        screen1.blit (namebox1, (500 - namebox1.get_width()//2, 200))

        # levels section
        levelsection = gamefont.render("levels", 0, (222, 89, 24))
        screen1.blit(levelsection, (160, 350))

        # copyright 
        copyright = cpfont.render("Nintendo theme used for educational purposes", 0, (0,0,0))
        screen1.blit(copyright, (210, 300))

        # about
        about = gamefont.render("about", 0, (222, 89, 24))
        screen1.blit(about, (640, 350))

        # mario image on menu to decorate and his enemies
        screen1.blit(marioright, (50, 180))
        screen1.blit(marioleft, (785, 180))
        screen1.blit(entryspace, (245, 230))
        screen1.blit(greenwizard, (478, 10))
        screen1.blit(browncloud, (538, 10))
        screen1.blit(graycloud, (418, 10))

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

            # to check the mouse clicks
             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the level 1 button
                 if mouse_x >= 180 and mouse_x <= 337:
                     if namebox != "":
                         if mouse_y >= 400 and mouse_y <= 428:
                             level1(namebox)
                             flag = 0

                # get the click on the level 2 button
                 if mouse_x >= 180 and mouse_x <= 337:
                     if namebox!="":
                         if mouse_y >= 450 and mouse_y <= 478:
                             level2(namebox)
                             flag = 0

                # get the click on the level 3 button
                 if mouse_x >= 185 and mouse_x <= 342:
                     if namebox != "":
                         if mouse_y >= 500 and mouse_y <= 528:
                             level3(namebox)
                             flag = 0

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

# instrcutions screen
def instructions():

    # music for the screen
    pygame.mixer.music.load("./images/chariots.mp3")
    pygame.mixer.music.play(-1,0,0)

    # loop that keeps the window active
    while True:
        
        # to delimit the movement of the frames
        clock.tick(FPS)

        # instructions background image
        inst_bg = pygame.image.load(instructiontext)
        screen1.blit(inst_bg, (0, 0))

        # backbutton
        buttonfont = pygame.font.Font("./images/mariofont.ttf", 40)
        backbutton = buttonfont.render("back", 0, (255,255,255))
        screen1.blit(backbutton, (20, 600))

        # checks if the player clicks the back button
        for click in pygame.event.get():
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

            # to check the mouse clicks
             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the back button
                 if mouse_x >= 20 and mouse_x <= 120:
                         if mouse_y >= 600 and mouse_y <= 628:
                             menu()
                             flag = 0

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

# info screen (credits)
def information():

    # music for the screen
    pygame.mixer.music.load("./images/simpsons.mp3")
    pygame.mixer.music.play(-1,0,0)
    
    # loop that keeps the window active
    while True:
        
        # to delimit the movement of the frames
        clock.tick(FPS)

        # info background image
        info_bg = pygame.image.load(infoscreen)
        screen1.blit(info_bg, (0, 0))

        # backbutton
        buttonfont = pygame.font.Font("./images/mariofont.ttf", 40)
        backbutton = buttonfont.render("back", 0, (255,255,255))
        screen1.blit(backbutton, (20, 600))

        # checks if the player clicks the back button
        for click in pygame.event.get():
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

            # to check the mouse clicks
             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the back button
                 if mouse_x >= 20 and mouse_x <= 120:
                         if mouse_y >= 600 and mouse_y <= 628:
                             menu()
                             flag = 0

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

# level 1 screen
def level1(namebox):

    #music for screen
    pygame.mixer.music.load("./images/chicken.mp3")
    pygame.mixer.music.play(-1,0,0)

    # global for the player´s score
    global score
    score=0 

    # for time
    time = 0
    secondstimer = 0

    # to work with the frames (timing)
    clock = pygame.time.Clock()

    # class for the character player
    class marioplayer:
        def __init__(self, x, y, health = 3):
            self.x = x
            self.y = y
            self.health = health
            self.left = True
            #self.mario1 = mario1
            self.cool_down_counter = 0

        # to draw the capitalist ship
        def draw(self, screen1):
            if self.left:
                screen1.blit(mario2, (self.x, self.y))
            else:
                screen1.blit(mario1, (self.x, self.y))

    # class for the enemies
    class enemies():
        def __init__(self, x, y, xspeed, yspeed):
            self.x = x
            self.y = y
            self.xspeed = xspeed
            self.yspeed = yspeed

        def moveenemy(self):
            if self.x <=0:
                self.xspeed = random.randint(1,5)
                self.yspeed = random.randint(-5,5)
                hits.play()
            if self.x + self.xspeed +50 >= 1000:
                self.xspeed = random.randint(1,5)*-1
                self.yspeed = random.randint(-5,5)
                hits.play()
            if self.y <=0:
                self.yspeed = random.randint(1,5)
                self.xspeed = random.randint(-5,5)
                hits.play()
            if self.y + self.yspeed +50 >= 550:
                self.yspeed = random.randint(1,5)*-1
                self.xspeed = random.randint(-5,5)
                hits.play()
            else:
                self.x += self.xspeed
                self.y += self.yspeed

        def draw(self, screen1):
            screen1.blit(graycloud, (self.x, self.y))

    def collisions(hits, marioplayer):
        global life
        for i in hits:
            if marioplayer.x < i.x < marioplayer.x + 100:
                if marioplayer.y < i.y < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x +50 < marioplayer.x + 100:
                if marioplayer.y < i.y < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x < marioplayer.x + 100:
                if marioplayer.y < i.y +50 < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x +50 < marioplayer.x + 100:
                if marioplayer.y < i.y + 50 < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1

    # characters on screen
    mariogame = marioplayer(500, 335)
    movingenemy = []
    for i in range(4):
        enemy1 = enemies(random.randint(100,800), random.randint(50,150), random.randint(-5,5), random.randint(-5,5))
        movingenemy += [enemy1]

    #life
    global life
    life = 3

    run = True

    # loop that keeps the window active
    while run:
        
        # to delimit the movement of the frames
        clock.tick(FPS)

        # background image
        background = pygame.image.load(level1_screen)
        screen1.blit(background, (0, 0))

        # backbutton
        buttonfont = pygame.font.Font("./images/mariofont.ttf", 40)
        backbutton = buttonfont.render("back", 0, (255, 255, 255))
        screen1.blit(backbutton, (20, 600))

        # name, level, time, life on screen
        labelfont = pygame.font.Font("./images/mariofont.ttf", 20)
        namebox_label = labelfont.render(f"{namebox}", 1, (255, 255, 255))
        screen1.blit(namebox_label, (50, 20))
        level1_label = labelfont.render(f"world", 0, (255, 255, 255))
        screen1.blit(level1_label, (310, 20))
        levelnumber = labelfont.render(f"1", 0, (255, 255, 255))
        screen1.blit(levelnumber, (340, 40))
        time_label = labelfont.render(f"time", 1, (255, 255, 255))
        screen1.blit(time_label, (570, 20))
        timenumbers = labelfont.render(f"{time}", 1, (255, 255, 255))
        screen1.blit(timenumbers, (585, 40))
        life_label = labelfont.render(f"life", 1, (255, 255, 255))
        screen1.blit(life_label, (820, 20))
        lifenumber = labelfont.render(f"x{life}", 1, (255, 255, 255))
        screen1.blit(lifenumber, (828, 40))
        score_label = labelfont.render(f"{score}", 1, (255, 255, 255))
        screen1.blit(score_label, (50, 40))

        # checks if the player clicks the back button
        for click in pygame.event.get():
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the back button
                 if mouse_x >= 20 and mouse_x <= 120:
                         if mouse_y >= 600 and mouse_y <= 628:
                             life = 3
                             menu()
                             flag = 0

        # the keys which the player can play
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mariogame.left = True
            if mariogame.x <= 0:
                pass
            else:
                mariogame.x -= player_vel 
        if keys[pygame.K_RIGHT]:
            mariogame.left = False
            if mariogame.x + 50 + player_vel >= 1000 - 50:
                pass
            else:
                mariogame.x += player_vel
        if keys[pygame.K_DOWN]:
            if mariogame.y + 50 + player_vel >= 650 - 100:
                pass
            else:
                mariogame.y += player_vel
        if keys[pygame.K_UP]:
            if mariogame.y <= 0:
                pass
            else:
                mariogame.y -= player_vel

        # showing timer per seconds-minutes
        if secondstimer == 59:
            secondstimer = 0
            time += 1
            score += 1
        else:
            secondstimer += 1

        #characters on screen
        mariogame.draw(screen1)

        # collisions between characters
        collisions(movingenemy, mariogame)

        #move enemy
        for enemy1 in movingenemy:
            enemy1.moveenemy()
            enemy1.draw(screen1)

        #player velocity
        player_vel = 6

        # to run out if the player lose
        if life <= 0:
            run = menu()
        elif time == 60 and life >= 1:
            level2(namebox, score)
            flag = 0

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

# playing in level 2
def level2(namebox, sscore=0):

    #music for screen
    pygame.mixer.music.load("./images/tetris.mp3")
    pygame.mixer.music.play(-1,0,0)

    # importing score from the first level
    global score
    score = sscore

    # for time
    time = 0
    secondstimer = 0

    # to work with the frames (timing)
    clock = pygame.time.Clock()

    # player character class
    class marioplayer:
        def __init__(self, x, y, health = 3):
            self.x = x
            self.y = y
            self.health = health
            self.left = True
            self.cool_down_counter = 0

        # to draw the capitalist ship
        def draw(self, screen1):
            if self.left:
                screen1.blit(mario2, (self.x, self.y))
            else:
                screen1.blit(mario1, (self.x, self.y))

    # class for the enemies
    class enemies():
        def __init__(self, x, y, xspeed, yspeed):
            self.x = x
            self.y = y
            self.xspeed = xspeed
            self.yspeed = yspeed

        # moving the enemy
        def moveenemy(self):
            if self.x <=0:
                self.xspeed = random.randint(1,5)
                self.yspeed = random.randint(-5,5)
                hits.play()
            if self.x + self.xspeed +50 >= 1000:
                self.xspeed = random.randint(1,5)*-1
                self.yspeed = random.randint(-5,5)
                hits.play()
            if self.y <=0:
                self.yspeed = random.randint(1,5)
                self.xspeed = random.randint(-5,5)
                hits.play()
            if self.y + self.yspeed +50 >= 550:
                self.yspeed = random.randint(1,5)*-1
                self.xspeed = random.randint(-5,5)
                hits.play()
            else:
                self.x += self.xspeed
                self.y += self.yspeed

        # drawing the enemy on screen
        def draw(self, screen1):
            screen1.blit(greenwizard, (self.x, self.y))

    # collisions between the player and the enemies
    def collisions(hits, marioplayer):
        global life
        for i in hits:
            if marioplayer.x < i.x < marioplayer.x + 100:
                if marioplayer.y < i.y < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x +50 < marioplayer.x + 100:
                if marioplayer.y < i.y < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x < marioplayer.x + 100:
                if marioplayer.y < i.y +50 < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x +50 < marioplayer.x + 100:
                if marioplayer.y < i.y + 50 < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1

    # characters on screen
    mariogame = marioplayer(500, 335)
    movingenemy = []
    for i in range(6):
        enemy1 = enemies(random.randint(100,800), random.randint(50,150), random.randint(-5,5), random.randint(-5,5))
        movingenemy += [enemy1]

    #life
    global life
    life = 3

    # for the while 
    run = True

    # loop that keeps the window active
    while run:
        
        # to delimit the movement of the frames
        clock.tick(FPS)

        # background image
        background = pygame.image.load(level2_screen)
        screen1.blit(background, (0, 0))

        # backbutton
        buttonfont = pygame.font.Font("./images/mariofont.ttf", 40)
        backbutton = buttonfont.render("back", 0, (255, 255, 255))
        screen1.blit(backbutton, (20, 600))

        # name, level, time, life on screen
        labelfont = pygame.font.Font("./images/mariofont.ttf", 20)
        namebox_label = labelfont.render(f"{namebox}", 1, (255, 255, 255))
        screen1.blit(namebox_label, (50, 20))
        level1_label = labelfont.render(f"world", 0, (255, 255, 255))
        screen1.blit(level1_label, (310, 20))
        levelnumber = labelfont.render(f"2", 0, (255, 255, 255))
        screen1.blit(levelnumber, (340, 40))
        time_label = labelfont.render(f"time", 1, (255, 255, 255))
        screen1.blit(time_label, (570, 20))
        timenumbers = labelfont.render(f"{time}", 1, (255, 255, 255))
        screen1.blit(timenumbers, (585, 40))
        life_label = labelfont.render(f"life", 1, (255, 255, 255))
        screen1.blit(life_label, (820, 20))
        lifenumber = labelfont.render(f"x{life}", 1, (255, 255, 255))
        screen1.blit(lifenumber, (828, 40))
        score_label = labelfont.render(f"{score}", 1, (255, 255, 255))
        screen1.blit(score_label, (50, 40))

        # checks if the player clicks the back button
        for click in pygame.event.get():
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

            # to check the mouse clicks
             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the back button
                 if mouse_x >= 20 and mouse_x <= 120:
                         if mouse_y >= 600 and mouse_y <= 628:
                             life = 3
                             menu()
                             flag = 0

         #player velocity
        player_vel = 6

        # the keys which the player can play
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mariogame.left = True
            if mariogame.x <= 0:
                pass
            else:
                mariogame.x -= player_vel 
        if keys[pygame.K_RIGHT]:
            mariogame.left = False
            if mariogame.x + 50 + player_vel >= 1000 - 50:
                pass
            else:
                mariogame.x += player_vel
        if keys[pygame.K_DOWN]:
            if mariogame.y + 50 + player_vel >= 650 - 100:
                pass
            else:
                mariogame.y += player_vel
        if keys[pygame.K_UP]:
            if mariogame.y <= 0:
                pass
            else:
                mariogame.y -= player_vel

        # showing timer per seconds-minutes
        if secondstimer == 59:
            secondstimer = 0
            time += 1
            score += 3
        elif time == 60 and life >= 1:
            run = level3(namebox, score)
        else:
            secondstimer += 1

        #characters on screen
        mariogame.draw(screen1)

        # collisions between characters
        collisions(movingenemy, mariogame)

        # move enemy
        for enemy1 in movingenemy:
            enemy1.moveenemy()
            enemy1.draw(screen1)

        # to run out if the player lose
        if life <= 0:
            run = menu()

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

# screen for level 3
def level3(namebox, ssscore=0):

    pygame.mixer.music.load("./images/kirby.mp3")
    pygame.mixer.music.play(-1,0,0)

    # importing score from the first level
    global score
    score = ssscore

    # for time
    time = 0
    secondstimer = 0

    # to work with the frames (timing)
    clock = pygame.time.Clock()

    # class for the character player
    class marioplayer:
        def __init__(self, x, y, health = 3):
            self.x = x
            self.y = y
            self.health = health
            self.left = True
            #self.mario1 = mario1
            self.cool_down_counter = 0

        # to draw the capitalist ship
        def draw(self, screen1):
            if self.left:
                screen1.blit(mario2, (self.x, self.y))
            else:
                screen1.blit(mario1, (self.x, self.y))

    # class for the enemies
    class enemies():
        def __init__(self, x, y, xspeed, yspeed):
            self.x = x
            self.y = y
            self.xspeed = xspeed
            self.yspeed = yspeed

        # moving the enemies
        def moveenemy(self):
            if self.x <=0:
                self.xspeed = random.randint(1,5)
                self.yspeed = random.randint(-5,5)
                hits.play()
            if self.x + self.xspeed + 50 >= 1000:
                self.xspeed = random.randint(1,5)*-1
                self.yspeed = random.randint(-5,5)
                hits.play()
            if self.y <=0:
                self.yspeed = random.randint(1,5)
                self.xspeed = random.randint(-5,5)
                hits.play()
            if self.y + self.yspeed +50 >= 550:
                self.yspeed = random.randint(1,5)*-1
                self.xspeed = random.randint(-5,5)
                hits.play()
            else:
                self.x += self.xspeed
                self.y += self.yspeed

        # drawing the enemy on screen
        def draw(self, screen1):
            screen1.blit(browncloud, (self.x, self.y))

    # collisions between the player and the enemies
    def collisions(hits, marioplayer):
        global life
        for i in hits:
            if marioplayer.x < i.x < marioplayer.x + 100:
                if marioplayer.y < i.y < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x +50 < marioplayer.x + 100:
                if marioplayer.y < i.y < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x < marioplayer.x + 100:
                if marioplayer.y < i.y +50 < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1
            elif marioplayer.x < i.x +50 < marioplayer.x + 100:
                if marioplayer.y < i.y + 50 < marioplayer.y + 100:
                    hits.remove(i)
                    life -= 1

    # characters on screen
    mariogame = marioplayer(500, 335)
    movingenemy = []
    for i in range(10):
        enemy1 = enemies(random.randint(100,800), random.randint(50,150), random.randint(-5,5), random.randint(-5,5))
        movingenemy += [enemy1]

    #life
    global life
    life = 3

    # to run in the while
    run = True

    # loop that keeps the window active
    while run:
        
        # to delimit the movement of the frames
        clock.tick(FPS)

        # background image
        background = pygame.image.load(level2_screen)
        screen1.blit(background, (0, 0))

        # backbutton
        buttonfont = pygame.font.Font("./images/mariofont.ttf", 40)
        backbutton = buttonfont.render("back", 0, (255, 255, 255))
        screen1.blit(backbutton, (20, 600))

        # name, level, time, life on screen
        labelfont = pygame.font.Font("./images/mariofont.ttf", 20)
        namebox_label = labelfont.render(f"{namebox}", 1, (255, 255, 255))
        screen1.blit(namebox_label, (50, 20))
        level1_label = labelfont.render(f"world", 0, (255, 255, 255))
        screen1.blit(level1_label, (310, 20))
        levelnumber = labelfont.render(f"3", 0, (255, 255, 255))
        screen1.blit(levelnumber, (340, 40))
        time_label = labelfont.render(f"time", 1, (255, 255, 255))
        screen1.blit(time_label, (570, 20))
        timenumbers = labelfont.render(f"{time}", 1, (255, 255, 255))
        screen1.blit(timenumbers, (585, 40))
        life_label = labelfont.render(f"life", 1, (255, 255, 255))
        screen1.blit(life_label, (820, 20))
        lifenumber = labelfont.render(f"x{life}", 1, (255, 255, 255))
        screen1.blit(lifenumber, (828, 40))
        score_label = labelfont.render(f"{score}", 1, (255, 255, 255))
        screen1.blit(score_label, (50, 40))

        # checks if the player clicks the back button
        for click in pygame.event.get():
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

            # to read the mouse click
             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the back button
                 if mouse_x >= 20 and mouse_x <= 120:
                         if mouse_y >= 600 and mouse_y <= 628:
                             life = 3
                             menu()
                             flag = 0

        #player velocity
        player_vel = 6

        # the keys which the player can play
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mariogame.left = True
            if mariogame.x <= 0:
                pass
            else:
                mariogame.x -= player_vel 
        if keys[pygame.K_RIGHT]:
            mariogame.left = False
            if mariogame.x + 50 + player_vel >= 1000 - 50:
                pass
            else:
                mariogame.x += player_vel
        if keys[pygame.K_DOWN]:
            if mariogame.y + 50 + player_vel >= 650 - 100:
                pass
            else:
                mariogame.y += player_vel
        if keys[pygame.K_UP]:
            if mariogame.y <= 0:
                pass
            else:
                mariogame.y -= player_vel

        # showing timer per seconds-minutes
        if secondstimer == 59:
            secondstimer = 0
            time += 1
            score += 5
        elif time == 60 and life >= 1:
            run = endgame(namebox, score)
        else:
            secondstimer += 1

        #characters on screen
        mariogame.draw(screen1)

        # collisions between characters
        collisions(movingenemy, mariogame)

        #move enemy
        for enemy1 in movingenemy:
            enemy1.moveenemy()
            enemy1.draw(screen1)

        # if the player´s life is 0, the level will stop
        if life <= 0:
            run = menu()

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

# leaderboard screen
def leader_board():
    
    # loop that keeps the window active
    while True:
        
        # to delimit the movement of the frames
        clock.tick(FPS)

        # info background image
        background = pygame.image.load(mainscreen)
        screen1.blit(background, (0, 0))

        # backbutton
        buttonfont = pygame.font.Font("./images/mariofont.ttf", 40)
        backbutton = buttonfont.render("back", 0, (255,255,255))
        screen1.blit(backbutton, (20, 600))

        # checks if the player clicks the back button
        for click in pygame.event.get():
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

            # to read the mouse click
             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the back button
                 if mouse_x >= 20 and mouse_x <= 120:
                         if mouse_y >= 600 and mouse_y <= 628:
                             menu()
                             flag = 0

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

# screen for the loose or winning
def endgame(namebox, score):

    # loop that keeps the window active
    while True:
        
        # to delimit the movement of the frames
        clock.tick(FPS)

        # info background image
        background = pygame.image.load(endgamescreen)
        screen1.blit(background, (0, 0))

        # backbutton and button to open the leaderboard screen
        buttonfont = pygame.font.Font("./images/mariofont.ttf", 40)
        backbutton = buttonfont.render("back", 0, (255,255,255))
        screen1.blit(backbutton, (20, 600))
        buttonleader = pygame.font.Font("./images/mariofont.ttf", 40)
        buttonleader = buttonleader.render("leaderboard", 0, (255,255,255))
        screen1.blit(buttonleader, (700, 600))

        # name of the player and final score for the screen presentation
        labelfont = pygame.font.Font("./images/mariofont.ttf", 70)
        namebox_label = labelfont.render(f"player:", 1, (255, 255, 255))
        screen1.blit(namebox_label, (350, 160))
        namebox_label = labelfont.render(f"{namebox}", 1, (255, 255, 255))
        screen1.blit(namebox_label, (350, 220))
        score_label = labelfont.render(f"{score}", 1, (255, 255, 255))
        screen1.blit(score_label, (490, 410))
        score_label = labelfont.render(f"score:", 1, (255, 255, 255))
        screen1.blit(score_label, (490, 350))
        score_label = labelfont.render(f"MARIO WINS!", 1, (255, 255, 255))
        screen1.blit(score_label, (225, 20))

        # checks if the player clicks the back button
        for click in pygame.event.get():
             if click.type == QUIT:
                 pygame.quit()
                 sys.exit()

            # to read the mouse click
             if click.type == MOUSEBUTTONUP:
                 mouse_x, mouse_y = pygame.mouse.get_pos()

                 # get the click on the back button
                 if mouse_x >= 20 and mouse_x <= 120:
                         if mouse_y >= 600 and mouse_y <= 628:
                             menu()
                             flag = 0
                             
                 # get the click on the leaderboard button
                 if mouse_x >= 700 and mouse_x <= 980:
                     if mouse_y >= 600 and mouse_y <= 628:
                         leader_board()
                         flag = 0 

        # to make the display surface appears on the user’s monitor (changes)
        pygame.display.update()

# to start from the menu screen
menu()