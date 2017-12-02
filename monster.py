import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self,name,x,y,img_file):

        pygame.sprite.Sprite.__init__(self)





        self.image = pygame.image.load(img_file).comvert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.name = name

        self.speed = 10


    def move(self):

        self.rect.x +=self.speed

    
