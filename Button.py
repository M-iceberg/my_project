
class Button:

    def __init__(self,in_ima,out_ima,position):

        self.out_ima = pygame.image.load('ima_name').comvert_alpha()

        self.in_ima = pygame.image.load('out_ima').conert_alpha()

        self.position=position

        self.game_start = False


    def isInside(self):

        x,y = pygame.mouse.get_pos()

        self.x1,self.y1 = self.position

        self.w,self.h = self.in_ima.get_size()


        in_x = x - w/2 < x < x + w/2

        in_y = y - h/2 < y < y + h/2

        return in_x and in_y


    def render(self):

        if self.isInside():

            screen.blit(self.in_ima,(x-w/2 , y- h/2))

        else:

            screen.blit(self.out_ima,(x-w/2 , y-h/2))

    def isGameStart(self):

        if self.isInside():
            a,b,c = pygame.mouse.get_pressed()
            if a == 1:

                self.game_start = True
                pygame.mixer.music.load('backgroundmusic')
                pygame.mixer.music.play(-1,0.0)

    def get_score():

        fptr = open('score.txt' ,'r')
        best_score = fptr.read(）
        fptr.close()
        return best_score
                               
                




            
