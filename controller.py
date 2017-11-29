import sys

import pygame

import random




class Controller:

    def __init__(self, width=900, height=600):

        pygame.init()

        self.width=width

        self.height = height

        in_ima_name='inside_the_botton.png'
        out_ima_name='outside_the_botton.png'



        self.screen = pygame.dispaly.set_mode((self.width, self.height),0,32)

        self.background = pygame.Surface(self.screen.get_size()).convert()

        self.time = pygame.time.Clock()

        self.button = button.Button(in_ima_name,out_ima_name,(500,500))

        self.caption = pygame.display.set_caption('chasing game')

        self.fpsclock = pygame.time.Clock()

        self.fontobj = pygame.font.Font( 'freesansbold.ttf' ,32)
        self.fptr = open('data.txt' , 'r')
        self.best_score = fptr.read()
        fptr.close()
        
        '''load the sprites'''

        self.food=[]
        for i in range(100):

            x = random.randrange(450,520)

            y = random.randrange(180,300)

            self.food.append(cat.Cat('sun',x,y,'food.png'))

        self.cat = cat.Cat('hep',60,30,'cat.png')&



    def mainLoop(self):

        Aqua =  (   0, 255, 255)

        Olive = ( 128, 128,   0)

        Yello = ( 255, 255,   0)



        current_time = pygame.time.Clock()

        while True:

            current_time = pygame.time.Clock()

            FPS=30 #frames per second setting
            score = 0

            pygame.mixer.music.load('backgroundmusic')
            pygame.mixer.music.play(-1,0.0)
            self.background = pygame.image.load('interface.png')

            pygame.display.set_caption('chasing game')

            
            for event in pygame.event.get():

                if event.type ==pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

                    if(event.key == pygame.K_UP):

                        self.cat.move_up()

                    elif(event.key == pygame.K_DOWN):

                        self.cat.move_down()

                    elif(event.key == pygame.K_LEFT):

                        self.cat.move_left()

                    elif(event.key == pygame.K_RIGHT):

                        self.cat.move_right()

        


            #check for collisions

            if pygame.sprite.collide_rect(self.cat,self.monster):

                self.cat.kill()


            if pygame.sprite.collide_rect(self.cat,self.food):

                score += 7

                if score > int(best_score):

                    best_score = score

                new_fptr = open( 'data.txt' , 'w+')

                new_fptr.write (str(best_score))

                new_fptr.close()

            if play_times ==6:

                game_end = True

                if game_end:

                    time = pygame.time.Clock()
                    time_duration = time - current_time

                    while time_duration < 5:

                        screen.fill(Yello)

                        text1 = self.fontobj.render(' You win the game',True,Green, Blue)

                        text2 = self.fontobj.render('Best score'+str(best_score), True, Green, Blue)

                        text3 = self.fontobj.render('Your score'+str(score),True,Green, Blue)

                        pygame.display.update()

                        
        

                        

                        
                    
                
                
                
            
            
