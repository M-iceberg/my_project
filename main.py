import sys， time, random, math, pygame
from pygame.locals import *





class Controller:

    def __init__(self, width=800, height=600):

        pygame.init()

        self.width=width #width of the program's window, in pixels

        self.height = height #height in pixels

        self.screen = pygame.dispaly.set_mode((self.width, self.height))

        self.background = pygame.Surface(self.screen.get_size()).convert()

        self.FPS = 30 #frames per second to update the screen
        self.FPSCLCOK = pygame.time.Clock()

        self.Aqua  =  (   0, 255, 255)#colors
        self.Olive =  ( 128, 128,   0)
        self.Yellow =  ( 255, 255,   0)
        self.White =  （ 255， 0，  0）

        self.num_food = 7 #number od foof objects in the active area

        self.fontobj = pygame.font.Font( 'freesansbold.ttf' ,32)
        self.textSurfaceObj = self.fontobj.render( 'Chasing me',True, Aqua, White)
        self.caption = pygame.display.set_caption('chasing me')


        self.button = button.Button(in_ima_name,out_ima_name,(500,500))

    

   

        self.fptr = open('data.txt' , 'r')
        self.best_score = fptr.read()
        fptr.close()


        
        # load the image files
        in_ima_name='inside_the_botton.png'
        out_ima_name='outside_the_botton.png' 
        
        '''load the sprites'''

        self.character = character.Character('cat',70,500,'cat.png')
        self.monster = monster.Monster('dragon',10,500, 'dragon.png')
        character_X = self.character.right()
        valid_food_x = self.width - character_X
        self.foods=[]
        for i in range(7):

            x = random.randrange(valid_food_x,valid_food_x+100)

            y = random.randrange(180,300)

            self.foods.append(food.Food('apple',x,y,'food.png'))

        self.sprites = pygame.sprite.Group((self.character,)+(self.monster,)+tuple(self.foods))

        self.best_score = 0

    def mainLoop(self):

        """The main loop of the game"""

        pygame.key.set_repeat(10)

        
        
        while True:

            self.background.fill(self.Aqua)
            
            for event in pygame.event.get():

                if event.type ==pygame.QUIT:

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

        


            #check for collisions

            if (pygame.sprite.collide_rect(self.character,self.monster)):

                self.character.kill()
                game_end = True

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
                               
                return self.best_score

            if game_end:
                text1 = self.fontobj.render(' You win the game',True,Green, Blue)

                text2 = self.fontobj.render('Best score'+str(self.best_score), True, Green, Blue)

                text3 = self.fontobj.render('Your score'+str(score),True,Green, Blue)

                pygame.display.update()
                



            self.sprites.draw(self.screen)

            self.screen.blit(self.background,(0,0))

            self.display.flip()

        

def main():

    main_window = Controller()
    main_window.mainLoop()

main()

                        
                    
                
                
                
            
            
