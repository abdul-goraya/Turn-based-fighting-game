#Imported pygame and contants file to use their functions
import pygame
import constants


pygame.init()
#allows you to initialize the attributes (variables) of an object.


#This class is used to create a generalized input-box 
class InputBox:
    #take initail parameters
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = constants.BLACK
        self.text = text
        self.txt_surface = constants.font.render(text, True, self.color)
        self.active = False
    #detacts clicks
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #checks if userpresses any mouse button
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = constants.RED if self.active else constants.BLACK
        if event.type == pygame.KEYDOWN: #checks key-input
            if self.active:
                if event.key == pygame.K_RETURN: #detects delete key
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE: #detects backspace and removes last charachter
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode #append text into the box and creates a surface for it
                self.txt_surface = constants.font.render(self.text, True, self.color)
    #sets width
    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    #draws input box
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 2))
        pygame.draw.rect(screen, self.color, self.rect, 2)
