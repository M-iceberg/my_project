import pygame

import random

#model

class Mycharacter(pygame.sprite.Sprite):

    def __init__(self,coordinates,img_file):
        """
        This function intializes the object as a sprite and it creates a surface image for it
        as well as takes in coordinates for its .rect portion of the object and sets its speed.
        Param list: coordinates, tuple with two integers for the x and y coordinates and img_file
        is a string for the name of the image file
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]
        self.speed = 3

    def move_up(self):
        """
        This function moves the character up by the set speed.
        Param list: None
        Return: None
        """
        self.rect.y -= self.speed

    def move_down(self):
        """
        This function moves the character up by the set speed.
        Param list: None
        Return: None
        """
        self.rect.y += self.speed

    def move_left(self):
        """
        This function moves the character up by the set speed.
        Param list: None
        Return: None
        """
        self.rect.x -=self.speed

    def move_right(self):
        """
        This function moves the character up by the set speed.
        Param list: None
        Return: None
        """
        self.rect.x +=self.speed
