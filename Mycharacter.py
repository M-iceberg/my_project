import pygame

import random

#model

class Mycharacter(pygame.sprite.Sprite):

    def __init__(self,coordinates,img_file):

        #initialize all the Sprite functionality

        pygame.sprite.Sprite.__init__(self)


        #The following two attributes must be called image and rect

        #pygame assumes you have intitialized these values

        #and uses them to update the screen



        #create surface object image

        self.image=pygame.image.load(img_file).convert_alpha()


        #get the rectangle for posotioning

        self.rect=self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (35,35))
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]


        #set other attributes


        self.speed=14


    #methods to move

    def move_up(self):

        self.rect.y -= self.speed

    def move_down(self):

        self.rect.y += self.speed

    def move_left(self):

        self.rect -=self.speed

    def move_right(self):

        self.rect +=self.speed



    def update(self):

        print("updating position")
