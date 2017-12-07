import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, location, img_file):
        """
        In this init the object is being intialized as a sprite with a surface loss_image
        that gets .rect coordinates passed into it.
        Param list: location, tuple of two numbers for the coordinates and img_file is a
        string of the name of the image file.
        Return: None
        """

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()

        self.image = pygame.transform.scale(self.image, (35,35))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        self.speed = 1

    def update(self):
        """
        When the sprite group is updated this is called and this function creates
        the random movement for the enemies (Paulas) on the screen.
        Param list: None
        Return: None
        """
        #This part accounts for if the object leaves the screen and sets a new location
        #for them
        if self.rect.x > 625 or self.rect.x < 25 :
            self.rect.x = random.randrange(300)
            if self.rect.x < 150 :
                self.rect.y = random.randrange(450, 650)
            else:
                self.rect.y = random.randrange(150,650)
        elif self.rect.y > 625 or self.rect.y < 25:
            self.rect.x = random.randrange(300)
            if self.rect.x < 150 :
                self.rect.y = random.randrange(450, 650)
            else:
                self.rect.y = random.randrange(150,650)
        #This piece randomly moves the object, though I know it could be done in a for
        #loop doing it like this creates the 45 degree motion of the enemies across the
        #screen
        else:
            if random.randrange(4) == 1:
                self.rect.y -= self.speed
            elif random.randrange(4) == 2:
                self.rect.y += self.speed
            elif random.randrange(4) == 3:
                self.rect.x += self.speed
            elif random.randrange(4) == 4:
                self.rect.x -= self.speed
