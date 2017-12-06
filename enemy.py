import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, location, img_file):
        '''general function description:initialized the sprite method, the resolution of the image file, the postion and speed
        of the object
        param list: (tuple)location,(str）img_file
        return:none'''
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()

        self.image = pygame.transform.scale(self.image, (35,35))
        
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        self.speed = 10

    def speed(self, speed):
  
        '''general function description: create a method to change the speed of the enemy object
        param list:(int)speed
        return:none'''
    
        self.speed = speed


    def move(self):
        '''general function description: create a method to move the enemy object
        param list:none
        return:none'''
        
        #if the positon of the enemy is outside the valid area, update the postion to the orgin       
        if self.rect.x > 650 or self.rect.x < 0 :
            self.rect.x = 0
            self.rect.y = 0
        elif self.rect.y > 650 or self.rect.y < 0:
            self.rect.x = 0
            self.rect.y = 0
        
        #give the enemy object a ramdom position
        else:
            if random.randrange(4) == 0:
                self.rect.y -= self.speed
            elif random.randrange(4) == 1:
                self.rect.y += self.speed
            elif random.randrange(4) == 2:
                self.rect.x += self.speed
            elif random.randrange(4) == 3:
                self.rect.x -= self.speed



    def update(self):
        '''general function description: update the enemy object
        param list:none
        return:none'''
        
        self.move()
