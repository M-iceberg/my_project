import pygame

class Obstacle(pygame.sprite.Sprite):
	
	
	def __init__(self, coordinates, img_fle):
		'''general function description:initialze the coordinates of the obstacle object, the image file and the 
		resolution of the picture.
		param list: (tuple)coordinates,(str)img_fle
		return:none'''
		
		pygame.sprite.Sprite.__init__(self)
		#self.rock = (coordinates[0], coordinates[1], 40, 40)
		self.image = pygame.image.load(img_fle).convert_alpha()
		#self.image = pygame.Surface((40,40))
		#self.myrock = pygame.Rect()

		self.image = pygame.transform.scale(self.image, (35,35))
		self.rect = self.image.get_rect()
		self.rect.x = coordinates[0]
		self.rect.y = coordinates[1]


	def Update(self):
		'''general function description: create a method to update the screen
		param list: none
		return:none'''
		
		
		print("obstacle updated")
