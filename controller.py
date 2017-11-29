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
        #may not need this image garbage if done in classes
        self.Mycharacter_image = pygame.image.load("head6.png").convert()
        self.enemy_image = pygame.image.load("enemy.png").convert()
        self.obstacle_image = pygame.image.load("rock-576685_640.png").convert()
        self.screen = pygame.display.set_mode(800, 800)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        """
        self.obstacle_list = pygame.sprite.Group()
        self.obstacle1 = Obstacle(random.randrange(50-650), random.randrange(50-650))
        self.obstacle2 = Obstacle(random.randrange(50-650), random.randrange(50-650))
        self.obstacle3 = Obstacle(random.randrange(50-650), random.randrange(50-650))
        self.obstacle_list.add(self.obstacle1)
        self.obstacle_list.add(self.obstacle2)
        self.obstacle_list.add(self.obstacle3)
        """
        self.obstacles = []
        for i in range(5):
            x = random.randrange(50, 600)
            y = random.randrange(60, 700)
            self.obstacles.append(obstacle.Obstacle((x, y), 'enemy.png' ))
        self.Mycharacter = Mycharacter((75, 100))
        self.enemy = enemy((random.randchoice('right','left','up','down'),(700,700), 6))
        self.obstacles.append(self.enemy)
        self.score = 0
        self.seconds = self.score/60
        #load sprites




    def mainLoop(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    #is this where you implement a seperate window to appear for the highscore
                    #and a seperate file that holds onto that information to be read into and written over
                if event.type == pygame.KEYDOWN:
                #Under here is the game logic and i don't know if i should have the random enemy movement under here
                    if(event.key == pygame.K_UP):
                        self.Mycharacter.recty -= 2
                    elif(event.key == pygame.K_DOWN):
                        self.Mycharacter.recty += 2
                    elif(event.key == pygame.K_LEFT):
                        self.Mycharacter.rectx -= 2
                    elif(event.key == pygame.K_RIGHT):
                        self.Mycharacter.rectx += 2
                self.score += 1
                if self.score > 400:
                    if clock > 800:
                        if clock > 1200:
                            self.enemy.speed(12)
                        else:
                            self.enemy.speed(10)
                    else:
                        self.enemy.speed(8)

            self.enemy.move()

            self.obstacles.update()
            for i in range(len(self.obstacle_list)):
                if(pygame.sprite.collide_rect(self.Mycharacter, self.obstacle[i])):
                    self.Mycharacter.kill()
                    pygame.quit()
                    endGame(self)
            #if statement for time and enemey getting faster

            screen.fill(GREEN)
            self.obstacles.draw(self.screen)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Mycharacter,(self.Mycharacter.rect.x, self.Mycharacter.rect.y))
                    #drawing code
                    #update screen with what has been drawn
            pygame.display.flip()

            clock.tick(60)
        pygame.quit()


def endGame(self):
    self.file = 
    #set up new screen to display high score and their score
    #use json file



    def main():
        the_game = Controller()
        the_game.mainLoop()

    main()
