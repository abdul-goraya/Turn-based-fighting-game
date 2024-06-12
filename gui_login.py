#Imported pygame and other files to use their functions
import pygame
import constants
import inputbox
import login_logic
import button
import leaderboard
import level_gui

pygame.init()
#allows you to initialize the attributes (variables) of an object.

#This file is being use to initiate Gui and functionalities use in the login page

#Function controlling main loop

def main():
    clock = pygame.time.Clock()
    input_box1 = inputbox.InputBox(300, 250, 140, 32)
    input_box2 = inputbox.InputBox(300, 320, 140, 32)
    input_boxes = [input_box1, input_box2]
    username_label = constants.small_font.render('Username:', True, constants.BLACK) #Lable for username text-box
    password_label = constants.small_font.render('Password:', True, constants.BLACK)#Lable for password text-box
    message = ''
    #buttons
    green_button=button.Button(constants.GREEN,300,400)
    red_button=button.Button(constants.RED,300,450)
    yellow_button=button.Button(constants.YELLOW,300,500)
    current_mode = 'login'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user quits
                pygame.quit()
                return
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN: #if user press any mouse button
                if green_button.handle_event(event): #if user presses sigin in button
                    username = input_box1.text
                    password = input_box2.text
                    if current_mode == 'signup': #check sign up process
                        message = login_logic.signup(username, password)
                    else:
                        message = login_logic.login(username, password) 
                        if message[1]=="False": #checks login info
                            message = message[0]
                        else:
                            points=message[1]
                            message=message[0]
                            level_gui.main(username,points) #else proceed to levels
                            return
                elif red_button.handle_event(event): #if user presses login button
                    current_mode = 'login' if current_mode == 'signup' else 'signup'
                elif yellow_button.handle_event(event): #if user presses leaderboard button
                    message="opening leaderboard"
                    leaderboard.main() #load leaderboard
                    return
        constants.screen.blit(constants.ui_bg_image, (0, 0)) #setup background image
        constants.screen.blit(constants.logo_image, (250, -20)) #setup logo image

        # to display username and password

        for box in input_boxes: 
            box.update()
        constants.screen.blit(username_label, (300, 230))
        constants.screen.blit(password_label, (300, 300))
        for box in input_boxes:
            box.draw(constants.screen)
        if current_mode == 'signup': #Display sigin up buton
            green_button.draw_button()
            btn_text = constants.font.render('Sign up', True, constants.BLACK)
        else: #display sign in button
            green_button.draw_button()
            btn_text = constants.font.render('Sign in', True, constants.BLACK)
        leaderboard_text = constants.font.render('Leaderboard', True, constants.BLACK)
        constants.screen.blit(btn_text, (355, 401))
        red_button.draw_button() #draw red box
        yellow_button.draw_button() #draw yellow box
        #checks mode and proceed accordingly
        switch_text = constants.font.render('Go to ' + ('Login' if current_mode == 'signup' else 'Signup'), True, constants.BLACK)
        constants.screen.blit(switch_text, (330, 451))
        msg_surface = constants.small_font.render(message, True, constants.BLACK)
        constants.screen.blit(msg_surface, (10, 550))
        constants.screen.blit(leaderboard_text, (318, 505))
        pygame.display.flip()
        clock.tick(30) #fps (Frames per second) counter


if __name__ == "__main__":
    main()