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
x
y

title
subtitle
ins_list
length
button_font
button_text
number_button
"""

# This function loads in the title and subtitle as needed.
# title_text: bool: determines whether the title will be shown or not
# subtitle_text: str: the text for the optional subtitle, not provided if a subtitle is not needed
def load_title(title_text, *subtitle_text):
    # Generate title
    if title_text:
        title = title_font.render('Tower of Hanoi', True, (27,13,3))
        title = title.convert_alpha()
        screen.blit(title, (134,10))
        
        try:
            subtitle = subtitle_font.render(subtitle_text[0], True, (0,0,0))
            subtitle.convert_alpha()
            screen.blit(subtitle, ((800 - subtitle_font.size(subtitle_text[0])[0]) / 2, 110))
        except IndexError:
            pass
        # End try/except
    else:
        try:
            subtitle = subtitle_font.render(subtitle_text[0], True, (0,0,0))
            subtitle.convert_alpha()
            screen.blit(subtitle, ((800 - subtitle_font.size(subtitle_text[0])[0]) / 2,10))
        except IndexError:
            pass        

# This function provides the instructions of the game to the user.
# start: bool: Determines whether the game is starting to call next method
def instructions(start):
    # Initialize the window depending on context
    pygame.display.set_caption('Tower of Hanoi')
    screen.blit(background, (0,0))
    load_title(True, 'Instructions')

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
                if button_clicked(event, (360,439), (493,552)):
                    active = False
                # End if button_clicked
            # End if event.type
        # End got event
    # End while active
    
    if start == True:
        # Begin loading game
        game_setup()
    else:
        pass # NOTE: This will return to game
     # End if start

# This function warns the user if they are about to quit the game.
def quit_warning():
    pass

# This function sets up the game and lets the user choose how many discs to play with.
def game_setup():
    # Reset display and generate title/subtitle
    screen.blit(background, (0,0))
    load_title(True, 'How many discs?')
    
    # Generate instruction text
    text = text_font.render('Select the number of discs you would like to play with.', True, (0,0,0))
    text = text.convert_alpha()
    screen.blit(text, (232,172))
    
    # Generate buttons for number selection with text
    # NOTE: gaps of 11px
    number_button = pygame.Surface((122,189))
    number_button.fill((0,0,255))
    
    for i in range(4):
        for j in range(2):
            screen.blit(number_button, (134+(i*145), 200+(j*200)))
        # End for j
    # End for i
    
    # Generate numbers within buttons
    for i in range(3,11):
        pass
        #button_text = button_font.render(str(i), True, (255,255,255))
        #button_text = button_text.convert_alpha()
        #screen.blit(button)
     # NOTE: combine this function with the one above for sanity's sake
    
    pygame.display.update()
    pygame.time.wait(3000)

if __name__ == '__main__': # Program was started directly and not called
    # Initialize pygame
    pygame.init()
    pygame.font.init()

    # Create global variables to avoid memory leak
    
    # The base display of the game
    screen = pygame.display.set_mode((800, 600))
    # Main background and colour
    background = pygame.Surface(screen.get_size())
    background.fill((241,238,223))
    # Default button and colour
    button = pygame.Surface((80,60))
    button.fill((0,0,255))
    # Lambda functions
    button_clicked = lambda event, x, y: True if event.button == 1 and event.pos[0] in range(x[0],x[1]) and \
                                         event.pos[1] in range(y[0],y[1]) else False # Returns True if left click in defined range
    
    # Various fonts
    title_font = pygame.font.SysFont('timesnewroman', 80, True)
    subtitle_font = pygame.font.SysFont('timesnewroman', 40, True, True)
    text_font = pygame.font.SysFont('timesnewroman', 15)
    button_font = pygame.font.SysFont('arial', 15, True)
    
    # Load instructions in game start mode
    instructions(True)
