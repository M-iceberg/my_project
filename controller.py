import pygame
import time
import random
import Mycharacter
import enemy
import obstacle
import json

GREEN = (0, 255, 0)

class Controller:
    def __init__(self):
        """
        Within this init function I initialize all of the sprites used in the game, the majority
        of the pictures and text used in the start and end game screens and I set another
        values that are used later in the function.
        Param list: None
        Return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        #self.background_image = pygame.image.load("background1.jpg")
        #self.background_image = pygame.transform.scale(self.background_image, (700,700))
        self.start_pic = pygame.image.load("huntpic.png").convert_alpha()
        self.start_pic = pygame.transform.scale(self.start_pic, (300,150))
        self.button = pygame.Rect(300, 260, 100, 50)
        self.font = pygame.font.Font("Shark_Soft_Bites.TTF", 50)
        self.font_small = pygame.font.Font("Shark_Soft_Bites.TTF", 38)
        self.font_big = pygame.font.Font("Shark_Soft_Bites.TTF", 70)
        self.font_smaller = pygame.font.Font("Shark_Soft_Bites.TTF", 30)
        self.text = pygame.font.Font.render(self.font,"Start", True, (139,69,19))
        self.text2 = pygame.font.Font.render(self.font, "Hunt for the Wilderpeople: The Game", True, (139,69,19))
        self.instructions = pygame.font.Font.render(self.font_small, "Instructions: Get Rickey Baker to Uncle Hec and evade Paula", True, (138,69,19))
        self.instructions_ps = pygame.font.Font.render(self.font_smaller, "P.S.: If Ricky gets to Tupac it's minus 5 Seconds", True, (138,69,19))
        self.ricky_baker = pygame.image.load("head6.png").convert_alpha()
        self.ricky_baker = pygame.transform.scale(self.ricky_baker, (50,50))
        self.ricky_text = pygame.font.Font.render(self.font, "= Ricky Baker", True, (139,69,19))
        self.uncle_hec = pygame.image.load("uncle.png").convert_alpha()
        self.uncle_hec = pygame.transform.scale(self.uncle_hec, (50,50))
        self.uncle_text = pygame.font.Font.render(self.font, "= Uncle Hec", True, (139,69,19))
        self.paula = pygame.image.load("paula.jpg").convert_alpha()
        self.paula = pygame.transform.scale(self.paula, (50,50))
        self.paula_text = pygame.font.Font.render(self.font, "= Paula", True, (139,69,19))
        self.tupac = pygame.image.load("tupac.jpg").convert_alpha()
        self.tupac = pygame.transform.scale(self.tupac, (50,50))
        self.tupac_text = pygame.font.Font.render(self.font, "= Tupac", True, (139,69,19))
        self.file = open("highscores.json", "r")
        self.currentState = "start"
        #This is an accumulator used to create a list of obstacle objects With
        #random coordinates and different image files
        self.obstacles = []
        for i in range(22):
            y = random.randrange(100, 600)
            if y > 150 :
                x = random.randrange(25, 650)
            else:
                x = random.randrange(100, 600)
            if i < 13:
                self.obstacles.append(obstacle.Obstacle((x, y), 'rock.png' ))
            elif i == 13:
                x = 0
                y = 400
                self.obstacles.append(obstacle.Obstacle((x,y), 'tree.png'))
            else:
                self.obstacles.append(obstacle.Obstacle((x, y), 'tree.png' ))
        #An accumulator that creats a list of enemy objects with several different
        #starting coordinates and sets the image file to be passed in
        self.enemies = []
        for i in range(6) :
            if i < 3 :
                x = 50
                y = 450
            elif i < 5 :
                x = 75
                y = 600
            else:
                x = 50
                y = 250
            #elif i == 6 or i == 7 :
                #x = 150
                #y = 150
            self.enemies.append(enemy.Enemy((x, y), "paula.jpg"))
        #An accumulator to create a list of tupacs using the obstacle object where
        #they each have a specific location on the screen and the specific image file
        #is passed in
        self.tupacs = []
        for i in range (3):
            if i == 0:
                x = 75
                y = 600
            elif i == 1:
                x = 625
                y = 400
            else:
                x = 350
                y = 350
            self.tupacs.append(obstacle.Obstacle((x,y), "tupac.jpg"))
        self.Uncle = obstacle.Obstacle((650, 650), "uncle.png")
        #create uncle sprite and locate at bottom right
        self.Mycharacter = Mycharacter.Mycharacter((0, 0), "head6.png")
        self.mysprites = pygame.sprite.Group((self.Mycharacter,) + tuple(self.enemies) + tuple(self.obstacles) + (self.Uncle,) + tuple(self.tupacs))
        self.mysprites2 = pygame.sprite.Group(tuple(self.enemies) + tuple(self.obstacles))
        self.mysprites3 = pygame.sprite.Group((self.Mycharacter,))
        self.mysprites4 = pygame.sprite.Group(tuple(self.enemies))
        self.mysprites5 = pygame.sprite.Group((self.Uncle,))
        self.mysprites6 = pygame.sprite.Group(tuple(self.tupacs))
        self.score = 0
        self.collides = 0
        self.end_time = 0
        self.start_time = 0
        self.time =(self.end_time - self.start_time) // 1000
        self.loser_pic = pygame.image.load("loss_image.png").convert_alpha()
        self.loser_pic = pygame.transform.scale(self.loser_pic, (500,250))
        self.winner_pic = pygame.image.load("thumbs_up.png").convert_alpha()
        self.winner_pic = pygame.transform.scale(self.winner_pic, (300,300))


    def mainLoop(self):
        """
        This is the main loop for the game that calls the other functions in this class
        in order to create a start screen, run the game, and present the high score and player
        score at the end of the game.
        Param list: None
        Return list: None
        """
        #This is the while loop that runs the game as self.currentState is set
        #to different values in order to call different functions
        self.done = False
        while not self.done:
            if self.currentState == "start":
                self.startGame()
            elif self.currentState == "running":
                self.runGame()
            elif self.currentState == "won" or self.currentState == "lost":
                self.endGame()
        pygame.quit

    def startGame(self):
        """
        This is the function for the start of the game.  It fills the screen
        with a different color background and creates the start button that the user
        can click on to begin running the game.
        Param list: None
        Returns: None
        """
        #This while loop runs for the duration of the start screen being open and
        #used a mouse click collide to start the game
        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    start = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button.collidepoint(mouse_pos):
                        self.currentState = "running"
                        start = False
            self.screen.fill((162,205,90))
            self.screen.blit(self.start_pic, (200,15))
            pygame.draw.rect(self.screen, (189,183,107), self.button)
            self.screen.blit(self.text, (310,255))
            self.screen.blit(self.text2, (60, 180))
            self.screen.blit(self.ricky_baker, (325,330))
            self.screen.blit(self.ricky_text, (385,330))
            self.screen.blit(self.tupac, (325,400))
            self.screen.blit(self.tupac_text, (385, 400))
            self.screen.blit(self.uncle_hec, (325,460))
            self.screen.blit(self.uncle_text, (385,460))
            self.screen.blit(self.paula, (325,535))
            self.screen.blit(self.paula_text, (385,535))
            self.screen.blit(self.instructions, (10,615))
            self.screen.blit(self.instructions_ps, (125, 655))
            pygame.display.flip()
        pygame.quit

    def runGame(self):
        """
        This is the function that runs while you are actually playing the game and
        it contains all of the game logic.
        Param list: None
        Return: None
        """
        #This while loop runs for the duration of the game being played and that
        #screen being open and this while loop contains the event loop that takes
        #in the arrow key presses and if the user quits
        run = True
        pygame.key.set_repeat(1,25)
        self.start_time = pygame.time.get_ticks()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    run = False
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.Mycharacter.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.Mycharacter.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.Mycharacter.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.Mycharacter.move_right()

            self.end_time = pygame.time.get_ticks()
            #print(str((self.end_time - self.start_time)))
            self.mysprites.update()
            #This if statement accounts for if the Mycharacter object collides with either an
            #enemy or an obstacle that isn't a tupac or Uncle Hec and you "lose" the game and
            #change the current state
            if pygame.sprite.groupcollide(self.mysprites2, self.mysprites3, False, False):
                self.currentState = 'lost'
                run = False
            #This if statement accounts for the Mycharacter object colliding with the
            #Uncle obstacle object and then you "win" the game as it changes the current state
            if pygame.sprite.groupcollide(self.mysprites3, self.mysprites5, False, False):
                self.currentState = 'won'
                self.end_time = pygame.time.get_ticks()
                run = False
            #This if statement is for collisions between Mycharacter and the tupac obstacle object
            #which then causes this to act like an accumulator as the self.collides value increases
            #with each collision
            if pygame.sprite.groupcollide(self.mysprites3, self.mysprites6, False, True):
                self.collides += 1
            self.time = (self.end_time - (self.collides * 5000) - self.start_time) // 1000
            if self.time < 0 :
                self.time = 0
            self.time_text = pygame.font.Font.render(self.font, "Time: " + str(self.time), True, (139,69,19))
            self.mysprites.update()
            self.screen.fill((0, 125, 0))
            #self.screen.blit(self.background_image, (0, 0))
            self.mysprites.draw(self.screen)
            self.screen.blit(self.time_text, (550,10))
            pygame.display.flip()
        pygame.quit

    def endGame(self):
        """
        This is the function for the end of the game that displays a Game over screen with the
        highscore and your score which is either the time it took you to get to Uncle or 0
        if you got stopped before you got there.
        Param list: None
        Return: None
        """
        #while loop that runs for the duration of the screen being open and contains
        #the event loop
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                    self.done = True
                else:
                    #This portion of code reads into a json file, takes the best time in it
                    #and then compares it against the time in the most recent game to decide
                    #to either set a new best time or not
                    self.file = open("highscores.json", "r")
                    line = json.loads(self.file.readline())
                    self.num = line["highscore"]
                    self.file.close()
                    if self.time < int(self.num) and self.currentState == "won":
                        self.file = open("highscores.json", "w")
                        newdict = {"highscore": self.time}
                        jsonstr = json.dumps(newdict)
                        self.file.write(jsonstr)
                        self.file.close()

                    #except ValueError:
                        #self.file = open("highscores.json", "w")
                        #newdict = {"highscore": self.time}
                        #jsonstr = json.dumps(newdict)
                        #self.file.write(jsonstr)
                        #self.file.close()
                    self.file = open("highscores.json", "r")
                    newline = json.loads(self.file.readline())
                    self.highscore = newline["highscore"]
                    self.file.close()
                    self.screen.fill((162,205,90))
                    self.highscore_text = pygame.font.Font.render(self.font, "Best Time: "+ str(self.highscore), True, (139,69,19))
                    self.num_text = pygame.font.Font.render(self.font, "Your Time: "+ str(self.time),True , (139,69,19))
                    #This displays the end screen set up for when you lose
                    if self.currentState == 'lost':
                        self.loser_text = pygame.font.Font.render(self.font_big, "Sorry not Sorry, you Lost", True, (139,69,19))
                        self.dif_highscore_text = pygame.font.Font.render(self.font, "Best Time: " + str(self.num), True, (139,69,19))
                        self.your_score = pygame.font.Font.render(self.font, "Your Time: 0", True, (139,69,19))
                        self.screen.blit(self.your_score, (250,225))
                        self.screen.blit(self.loser_text, (98, 25))
                        self.screen.blit(self.dif_highscore_text, (250, 150))
                        self.screen.blit(self.loser_pic, (100, 300))
                    #This displays the end screen set up for when you collide with the uncle obstacle object
                    else:
                        self.thank_you_text = pygame.font.Font.render(self.font, "Congratulations, You Got To Uncle Hec", True, (139,69,19))
                        self.screen.blit(self.thank_you_text, (57, 25))
                        self.screen.blit(self.highscore_text, (250, 150))
                        self.screen.blit(self.num_text, (250, 225))
                        self.screen.blit(self.winner_pic, (200, 350))
                    pygame.display.flip()
        pygame.quit



def main():
    """
    The main is the driver code for this program so an object is created
    that is then used to call the main loop function and put the program
    into action.
    Param list: None
    Return: None
    """
    the_game = Controller()
    the_game.mainLoop()

main()
