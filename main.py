import sys,time, random, math, pygame,character,music,food,button,monster
from pygame.locals import *





class Controller:

    def __init__(self, width=800, height=600):

        pygame.init()

        pygame.mixer.init()
        
        self.width=width #width of the program's window, in pixels

        self.height = height #height in pixels

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.background = pygame.Surface(self.screen.get_size()).convert()

        pygame.display.set_caption('chasing me')


        #music inicialized
        self.back_music =pygame.mixer.Sound('background.mp3')

        self.food_get_music = pygame.mixer.Sound('get_food.wav')

        self.game_over = pygame.mixer.Sound('game_over.wav')


        #frames per second to update the screen
        self.FPS = 30
        self.FPSCLCOK = pygame.time.Clock()

        

        #colors
        self.Aqua  =  (   0, 255, 255)
        self.Olive =  ( 128, 128,   0)
        self.Yellow =  ( 255, 255,   0)
        self.White =  ( 255, 0, 0)

        #self.num_food = 7 #number od foof objects in the active area

        #self.fontobj = pygame.font.Font( 'freesansbold.ttf' ,32)
        #self.textSurfaceObj = self.fontobj.render( 'Chasing me',True,self.Aqua, self.White)
        #self.caption = pygame.display.set_caption('chasing me')

         
    
        
        '''load the sprites'''
        self.button = button.Button('inside_the_button.png','outside_the_button.png',(320,400))
        self.character = character.Character('sun',70,500,'character.png')
        self.monster = monster.Monster('bear',10,500, 'monster.png')
        
        #character_X = self.character.return_xcoor()
        #valid_food_x = self.width - character_X
        self.foods=[]
        for i in range(7):

            x = random.randrange(valid_food_x,valid_food_x+100)

            y = random.randrange(180,300)

            self.foods.append(food.Food('apple',x,y,'food.png'))

        self.sprites = pygame.sprite.Group((self.character,)+(self.monster,)+tuple(self.foods))

        #variables
        self.game_end = False
        win_game = False
        game_pause = True
        self.best_score = 0
        self.score = 0
        #self.bg_music = music.Music(self.back_music)
        #self.game_end_music = music.Music(self.game_over)
        #self.get_apple_music = music.Music(self.food_get_music)
        game_round = {'1':'round_one','2':'round_two','3':'round_three','4':'round_four','5':'round_five'}
        self.current_round = 0
        self.current_time = 0
        self.start_time = 0
        #self.music_time = 0
        #replay_flag = True

        #read data
        self.fptr = open('data.txt' , 'r')
        self.best_score = self.fptr.read()
        self.fptr.close()




    def mainLoop(self):

        """The main loop of the game"""

        pygame.key.set_repeat(10)
    
        

        
        while True:

            self.background.fill(self.Yellow)
            self.button.render()
            self.button.isGameStart()
            #play the background music
            self.back_music.play(-1,0.0)
            
            
            for event in pygame.event.get():

                if event.type ==pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

                    if(event.key == pygame.K_UP):

                        self.character.move_up()

                    elif(event.key == pygame.K_DOWN):

                        self.character.move_down()

                    elif(event.key == pygame.K_LEFT):

                        self.character.move_left()

                    elif(event.key == pygame.K_RIGHT):

                        self.character.move_right()

            if self.button.isGameStart == True:

                if game_pause:

                    self.current_round +=1

                    if self.score >int(best_score):
                        best_score = score

                    fptr1 = open('data.txt','w+')
                    fptr1.write(str(best_score))
                    fptr1.close()

                    if self.current_round == 5:

                        win_game = True

                    if win_game:

                        #self.start_time = pygame.time.Clock()
                        #time_duration =
                        self.screen.fill((Aqua))
                        font1 = font.render('Game win!',True,self.Yellow)
                        obj1 = pygame.display.get_surface()
                        obj1.blit(font1,(330,200))

                        font2 = font.render('Best score:',True,self.Yellow)
                        obj2 = pygame.display.get_surface()
                        obj2.blit(font2,(370,300))

                        font3 = font.render(str(best_score),True,self.Yellow)
                        obj3 = pygame.display.get_surface()
                        obj3.blit(font3,(400,340))

                        font4 = font.render('Your score:', True, self.Yellow)
                        obj4 = pygame.display.set_surface()
                        obj4.blit(font4,(300,380))

                        font5 = font.render(str(score),True, self.Yellow)
                        obj5 = pygame.display.set_surface()
                        obj5.blit(font5,(420,480))

                        pygame.display.update()
                        self.FPSLOCK.tick(self.FPS)

                        pygame.quit()
                        sys.exit()

                    start_time = time.clock()
                    time_duration = time.clock()-start_time

                    while time_duration <3:

                        self.screen.fill((self.Yellow))
                        font6 = font.render(game_round[self.current_round],True,self.Yellow)
                        obj6 = pygame.display.set_surface()
                        obj6.blit(font6,(350,370))
                        pygame.display.update()
                        game_pause = False


                else:
                    if pygame.sprite.collide_rect(self.character,self.monster):
                        game_
                    
        


            #check for collisions

            if (pygame.sprite.collide_rect(self.character,self.monster)):

                self.character.kill()
                self.game_end = True

            for i in range(len(self.foods)):

                if (pygame.sprite.collide_rect(self.character,self.foods[i])):
                    self.foods[i].kill()
                    del self.foods[i]
                    score += 7

                    if score > self.best_score:

                        self.best_score = score

                    fptr = open('score.txt' ,'w+')
                    fptr.write(str(self.best_score))
                    fptr.close()
                               
            for i in self.foods:
                self.foods.x -=5

            if self.monster.x >500:
                game_pause = True
                self.character = 400
                self.monster = 50
          

            if not self.game_end:
                self.sprites.update()
                

            self.sprites.draw(self.screen)

            self.screen.blit(self.background,(0,0))

            pygame.display.flip()

        

def main():

    main_window = Controller()
    main_window.mainLoop()

main()

                        
                    
                
                
                
            
            
