import pygame

class Obstacle(pygame.sprite.Sprite):
	def __init__(self, coordinates, img_fle):
		"""
		In here the object is intialized as a sprite object that has a surface image that is passed in
		as well as .rect coordinates that are passed in.  This class just creates a stationary object for
		the character to interact with.
		Param list: coordinates, tuple of two integers and img_file is a string for the image file
		Return: None
		"""
		pygame.sprite.Sprite.__init__(self)
		#self.rock = (coordinates[0], coordinates[1], 40, 40)
		self.image = pygame.image.load(img_fle).convert_alpha()
		#self.image = pygame.Surface((40,40))
		#self.myrock = pygame.Rect()

		self.image = pygame.transform.scale(self.image, (35,35))
		self.rect = self.image.get_rect()
		self.rect.x = coordinates[0]
		self.rect.y = coordinates[1]
