class Map(pygame.sprite.Sprite):

    def __init__(self,x,y):

        self.x = x

        self.y = y

        self.backgroung = pygame.image.load('background.png').convert_alpha()


    def map_update(self):

        screen,blit(self.background,(self.x,self.y))

    def setPostion(x,y):

        self.x=x
        self.y=y
