import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, location, img_file):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()

        self.image = pygame.transform.scale(self.image, (35,35))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        self.speed = 10

    def speed(self, speed):
        self.speed = speed


    def move(self):
        if self.rect.x > 650 or self.rect.x < 0 :
            self.rect.x = 0
            self.rect.y = 0
        elif self.rect.y > 650 or self.rect.y < 0:
            self.rect.x = 0
            self.rect.y = 0
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
        self.move()
