import pygame, time

# Setup
pygame.init()
pygame.display.set_caption('Hello there!')
screen = pygame.display.set_mode((640,480))

# Background
background = pygame.Surface(screen.get_size())
background.fill((0,50,200))
background = background.convert()
screen.blit(background, (0,0))

# pygame.display.update updates part of the screen, .flip for the whole thing
time.sleep(0.5)
pygame.display.update()

# Infinite loop
i=0
j=''
running = True
while running:
    # The event handler
    # Other allowed commands include event.get(type/list of types), event.post(), event.wait(), event.event_name(integerID here)
    # event.poll {only returns one event or NOEVENT if nothing occurs}, event.peek() {boolean of event present}
    # event.set_grab()/.get_grab() for windowed app, event.set_blocked()/.get_blocked(), event.set_allowed, event.clear( /type/typelist) 
    for event in pygame.event.get(): # This is a queue
        print event
        # **event.type** includes ACTIVEEVENT (active window), KEYDOWN/KEYUP, MOUSEMOTION, MOUSEBUTTONUP/MOUSEBUTTONDOWN
        # various joystick movements, VIDEOEXPOSE (potentially visible), VIDEORESIZE, USEREVENT (user defined event)
        
        
        if event.type == pygame.QUIT: # X button
            running = False
            
        elif event.type == pygame.KEYDOWN: # Keypress
            if event.key == pygame.K_ESCAPE: # Key type constant returns an integer assigned to the key
                running = False
            else:
                j = j+chr(event.key)
                i+=1
        elif i>10:
            print j
            i=0
            j=''
        