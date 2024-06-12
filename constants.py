#Imported pygame
import pygame

pygame.init()
#allows you to initialize the attributes (variables) of an object

#This file is being use to initiate game variables that are use by multiple other files
# i.e screen size etc

screen_width = 800
screen_height = 600
SCROLL_SPEED = 28
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
TEAL = (0,255,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
#Setting up logo images
logo_image = pygame.image.load("assets/King’s Bran.png")
logo_image= pygame.transform.scale_by(logo_image,3)
ui_bg_image = pygame.image.load('assets/ui_background_image.jpg')
font = pygame.font.Font("Ldfcomicsansbold-zgma.ttf", 28) #Setting up big fonts
small_font = pygame.font.Font("Ldfcomicsansbold-zgma.ttf", 18) #Setting up small fonts
screen = pygame.display.set_mode((screen_width, screen_height))
#Setting up backgroung images
bg1 = pygame.image.load('assets/bg1.png')
bg2 = pygame.image.load('assets/bg2.png')
bg3 = pygame.image.load('assets/bg3.png')
bg4 = pygame.image.load('assets/bg4.png')
bg5 = pygame.image.load('assets/bg5.png')