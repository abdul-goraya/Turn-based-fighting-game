#Imported pygame and constants file to use their functions
import pygame
import constants
#Button class dealing with stuff related to button
class Button:
    def __init__(self,color,x,y) -> None:
        self.color=color
        self.x=x
        self.y=y
    #Draw the button
    def draw_button(self):
        pygame.draw.rect(constants.screen, constants.BLACK, (self.x-2, self.y-2, 204, 44),0,10,10,10,10,10)
        
        pygame.draw.rect(constants.screen, self.color, (self.x, self.y, 200, 40),0,10,10,10,10,10)
    #to check if the click is within the reactangular area or not?
    def handle_event(self,event):
        return self.x<=event.pos[0]<=self.x+200 and self.y<=event.pos[1]<=self.y+40