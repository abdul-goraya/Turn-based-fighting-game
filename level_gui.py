#Imported pygame and other files to use their functions
import pygame
import button
import constants
import gui_login
import gameplay_gui
import charachter

pygame.init()
#allows you to initialize the attributes (variables) of pygame object.
#main gui logic of level ui
def main(username,points):
    exit_button=button.Button(constants.RED,570,100) #exit button
    buttonslst=[button.Button(constants.BLUE,30,100), #level buttons listed
                button.Button(constants.BLUE,30,200),
                button.Button(constants.BLUE,30,300),
                button.Button(constants.BLUE,30,400),
                button.Button(constants.BLUE,30,500)]
    clock = pygame.time.Clock()
    message = ""
    #operations on health,streangth and potions of user
    health=int((30+points)/2)
    strength=int((20+points)/5)
    potions=int((20+points)//10)
    usertxt1 = constants.font.render(f"Username: {username}   Points: {points}", True, constants.BLACK)#render username and points
    usertxt2 = constants.font.render(f"Damage: {strength}+/-2   Health: {health}   Potions: {potions}",True,constants.BLACK)#render damaege and health
    while True:
        constants.screen.blit(constants.ui_bg_image, (0, 0)) #background images
        constants.screen.blit(usertxt1, (10, 10)) #display username and points
        constants.screen.blit(usertxt2, (10, 40))#display strength and health
        for lvl_button in buttonslst:
            lvl_button.draw_button()#draw level buttons
        exit_button.draw_button()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #if user exits
                pygame.quit()
                exit()    
            if event.type==pygame.MOUSEBUTTONDOWN: #checks userpress any mouse button
                #if user trys to access level 1
                if buttonslst[0].handle_event(event):
                    message="Loading level 1..."
                    #check if points are valid
                    if points>=0:
                        #renders level1
                        gameplay_gui.main(username,points,constants.bg5,charachter.Fighter(200,300,'main character',health,strength,potions),charachter.Fighter(550, 280, 'mushroom', 10, 5, potions//2),10)
                        return
                    else:
                        message = "Points too low for level"
                #if user trys to access level 2
                elif buttonslst[1].handle_event(event):
                    message="Loading level 2..."
                    #check if points are more than 10
                    if points>=10:
                        #renders level2
                        gameplay_gui.main(username,points,constants.bg1,charachter.Fighter(200,280,'main character',health,strength,potions),charachter.Fighter(550, 270, 'goblin', 25, 7, potions//2),20)
                        return
                    else:
                        message = "Points too low for level"
                #if user trys to access level 3
                elif buttonslst[2].handle_event(event):
                    message="Loading level 3..."
                    #check if points are more than 30
                    if points>=30:
                        #renders level3
                        gameplay_gui.main(username,points,constants.bg3,charachter.Fighter(200,290,'main character',health,strength,potions),charachter.Fighter(550, 270, 'skeleton', 40, 10, potions//2),30)
                        return
                    else:
                        message = "Points too low for level"
                #if user trys to access level 4
                elif buttonslst[3].handle_event(event):
                    message="Loading level 4..."
                    #check if points are more than 60
                    if points>=60:
                        #renders level4
                        gameplay_gui.main(username,points,constants.bg4,charachter.Fighter(200,320,'main character',health,strength,potions),charachter.Fighter(550, 270, 'minion', 55, 15, potions//2),40)
                        return
                    else:
                        message = "Points too low for level"
                #if user trys to access level 5
                elif buttonslst[4].handle_event(event):
                    message="Loading level 5..."
                    #check if points are more than 100
                    if points>=100:
                        #renders level5
                        gameplay_gui.main(username,points,constants.bg2,charachter.Fighter(200,300,'main character',health,strength,potions),charachter.Fighter(550, 270, 'wizard', 100, 20, potions//2),50)
                        return
                    else:
                        message = "Points too low for level"
                #if user presses exit button
                elif exit_button.handle_event(event):
                    gui_login.main()
                    return
        msg_surface = constants.small_font.render(message, True, constants.BLACK)
        #Description of game
        tutorial_txt1 = constants.font.render("Brave warrior, by the decree", True, constants.BLACK) 
        tutorial_txt2 = constants.font.render("of the king, defeat all evil", True, constants.BLACK)
        tutorial_txt3 = constants.font.render("in the kingdom. Clear levels", True, constants.BLACK)
        tutorial_txt4 = constants.font.render("to gain points which grant", True, constants.BLACK)
        tutorial_txt5 = constants.font.render("extra health, potions and be", True, constants.BLACK)
        tutorial_txt6 = constants.font.render("granted access to more levels.", True, constants.BLACK)
        #level button text label instances
        lvl1txt = constants.font.render("Level 1", True, constants.BLACK)
        lvl2txt = constants.font.render("Level 2", True, constants.BLACK)
        lvl3txt = constants.font.render("Level 3", True, constants.BLACK)
        lvl4txt = constants.font.render("Level 4", True, constants.BLACK)
        lvl5txt = constants.font.render("Level 5", True, constants.BLACK)
        exittxt = constants.font.render("Exit", True, constants.BLACK)
        #rendering all text in ui
        constants.screen.blit(tutorial_txt1, (400, 270))
        constants.screen.blit(tutorial_txt2, (400, 300))
        constants.screen.blit(tutorial_txt3, (400, 330))
        constants.screen.blit(tutorial_txt4, (400, 360))
        constants.screen.blit(tutorial_txt5, (400, 390))
        constants.screen.blit(tutorial_txt6, (400, 420))
        constants.screen.blit(lvl1txt, (85, 105))
        constants.screen.blit(lvl2txt, (85, 205))
        constants.screen.blit(lvl3txt, (85, 305))
        constants.screen.blit(lvl4txt, (85, 405))
        constants.screen.blit(lvl5txt, (85, 505))
        constants.screen.blit(exittxt, (645, 105))
        constants.screen.blit(msg_surface, (10, 550))
        pygame.display.flip()
        clock.tick(30) #Control fps

if __name__=="__main__":
    main("sexy lady",10000)