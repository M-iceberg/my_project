import pygame

class Obstacle(pygame.sprite.Sprite):
	def __init__(self, coordinates, img_fle):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).covert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = coordinates[0]
		self.rect.y = coordinates[1]

	def Update(self):
		print("obstacle updated")
