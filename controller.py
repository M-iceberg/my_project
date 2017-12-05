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
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        #self.button_image = pygame.image.load("start_button.png").convert
        self.button = pygame.Rect(300, 150, 100, 50)
        #self.button_image.get_rect()
        self.font = pygame.font.Font("Shark_Soft_Bites.TTF", 50)
        self.text = pygame.font.Font.render(self.font,"Start", True, (255, 0, 0))
        #self.score_text = pygame.font.Font.render("Highscore: "+ str())
        self.file = open("highscores.json", "r")
        self.currentState = "start"
        self.obstacles = []
        for i in range(5):
            x = random.randrange(45, 600)
            y = random.randrange(55, 625)
            self.obstacles.append(obstacle.Obstacle((x, y), 'rock.png' ))
        self.enemies = []
        for i in range(3) :
            if i == 0:
                x = 650
                y = 100
            elif i == 1:
                x = 75
                y = 650
            elif i == 2:
                x = 650
                y = 650
            self.enemies.append(enemy.Enemy((x, y), "enemy.png"))
        self.Mycharacter = Mycharacter.Mycharacter((75, 100), "head6.png")
        self.mysprites = pygame.sprite.Group((self.Mycharacter,) + tuple(self.enemies) + tuple(self.obstacles))
        self.mysprites2 = pygame.sprite.Group(tuple(self.enemies) + tuple(self.obstacles))
        self.mysprites3 = pygame.sprite.Group((self.Mycharacter,))
        self.mysprites4 = pygame.sprite.Group(tuple(self.enemies))
        self.score = 0
        self.end_time = 0
        self.start_time = 0
        self.time = (self.end_time-self.start_time) * 1000

    def mainLoop(self):
        """
        This is the main loop for the game that calls the other functions in this class
        in order to create a start screen, run the game, and present the high score and player
        score at the end of the game.
        Param list: None
        Return list: None
        """
        self.done = False
        print("got to mainloop")
        while not self.done:
            if self.currentState == "start":
                self.startGame()
            elif self.currentState == "running":
                print("running")
                self.start_time = pygame.time.get_ticks()
                self.runGame()
            elif self.currentState == "end":
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
        start = True
        clock = pygame.time.Clock
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
            self.screen.fill((255, 0, 255))
            pygame.draw.rect(self.screen, (0, 0, 0), self.button)
            self.screen.blit(self.text, (310,145))
            pygame.display.flip()
        pygame.quit

    def runGame(self):
        run = True
        pygame.key.set_repeat(1,50)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    run = False
                if event.type == pygame.KEYDOWN:
                #Under here is the game logic and i don't know if i should have the random enemy movement under here
                    if(event.key == pygame.K_UP):
                        self.Mycharacter.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.Mycharacter.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.Mycharacter.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.Mycharacter.move_right()
                """
                self.end_time = pygame.time.get_ticks()
                for g in self.mysprites4.sprites:
                    if self.time > 15:
                        g.speed(12)
                    elif self.time > 30:
                        g.speed(14)
                    elif self.time > 45:
                        g.speed(16)
                    elif self.time > 60:
                        g.speed(18)
                    elif self.time > 75:
                        g.speed(20)
                """
                self.mysprites.update()
                #self.mysprites2.group_collide
                #possibly sprite.groupcollide to save myself these two loops but I like the loops
                #also idk if the dokill means it will .kill() or something else
                if pygame.sprite.groupcollide(self.mysprites, self.mysprites3, False, True):
                    self.currentState = 'end'
                    self.end_time = pygame.time.get_ticks()
                    run = False
                """
                for i in range(len(self.obstacles)):
                    if(pygame.sprite.collide_rect(self.Mycharacter, self.obstacle[i])):
                        self.Mycharacter.kill()
                        self.currentState = "end"
                        self.end_time = pygame.time.get_ticks()
                        run = False

                for i in range(len(self.enemies)):
                    if(pygame.sprite.collide_rect(self.Mycharacter, self.enemies[i])):
                        self.Mycharacter.kill()
                        self.currentState = "end"
                        self.end_time = pygame.time.get_ticks()
                        run = False
                """

                self.screen.fill((0, 255, 0))
                #self.obstacles.draw(self.screen)
                #self.enemies.draw(self.screen)
                self.screen.blit(self.background, (0, 0))
                self.mysprites.draw(self.screen)
                #self.screen.blit(self.Mycharacter,(self.Mycharacter.rect.x, self.Mycharacter.rect.y))
                        #drawing code
                        #update screen with what has been drawn
                pygame.display.flip()
        pygame.quit

    def endGame(self):
        #self.screen = pygame.display.set_mode(800, 800)
        #self.background = pygame.Surface(self.screen.get_size()).convert()
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                    self.done = True
                else:
                    line = json.load(self.file.readline())
                    num = line["one"]
                    self.file.close()
                    if self.time > int(num):
                        self.file = open("highscores.json", "w")
                        newstr = "highscore:"+str(num)
                        jsonstr = json.dump(newstr)
                        self.file.write(newstr)
                        self.file.close
                    self.file = open("highscores.json", "r")
                    newline = json.load(self.file.readline())
                    score = newline["highscore"]
                    self.file.close()
                    self.screen.fill((0, 0, 255))
                    #create text and rect to blit onto screen to display high score
                    self.screen.blit("Highscore: " + str(score), (325, 50))
                    self.screen.blit("Your Score: " + str(num), (325, 150))
                    pygame.display.flip()
        pygame.quit


def main():
    the_game = Controller()
    the_game.mainLoop()

main()
