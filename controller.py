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
        self.screen = pygame.display.set_mode(800, 800)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.button = pygame.Rect(350, 50, 100, 100)
        self.type = pygame.font.Font("times.ttf", 60)
        self.text = pygame.font.Font.render("Start", True, (255, 0, 0))
        self.file = open("highscores.json", "r")
        self.currentState = "Start"
        self.obstacles = []
        #set up score
        for i in range(5):
            x = random.randrange(50, 600)
            y = random.randrange(60, 700)
            self.obstacles.append(obstacle.Obstacle((x, y), 'rock-576685_640.png' ))
        self.enemies = []
        for i in range(3)
            if i == 0:
                x = 725
                y = 100
            elif i == 1:
                x = 75
                y = 700
            else:
                x = 725
                y = 700
            self.enemies.append(enemy.Enemy((x,y), 10, "enemy.png"))
        self.Mycharacter = Mycharacter.Mycharacter((75, 100))
        self.mysprites = pygame.sprite.Group((self.Mycharacter,) + tuple(self.enemies) + tuple(self.obstacles))
        self.mysprites2 = pygame.spriteGroup(tuple(self.enemies) + tuple(self.obstacles))
        self.score = 0
        #load sprites




    def mainLoop(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            if self.currentState == "start":
                self.startGame(self)
            elif self.currentstate == "running":
                self.runGame(self)
            elif self.currentstate == "end"
                self.endGame(self)


    def startGame():
        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT
                    retrn False
                if event.type == pygame.MOUSEBUTTONDOWN
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button.collidepoint(mouse_pos):
                        self.runGame(self)
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 0), self.button)
            self.screen.blit(self.text, (350,50))
            pygame.display.flip()


    def runGame(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                #is this where you implement a seperate window to appear for the highscore
                #and a seperate file that holds onto that information to be read into and written over
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
        self.score += 1
        if self.score > 400:
            if self.score > 800:
                if self.score > 1200:
                    self.enemy.speed(16)
                else:
                    self.enemy.speed(14)
            else:
                self.enemy.speed(12)

        self.enemies.update()
        self.obstacles.update()
        for i in range(len(self.obstacles)):
            if(pygame.sprite.collide_rect(self.Mycharacter, self.obstacle[i])):
                self.Mycharacter.kill()
                self.currentState = "end"
                pygame.quit
        for i in range(len(self.enemies)):
            if(pygame.sprite.collide_rect(self.Mycharacter, self.enemies[i])):
                self.Mycharacter.kill()
                self.currentState = "end"
                pygame.quit

        #if statement for time and enemey getting faster

        self.screen.fill(GREEN)
        #self.obstacles.draw(self.screen)
        #self.enemies.draw(self.screen)
        self.screen.blit(self.background, (0, 0))
        self.mysprites.draw()
        #self.screen.blit(self.Mycharacter,(self.Mycharacter.rect.x, self.Mycharacter.rect.y))
                #drawing code
                #update screen with what has been drawn
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()







    def endGame(self):
        #self.screen = pygame.display.set_mode(800, 800)
        #self.background = pygame.Surface(self.screen.get_size()).convert()
        line = json.load(self.file.readline())
        num = line["one"]
        self.file.close()
        if self.seconds > num:
            self.file = open("highscores.json", "w")
            newstr = "highscore:"+str(num)
            jsonstr = json.dump(newstr)
            self.file.write(newstr)
            self.file.close
        self.screen.fill((0, 0, 255))
        #create text and rect to blit onto screen to display high score
        self.




    #set up new screen to display high score and their score
    #use json file



    def main():
        the_game = Controller()
        the_game.mainLoop()

    main()
