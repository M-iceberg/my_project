import pygame

import random

#model

class Cat(pygame.sprite.Sprite):

    def __init__(self,name,x,y,img_file):

        #initialize all the Sprite functionality

        pygame.sprite.Sprite.__init__(self)


        #The following two attributes must be called image and rect

        #pygame assumes you have intitialized these values

        #and uses them to update the screen



        #create surface object image

        self.image=pygame.image.load(img_file).convert_alpha()


        #get the rectangle for posotioning

        self.rect=self.image.get_rect()

        self.rect.x=x

        self.rect.y=y


        #set other attributes

        self.name=name

        self.speed=20


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
        
        
        
