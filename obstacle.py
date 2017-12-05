import pygame

class Obstacle(pygame.sprite.Sprite):
	def __init__(self, coordinates, img_fle):
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
		print("obstacle updated")
