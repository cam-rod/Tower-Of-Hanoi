# Cameron Rodriguez
# June 11, 2019
# This program allows a user to play the Tower of Hanoi game.

# These modules is used for the game interface.
import pygame

"""
Data Dictionary

screen: pygame.Surface: the window container for the game
background: pygame.Surface: the background colour for the game, a light beige
title_font: pygame.font.Font: the template font for the main title
subtitle_font: pygame.font.Font: the template font for subtitles
text_font: pygame.font.Font: the template font for body text
button_font: pygame.font.Font: the template font for buttons
towers: list: the array of discs currently on 3 towers, used as stacks
selected: list: contains the currently selected disc, and the tower it was removed from
quit_game: bool: records whether the user has opted to quit the game
active: bool: determines whether pygame should continue scanning for events
event: Event: an event recorded by pygame, used for interactions with the game
x: tuple: the range of x-coordinates of a target, used by button_clicked()
y: tuple: the range of y-coordinates of a target, used by button_clicked()

title: pygame.Surface: the title of the game displayed in some menus
subtitle: pygame.Surface: the subtitle of the game displayed in some menus
ins_list: list: an array of pygame.Surface objects used to generate the instructions
button_text: pygame.Surface: the text found on buttons and discs in most of the game interface
text:: pygame.Surface: the body text displayed in some menus
number_button: pygame.Surface: the text of the buttons used to indicate the number of discs in a game
num: int: indicates the number of discs to be used in the game
tower_block: pygame.Surface: the rectangles representing towers in the main game interface
disc: pygame.Surface: the rectangles representing discs in the main game interface
successful: bool: declares if the user has successfully moved all discs to the last tower
valid: int: contains the tower a held disc will be dropped onto, or None if the move is invalid in valid_placement()
clock: Clock: used to maintain a steady framerate of 120 fps in the game
time: int: temporarily holds the output of clock.tick(120), to prevent printing to command prompt
dropped_tower: int: contains the tower a held disc will be dropped onto, or None if the move is invalid in game_mechanics()
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
            screen.blit(subtitle, ((400 - (subtitle_font.size(subtitle_text[0])[0])/2) ,10))
        except IndexError:
            pass
        # End try/except
    # End if title_text      
# End load_title

# This function provides the instructions of the game to the user.
# start: bool: Determines whether the game is starting to call next method
def instructions(start):
    global quit_game
    # Initialize the window depending on context
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
    ins_list.append(text_font.render('discs as many times as you want, until the whole stack has been moved.', True, (0,0,0)))
    ins_list.append(text_font.render('', True, (0,0,0)))
    ins_list.append(text_font.render('Good luck!', True, (0,0,0)))

    for i in range(len(ins_list)):
        # Center text on display
        ins_list[i] = ins_list[i].convert_alpha()
        screen.blit(ins_list[i], ((800-ins_list[i].get_size()[0])/2, 200+(i*18)))
    # End for i

    # Generate button
    button_text = button_font.render('OK', True, (255,255,255))
    button_text = button_text.convert_alpha()
    screen.blit(button, (360,493))
    screen.blit(button_text, (390, 514))

    pygame.display.update()

    # Scan for button click
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit button
                quit_game = True
                active = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_clicked(event, (360,439), (493,552)):
                    active = False
                # End if button_clicked()
            # End if event.type
        # End for event
    # End while active
    
    if start:
        # Begin loading game
        game_setup()
    else:
        pass # Return to game
    # End if start
# End load_instructions

# This function updates the interface based on the location of the discs
# mouse_clicked: bool: declares whether the mouse is currently holding a number
# mouse_data: list: optional; provides mouse position as tuple
def screen_update(mouse_clicked, *mouse_data):
    # Generate the background, towers, and instructions button
    screen.blit(background, (0,0))

    tower_block = pygame.Surface((40, 440))
    tower_block.fill((27,13,3))
    tower_block = tower_block.convert()
    for i in range(3):
        screen.blit(tower_block, (120+(i*260), 160))
    # End for i

    button_text = button_font.render('Instructions', True, (255,255,255))
    button_text = button_text.convert_alpha()
    screen.blit(button, (710,10))
    screen.blit(button_text, (713,31))

    # Generate the discs currently located on the towers
    for i in range(3):
        for j in range(len(towers[i])):
            disc = pygame.Surface((40+(towers[i][j]*20),25))
            disc.fill((0,100,0))
            disc = disc.convert()
            button_text = button_font.render(str(towers[i][j]), True, (255,255,255))
            button_text = button_text.convert_alpha()
            screen.blit(disc, (120+(i*260)-(towers[i][j]*10), 600-(35*(j+1)))) # Centered on tower
            screen.blit(button_text, (140+(i*260)-(button_text.get_size()[0]/2), 
                                      600+12-(35*(j+1))-(button_text.get_size()[1]/2))) # Centered
        # End for j
    # End for i

    # Generate disc currently held by mouse, if any
    if mouse_clicked:
        disc = pygame.Surface((40+(selected[0]*20),25))
        disc.fill((0,100,0))
        disc = disc.convert()
        button_text = button_font.render(str(selected[0]), True, (255,255,255))
        button_text = button_text.convert_alpha()
        screen.blit(disc, (mouse_data[0][0]-(disc.get_size()[0]/2),
                           mouse_data[0][1]-(disc.get_size()[1]/2))) # Centered on mouse
        screen.blit(button_text, (mouse_data[0][0]-(button_text.get_size()[0]/2)-15,
                                  mouse_data[0][1]-(button_text.get_size()[1]/2))) # Offset left for visibility
    # End if mouse clicked

    pygame.display.update()
# End screen_update

# This function sets up the game and lets the user choose how many discs to play with.
def game_setup():
    global towers, quit_game
    if quit_game is False: # Skip if user opts to quit game
        # Reset display and generate title/subtitle
        screen.blit(background, (0,0))
        load_title(True, 'How many discs?')
        
        # Generate instruction text
        text = text_font.render('Select the number of discs you would like to play with.', True, (0,0,0))
        text = text.convert_alpha()
        screen.blit(text, (232,172))
        
        # Generate buttons for number selection with text
        number_button = pygame.Surface((122,189))
        number_button.fill((0,0,255))
        
        for i in range(4):
            for j in range(2):
                screen.blit(number_button, (134+(i*145), 200+(j*200)))

                button_text = button_font.render(str(3+i+(j*4)), True, (255,255,255))
                button_text = button_text.convert_alpha()
                screen.blit(button_text, (195+(i*145)-(button_text.get_size()[0]/2),
                                        285+(j*200))) # Centered on each button
            # End for j
        # End for i
        
        pygame.display.update()

        # Scan for number selection
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit button
                    quit_game = True
                    active = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(4):
                        if active is not True:
                            break
                        # End if active
                        for j in range(2):
                            if button_clicked(event, (134+(i*145),255+(i*145)),
                                            (200+(j*200),388+(j*200))):
                                num = 3 + i + (j*4) # Return the number selected
                                active = False
                            # End if button_clicked()
                        # End for i
                    # End for i
                # End if event.type
            # End got event
        # End while active

        # Initialize game and interface
        if quit_game is False:
            towers[0] = [i for i in range(num, 0, -1)]
            screen_update(False)
        # End if quit_game
    # End if quit_game
# End game_setup

# This function checks if the user has successfully moved all discs to the third tower
# Returns a boolean of if the user has won
def game_won():
    successful = True
    if towers[0] == [] and towers[1] == [] and selected[0] == None: # Left/center tower and mouse are empty
        # Verify the discs are in the correct order
        for i in range(0, len(towers[2])-1):
            if towers[2][i] - 1 == towers[2][i+1]:
                continue
            else:
                successful = False
                break
            # End if towers[2][i]
        # End for i
    else:
        successful = False
    # End if towers[0]

    return successful
# End game_won

# This function checks if a disc can be dropped on a certain tower.
# coord: tuple: the x and y location of the mouse
# Returns tower the disc is placed on if valid, else None
def valid_placement(coord):
    valid = None

    # Check if disc can be placed on tower
    for i in range(3):
        # Check to see if the mouse is within 20 pixels of a tower
        if coord[0] in range(100+(i*260), 179+(i*260)) and coord[1] in range(140, 599):
            try:
                if selected[0] < towers[i][-1]: # Disc is smaller than top disc on tower
                    valid = i
                    break
                else:
                    break
                # End if selected[0]
            except IndexError: # Tower is currently empty
                valid = i
                break
            # End try/except
        # End if coord[0]
    # End for i

    return valid
# End valid_placement

# This function scans input and interprets it into game actions.
def game_mechanics():
    global towers, selected, quit_game
    time = 0.0
    clock = pygame.time.Clock() # Used to maintain framerate

    # Begin scanning
    active = True
    while active:
        for event in pygame.event.get():
            if game_won(): # User has moved all discs successfully
                active = False
                break
            else:
                time = clock.tick(120) # Update at max 120 fps
            # End if game_won()

            if event.type == pygame.QUIT: # Quit button
                quit_game = True
                active = False
            # End if event_type
            
            if selected[0] is None: # No disc currently selected
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_clicked(event, (710, 789), (10,69)): # Instructions button
                        instructions(False)
                        if quit_game is True: # Game was quit in instructions menu
                            active = False
                        else:
                            screen_update(False)
                        # End if quit_game
                    # End if button_clicked()

                    for i in range(3):
                        if towers[i] <> []:
                            # Check if the disc on top of each tower was clicked 
                            if button_clicked(event, (120+(i*260)-(towers[i][-1]*10), 160+(i*260)+(towers[i][-1]*10)),
                                                (600-(35*(len(towers[i]))), 625-(35*(len(towers[i]))))):
                                # Add to selected and pop disc from towers stack
                                selected[0] = towers[i][-1]
                                selected[1] = i
                                towers[i].pop()
                                screen_update(False)
                            # End if button_clicked
                        # End if towers[i]
                    # End for i
                # End if event.type
            else:
                if event.type == pygame.MOUSEBUTTONUP: # Disc released
                    if event.button == 1:
                        dropped_tower = valid_placement(event.pos) # Check if the disc can be placed on that tower
                        if dropped_tower is not None:
                            # Valid placement, add to tower
                            towers[dropped_tower].append(selected[0])
                            selected = [None, None]
                            screen_update(False)
                        else:
                            # Invalid placement, return to original tower
                            towers[selected[1]].append(selected[0])
                            selected = [None, None]
                            screen_update(False)
                        # End if dropped_tower
                    # End if event.button
                elif event.type == pygame.MOUSEMOTION:
                    # Update the held disc to follow the mouse
                    screen_update(True, event.pos)
                # End if event.type
            # End if selected[0]
        # End for event
    # End while active
# End game_mechanics

# This function informs the user that they have successfully completed the game.
def endgame():
    global quit_game
    # Load background and titles
    screen.blit(background, (0,0))
    load_title(True, 'You Won!')

    # Load text
    text = text_font.render('Congratulations, you beat Tower of Hanoi!', True, (0,0,0))
    text = text.convert_alpha()
    screen.blit(text, (400-(text.get_size()[0]/2), 300-(text.get_size()[1]/2)))

    # Load button
    screen.blit(button, (360,500))
    button_text = button_font.render('Goodbye!', True, (255, 255, 255))
    button_text = button_text.convert_alpha()
    screen.blit(button_text, (400-(button_text.get_size()[0]/2), 530-(button_text.get_size()[1]/2)))

    pygame.display.update()

    # Scan for closing
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit button
                quit_game = True
                active = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_clicked(event, (360, 539), (500, 559)):
                    active = False
                # End if button_pressed()
            # End if event_type
        # End for event
    # End while active
# End endgame


if __name__ == '__main__': # Program was started directly and not called by another program
    # Initialize pygame
    pygame.init()
    pygame.font.init()

    # Create global variables to avoid memory leak
    
    # The base display of the game
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tower of Hanoi')
    # Main background and colour
    background = pygame.Surface(screen.get_size())
    background.fill((241,238,223))
    background = background.convert()
    # Default button and colour
    button = pygame.Surface((80,60))
    button.fill((0,0,255))
    button = button.convert()
    # Returns True if left click in defined range
    button_clicked = lambda event, x, y: True if event.button == 1 and event.pos[0] in range(x[0],x[1]) and \
                                         event.pos[1] in range(y[0],y[1]) else False
    # Various fonts
    title_font = pygame.font.SysFont('timesnewroman', 80, True)
    subtitle_font = pygame.font.SysFont('timesnewroman', 40, True, True)
    text_font = pygame.font.SysFont('timesnewroman', 15)
    button_font = pygame.font.SysFont('arial', 15, True)
    # Towers and selected disc arrays, quit game variable
    towers = [[], [], []]
    selected = [None, None]
    quit_game = False

    # Load instructions in game start mode
    instructions(True)
    
    if quit_game is False:
        # Run main game
        game_mechanics()

        if quit_game is False:
            # End the game
            endgame()
        # End if quit_game
    # End if quit_game
