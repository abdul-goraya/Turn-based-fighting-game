#Imported pygame and other files to use their functions
import pygame
import lbloaddata
import constants
import gui_login
import button

pygame.init()
#allows you to initialize the attributes (variables) of an object.
pygame.display.set_caption("King's Brand")


#Controls main loop
def main():
    exit_button=button.Button(constants.RED, 590,10)
    scroll_y = 0
    running = True
    while running:
        users = lbloaddata.Leaderboardloaddata('users.txt')
        users.load_data()#load data from users.txt (where user's info is stored)
        user = users.leaderboard
        constants.screen.blit(constants.ui_bg_image, (0, 0))
        exit_text = constants.font.render("Back", True, constants.BLACK) #exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user exit
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:#Checks if user press mouse button
                if exit_button.handle_event(event) and event.button==1: #if user clicks back button
                    gui_login.main()
                elif event.button == 4:  # Mouse wheel up
                    scroll_y = min(scroll_y + constants.SCROLL_SPEED, 0)
                elif event.button == 5:  # Mouse wheel down
                    scroll_y = max(scroll_y - constants.SCROLL_SPEED, -(len(user) * 28))
            elif event.type == pygame.KEYDOWN: #check if user scrolls
                if event.key == pygame.K_UP:#checks if user presses up arrow
                    scroll_y = min(scroll_y + constants.SCROLL_SPEED, 0)
                elif event.key == pygame.K_DOWN: #checks if user presses down arrow
                    scroll_y = max(scroll_y - constants.SCROLL_SPEED, -(len(user) * 28 ))
        #exit button
        exit_button.draw_button()
        constants.screen.blit(exit_text, (660, 13))
        y = scroll_y+10
        username_text = constants.font.render("Username", True, constants.BLACK) #username text
        pts_text = constants.font.render("Points", True, constants.BLACK) #points text
        #Display username and points
        constants.screen.blit(username_text, (20, y)) #username heading rendered
        constants.screen.blit(pts_text, (300, y)) #points heading rendered
        y += 56 #y adjusted accordingly
        for name, points in user:#loop to render usernames and points 
            ptstext = constants.font.render(str(points), True, constants.BLACK) 
            usertext = constants.font.render(name, True, constants.BLACK)
            constants.screen.blit(usertext, (30, y))#display username
            constants.screen.blit(ptstext,(310,y))#display points
            y += 28
        pygame.display.flip()
        pygame.time.Clock().tick(30) #contorls fps
    pygame.quit()

if __name__=="__main__":
    main()