import pygame

import random

#model

class Mycharacter(pygame.sprite.Sprite):

    def __init__(self,coordinates,img_file):
        '''general function description:create the rect object for the character, initialize the size and speed of the character
        param list:(tuple)coordinates,(str)img_file
        return:none'''
        
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)


        #The following two attributes must be called image and rect

        #pygame assumes you have intitialized these values

        #and uses them to update the screen



        #create surface object image
        self.image=pygame.image.load(img_file).convert_alpha()


        #get the rectangle for positioning

        self.rect=self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (35,35))
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]


        #set other attributes


        self.speed=14


    #methods to move

    def move_up(self):
        '''general function description: update the y coordinate to move upward the object
        param list:none
        return:none'''

        self.rect.y -= self.speed

    def move_down(self):
        '''general function description: update the y coordinate to move downward the object
        param list:none
        return:none'''
        
        self.rect.y += self.speed

    def move_left(self):
        '''general function description: update the x coordinate to move leftward the object
        param list:none
        return:none'''
        
        self.rect -=self.speed

    def move_right(self):
        '''general function desciption: update the x coordinate to move rightward the object
        param list:none
        return:none'''
        
        self.rect +=self.speed



    def update(self):
        '''general function description: tell the user the screen is updating
        param list:none
        return:none'''
        
        print("updating position")
