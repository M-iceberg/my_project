import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, location, img_file):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).comvert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = location[0]

        self.rect.y = location[1]

        self.speed = 10


    def move(self):
        if self.rect.x > 750 or self.rect.x < 0 :
            self.rect.x = 0
            self.rect.y = 0
        elif: self.rect.y > 750 or self.rect.y < 0:
            self.rect.x = 0
            self.rect.y = 0
        else:
            if random.choice("right","left","up","down") == "up":
                self.rect.y -= self.speed
            elif random.choice("right","left","up","down") == "down":
                self.rect.y += self.speed
            elif random.choice("right","left","up","down") == "right":
                self.rect.x += self.speed
            elif random.choice("right","left","up","down") == "left":
                self.rect.x -= self.speed



    def update(self):
        self.move(self)
