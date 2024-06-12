#Imported pygame and other files to use their functions
import pygame
import constants
import level_gui
import button
import lbloaddata

pygame.init()
# allows you to initialize the attributes (variables) of an object

#Function controlling main game loop

def main(username,points,bg,main_character,enemy,reward):
    screen=constants.screen
    users=lbloaddata.Leaderboardloaddata('users.txt')
    clock = pygame.time.Clock()
    game_won=False
    game_over=False
    current_fighter = 1
    action_cooldown = 0
    action_wait_time = 90
    attack = False
    potion = False
    potion_effect = main_character.max_hp//2
    screen.blit(bg, (0, 0))
    #Victory text
    victory_text = constants.font.render("Victory! Press 'back' button to exit realm.", True, constants.RED)
    #Defeat text
    defeat_text = constants.font.render("Defeat! Press 'back' button to exit realm.", True, constants.RED)
    running=True
    #Staring the loop
    while running:    
        #loading the background
        screen.blit(constants.ui_bg_image, (0, 400))
        #Exit button to come back to main menu
        exit_button =button.Button(constants.RED, 590,10)
        exit_text = constants.font.render("Back", True, constants.BLACK)
        #Attack button to attack enemy
        attack_button=button.Button(constants.PURPLE, 10,500)
        attack_text=constants.font.render("Attack", True, constants.BLACK)
        #Heal button to heal your charachter
        heal_button=button.Button(constants.TEAL, 10,550)
        heal_text=constants.font.render("Heal", True, constants.BLACK)
        #To represent total number of potions
        potions_text = constants.font.render(f"Potions: {main_character.potions}", True, constants.BLACK)
        #To represent the health of both charachters
        main_health_text = constants.font.render(f"Health: {main_character.hp}/{main_character.max_hp}", True, constants.BLACK)
        enemy_health_text = constants.font.render(f"Health: {enemy.hp}/{enemy.max_hp}", True, constants.BLACK)
        for event in pygame.event.get():
            #If the user quits
            if event.type==pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #If the user click exit button
                if exit_button.handle_event(event):
                    #and the game is over and user has won it
                    if game_over and game_won:
                        #Points will be updated
                        users.update(username,reward)
                        running = False
                        level_gui.main(username,points+reward)
                        return
                    else:
                        level_gui.main(username,points)
                        pygame.quit()
                        running = False
                        return
                elif attack_button.handle_event(event): #handle attack
                    attack=True
                elif heal_button.handle_event(event): #handle heal
                    potion=True
        enemy.update() #updates enemy
        main_character.update() #upadtes charachter
        main_character.draw(bg,enemy)
        exit_button.draw_button() #draw exit button
        attack_button.draw_button() #draw attack button
        heal_button.draw_button() #draw heal button
        if game_over and game_won:
            #to display victory text if user won
            screen.blit(victory_text, (10, 20)) 
        if game_over and not game_won:
            #to display defeat text if user loses
            screen.blit(defeat_text,(10,20))
        #to display different texts on the screen
        screen.blit(exit_text, (660, 13))
        screen.blit(heal_text, (80, 555))
        screen.blit(attack_text, (70, 505))
        screen.blit(potions_text, (20, 460))
        screen.blit(main_health_text, (20, 410))
        screen.blit(enemy_health_text, (500, 410))
        if game_over==False:
            if main_character.alive: #if charachter is alive
                if current_fighter==1:
                    action_cooldown+=1
                    if action_cooldown >= action_wait_time:
                        if attack == True:#to attack enemy
                            main_character.attack(enemy)
                            current_fighter += 1
                            action_cooldown = 0 
                            attack=False
                        if potion==True:#to heal
                            if main_character.potions > 0:
                                if main_character.max_hp - main_character.hp > potion_effect:
                                    heal_amount = potion_effect
                                else:
                                    heal_amount = main_character.max_hp - main_character.hp
                                main_character.hp += heal_amount #heals charachter
                                main_character.potions -= 1 #decrease potion count
                                current_fighter += 1
                                action_cooldown = 0
                                potion=False
                if current_fighter == 2:
                    if enemy.alive == True: #if enemy is alive
                        action_cooldown += 1
                        if action_cooldown >= action_wait_time:
                            if (enemy.hp / enemy.max_hp) < 0.5 and enemy.potions > 0: #take damage
                                if enemy.max_hp - enemy.hp > potion_effect:
                                    heal_amount = potion_effect
                                else:
                                    heal_amount = enemy.max_hp - enemy.hp
                                enemy.hp += heal_amount #heals charachter
                                enemy.potions -= 1#decrease potion count
                                current_fighter -= 1 
                                action_cooldown = 0
                            else:
                                enemy.attack(main_character)
                                current_fighter -= 1
                                action_cooldown = 0

            #checks if user won or not
            if main_character.alive==False:
                game_over=True
                game_won=False 
            if enemy.alive==False:
                game_over=True
                game_won=True
                     
                
                
        pygame.display.flip()
        clock.tick(30) #controls fps    