
class Button:

    def __init__(self,in_ima,out_ima,position):

        self.out_ima = pygame.image.load('ima_name').comvert_alpha()

        self.in_ima = pygame.image.load('out_ima').conert_alpha()

        self.position=position

        #self.game_start = False


    def is_over(self):

        x,y = pygame.mouse.get_pos()

        x1,y1 = self.position

        w,h = self.in_ima.get_size()


        in_x = x - w/2 < x < x + w/2

        in_y = y - h/2 < y < y + h/2

        return in_x and in_y


    def which_ima(self):

        w,h = self.out_ima.get.size()

        x,y = self.position

        if self.is_over():

            screen.blit(self.in_ima,(x-w/2 , y- h/2))

        else:

            screen.blit(self.out_ima,(x-w/2 , y-h/2))
