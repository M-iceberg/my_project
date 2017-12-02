import pygame
import character
import random

chass Food(pygame.sprite.Sprite):

    def __init__(self, name, x, y, img_file):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).comvert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.name = name

        self.character = character.Character('cat',100,500,'cat.png')
        

    def appear(self):

        cat_x = self.character.right

        self.rect.x = random.randrange(800-cat_x ,800)

        self.rect.y = random.randrange(100,200)
