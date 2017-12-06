
class Button:

    def __init__(self,in_ima,out_ima,position):
        '''general function desciption:initialize the image, the postion of the button object
        param list:(str)in_ima,(str)out_ima,(tuple)position
        return:none'''
        
        self.out_ima = pygame.image.load('ima_name').comvert_alpha()

        self.in_ima = pygame.image.load('out_ima').conert_alpha()

        self.position=position

        self.game_start = False


    def isInside(self):
        '''general function description:check whether of postion of mouse inside the button or not
        param list:none
        return:(bool)in_x and in_y'''
        
        #get the mouse position
        x,y = pygame.mouse.get_pos()

        #give the value of position tuple to the coordinates
        self.x1,self.y1 = self.position
        
        #get the size of the button image
        self.w,self.h = self.in_ima.get_size()

        #chech the position of the mouse, if satisfy the both x,y limits, return True
        in_x = x - w/2 < x < x + w/2

        in_y = y - h/2 < y < y + h/2

        return in_x and in_y


    def render(self):
        '''general function description: update the button image 
        param list:none
        return:none'''
        
        #if inside, show the inside image
        if self.isInside():

            screen.blit(self.in_ima,(x-w/2 , y- h/2))

        else:
        #show the outside image
            screen.blit(self.out_ima,(x-w/2 , y-h/2))

    def isGameStart(self):
        '''general function desciption:check if the game is start 
        param list:none
        return:none'''
        
        #if the mouse if inside the button and right click the button, game begin
        if self.isInside():
            a,b,c = pygame.mouse.get_pressed()
            if a == 1:

                self.game_start = True
                
                #when the game begin, play the background music repeatedly
                pygame.mixer.music.load('backgroundmusic')
                pygame.mixer.music.play(-1,0.0)

    #def get_score():

        #fptr = open('score.txt' ,'r')
        #best_score = fptr.read(）
        #fptr.close()
        #return best_score
                               
                




            
