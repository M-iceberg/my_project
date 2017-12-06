import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self,name,x,y,img_file):
        '''general function description: initialze the sprite methods, the position of the monster object, get the image file
        param list:(str)name,(int)x,(int)y,(str)img_file
        return:none'''
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).comvert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.name = name

        self.speed = 10


    def move(self):
        '''general function description: create a method to move the monster object
        param list:none
        return:none'''
        
        self.rect.x +=self.speed

    
