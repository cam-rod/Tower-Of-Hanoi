# Cameron Rodriguez
# Date
# This program allows a user to play the Tower of Hanoi game.

# These modules is used for the game interface.
import pygame

"""
Data Dictionary

screen
background
title_font
subtitle_font
text_font
active
event

title
subtitle
ins_list
length
button_font
button_text
"""

# This function provides the instructions of the game to the user.
# start: bool: Determines whether the game is starting to call next method
def instructions(start):
    # Use global variables
    global screen, background, button
    global title_font, subtitle_font, text_font, button_font

    # Initialize the window depending on context
    pygame.display.set_caption('Tower of Hanoi')
    screen.blit(background, (0,0))
    # End if start

    # Generate title and subtitle
    title = title_font.render('Tower of Hanoi', True, (27,13,3))
    title = title.convert_alpha()
    screen.blit(title, (134,10))

    subtitle = subtitle_font.render('Instructions', True, (0,0,0))
    subtitle.convert_alpha()
    screen.blit(subtitle, (298,110))

    # Generate text
    ins_list = []
    ins_list.append(text_font.render('Welcome to Tower of Hanoi!', True, (0,0,0)))
    ins_list.append(text_font.render('', True, (0,0,0)))
    ins_list.append(text_font.render('You will start with 3 to 10 discs on the leftmost tower, from the largest at', True, (0,0,0)))
    ins_list.append(text_font.render('the bottom to the smallest on top. Your goal is to move all of the discs to', True, (0,0,0)))
    ins_list.append(text_font.render('to the tower on the far right. You can only move one disc at a time, and you', True, (0,0,0)))
    ins_list.append(text_font.render('are only allowed to have smaller discs on top of larger discs. To help with', True, (0,0,0)))
    ins_list.append(text_font.render('this, discs are numbered from smallest to largest.', True, (0,0,0)))
    ins_list.append(text_font.render('', True, (0,0,0)))
    ins_list.append(text_font.render('To move discs, click and drag them from one tower to another. The disc will', True, (0,0,0)))
    ins_list.append(text_font.render('jump back to the original tower if it cannot be moved there. You can move', True, (0,0,0)))
    ins_list.append(text_font.render('discs as many time as you want, until the whole stack has been moved.', True, (0,0,0)))
    ins_list.append(text_font.render('', True, (0,0,0)))
    ins_list.append(text_font.render('Good luck!', True, (0,0,0)))

    for i in range(len(ins_list)):
        # Center text on display
        length = ins_list[i].get_size()[0]
        ins_list[i] = ins_list[i].convert_alpha()
        screen.blit(ins_list[i], ((800-length)/2, 200+(i*18)))
    # End for i

    # Generate button
    button_text = button_font.render('OK', True, (255,255,255))
    button_text = button_text.convert_alpha()
    screen.blit(button, (360,493))
    screen.blit(button_text, (390, 514))

    pygame.display.update()

    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit button
                active = False # NOTE: remove when quit function is complete
                quit_warning()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] in range(360, 439) and event.pos[1] in range(493, 552):
                        if start == True:
                            game_setup()
                        else:
                            pass # NOTE: LINKS BACK TO GAME
                        # Left click on button
                    # End if event.pos[0]
                # End if event.button
            # End if event.type
        # End got event
    # End while active

# This function warns the user if they are about to quit the game.
def quit_warning():
    pass

# This function sets up the game and lets the user choose how many discs to play with.
def game_setup():
    print 'hey hey!'

if __name__ == '__main__': # Program was started directly and not called
    # Initialize pygame
    pygame.init()
    pygame.font.init()

    # Create global variables to avoid memory leak
    screen = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800,600))
    background.fill((241,238,223))
    button = pygame.Surface((80,60))
    button.fill((0,0,255))

    title_font = pygame.font.SysFont('timesnewroman', 80, True)
    subtitle_font = pygame.font.SysFont('timesnewroman', 40, True, True)
    text_font = pygame.font.SysFont('timesnewroman', 15)
    button_font = pygame.font.SysFont('arial', 15, True)

    instructions(True)