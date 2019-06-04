import pygame, time

# Setup
pygame.init() # pygame works in milliseconds or FPS
pygame.display.set_caption('Hello there!')
screen = pygame.display.set_mode((640,480))

# Background
# .subsurface() creates permenantly identical child Surface (.get_offset() for location in parent)
# Use .get_at((x,y)) for colour of indiv. pixel
# Also available: .get_size/width/height()
background = pygame.Surface(screen.get_size())
background.fill((0,50,200))
background = background.convert()
screen.blit(background, (0,0)) # target.blit(from, pos) --> returns Rect of affected area

# pygame.display.update updates part of the screen, .flip for the whole thing
time.sleep(0.5)
pygame.display.update()

# Create a circle
ball = pygame.Surface((50,50))
ball.fill((128,32,128))
ball.set_colorkey((128,32,128)) # All pixels this colour become transparent; also available is .set_alpha(0-255) for full image transparency

pygame.draw.circle(ball, (255,0,0), (25,25), 25) # surface, colour, pos (from top-left), radius, linewidth (don't include for solid fill)
ball = ball.convert()
screen.blit(ball, (320,240))
pygame.time.wait(300)
pygame.display.update()

# Infinite loop
# **pygame.time** includes .delay() {use processor for accurate wait}, .wait() {sleep program to free processor}, .get_ticks() {since pygame.init()}
# .set_timer(eventid, milliseconds) {create _eventid_ on event every _milliseconds}

i=0
j=''
running = True
clock = pygame.time.Clock() # Setup clock.tick()
playtime = 0
while running:
    # The event handler
    # Other allowed commands include event.get(type/list of types), event.post(), event.wait(), event.event_name(integerID here)
    # event.poll {only returns one event or NOEVENT if nothing occurs}, event.peek() {boolean of event present}
    # event.set_grab()/.get_grab() for windowed app, event.set_blocked()/.get_blocked(), event.set_allowed, event.clear( /type/typelist) 
    for event in pygame.event.get(): # This is a queue
        print event
        # **event.type** includes ACTIVEEVENT (active window), KEYDOWN/KEYUP, MOUSEMOTION, MOUSEBUTTONUP/MOUSEBUTTONDOWN
        # various joystick movements, VIDEOEXPOSE (potentially visible), VIDEORESIZE, USEREVENT (user defined event)
        a = clock.tick()
        print a # Returns time since last called (add param to set framerate)
        playtime += a
        
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
            print '{:.3f}'.format(playtime/1000.0)
            i=0
            j=''
        
