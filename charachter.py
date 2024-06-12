#Imported pygame,reandom and constants files to use their functions
import pygame
import random
import constants

#Fighter class deals with the stuff related to charachter
class Fighter():
	#Initalizing the basic paramters of a charachter
	def __init__(self, x, y, name, max_hp, strength, potions):
		self.name = name
		self.max_hp = max_hp
		self.hp = max_hp
		self.strength = strength
		self.start_potions = potions
		self.potions = potions
		self.alive = True
		self.animation_list = []
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()
		#load idle images
		temp_list = []
		for i in range(4):
			img = pygame.image.load(f'assets/{self.name}/idle/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		#load attack images
		temp_list = []
		for i in range(4):
			img = pygame.image.load(f'assets/{self.name}/attack/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	#handle animation
	def update(self):
		animation_cooldown = 100
		#update image
		self.image = self.animation_list[self.action][self.frame_index]
		#check if enough time has passed since the last update
		if pygame.time.get_ticks() - self.update_time > animation_cooldown:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		#if the animation has run out then reset back to the start
		if self.frame_index >= len(self.animation_list[self.action]):
			if self.action == 3:
				self.frame_index = len(self.animation_list[self.action]) - 1
			else:
				self.idle()

	#set variables to idle animation
	def idle(self):
		self.action = 0
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	#deal damage to enemy
	def attack(self, target):
		rand = random.randint(-2, 2)
		damage = self.strength + rand
		target.hp -= damage
		#run enemy hurt animation also check if target has died or not
		if target.hp < 1:
			target.hp = 0
			target.alive = False
		#set variables to attack animation
		self.action = 1
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()

	#Draw images on the screen
	def draw(self,bg,other):
		constants.screen.blit(bg, (0, 0))
		constants.screen.blit(self.image, self.rect)	
		constants.screen.blit(other.image, other.rect)		