import pygame, time

# Setup
pygame.init() # pygame works in milliseconds or FPS
pygame.display.set_caption('Hello there!')
screen = pygame.display.set_mode((640,480))

# Background
# .subsurface() creates permanently identical child Surface (.get_offset() for location in parent)
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
# Rectangle when mentioned are always pygame.Rect(x,y,width,height)
ball = pygame.Surface((50,50))
ball.fill((128,32,128))
ball.set_colorkey((128,32,128)) # All pixels this colour become transparent; also available is .set_alpha(0-255) for full image transparency

# {line width always optional} **pygame.draw** includes .rect(Surface, colour, Rect), .polygon(~, ~~, pointlist), .ellispe(~, ~~, Rect) {ovals!},
# .arc(~, ~~, Rect, init_angle, final_angle) {in radians from right}, .line(~, ~~, start_xy, end_xy), .lines(~, ~~, closed_bool, pointlist),
# .aalines (~, ~~, ~~~, ~~~~, blend_shades_bool) {anti-aliased lines}
pygame.draw.circle(ball, (255,0,0), (25,25), 25) # surface, colour, pos (from top-left), radius, linewidth (don't include for solid fill)
ball = ball.convert()
screen.blit(ball, (320-25,240-25))
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

        # Music can be added with pygame.mixer.music.load() and then commandds are expected incliding .unpause(), .fadeout(time)
        # .set_volume(0.0-1.0), .get_busy() --> bool, .set_pos() {.ogg use |seconds|, .mp3 is relative time to current pos}, .queue,
        # .set_endevent() {sends event}, .rewind()
        # Sound {}.ogg/.wav} is similar, but created with pygame.mixer.Sound(file) and lacks timeset and busy controls, but includes
        # .get_length() and .get_num_channels() {# of repeats}
        elif event.type == pygame.KEYDOWN: # Keypress
            if event.key == pygame.K_ESCAPE: # Key type constant returns an integer assigned to the key
                running = False
            elif event.key == pygame.K_i:
                    # Load a picture
                    # Import os and use os.path.join("folder", "file") for platform independent subfolder selection
                    # You can use subsurfaces to grab indiv. frames as segments of spritesheets
                    cutie = pygame.image.load('test_pic.png')
                    cutie = cutie.convert_alpha() # Preserves per-pixel alpha levels
                    screen.blit(cutie, (320-8, 240-8))
                    pygame.display.update()
                    pygame.time.wait(1300)

                    # **pygame.transform includes .flip(Surface,xbool,ybool), .scale(~, (width,height), dest) {or use returned value}
                    # .rotate(Surface, CCW degrees), .rotozoom(~, CCW degrees, int multiplier), .scale2x(~, dest) {best for solid colours}
                    # .smoothscale(~, (width,height), dest) .chop(~, Rect), .average_surfaces(~, dest) {creates surface of
                    # avg colours from all surfaces}, .average_color(~, optional Rect)
                    cutie = pygame.transform.flip(cutie, True, False) # Flip x/y bool
                    screen.blit(cutie, (320-8, 240-8))
                    pygame.display.update()
                    pygame.time.wait(400)

                    screen.blit(ball, (320-25, 240-25))
                    pygame.display.update()
            elif event.key == pygame.K_t:
                # Loads text
                # To start, assign pygame.font.SysFont(nameOfASystemFont or None, heightOfFontInVerticalPixels, optionalBoldbool, optionalItalicsbool) 
                # or pygame.font.Font(fontFileLocation, height) {use pygame.font.match_font(fontname) to get it and .getfonts() for a list of all options}
                # Then: fontvar.render(text[]2 byte unicode allowed], antialiasbool, textcolour, optionalBGcolour)
                # Also available is .size(text) {can be used before redndering to get req. size box}, .set_underline/bold/italic(bool) or .get_~/~~/~~~,
                # .get_linesize() {height of text, recommended space between lines}
                pygame.font.init()
                text = pygame.font.SysFont(None, 20, True)
                yeet = text.render('You called?', True, (0,255,0))
                yeet = yeet.convert_alpha()
                
                screen.blit(yeet, (320-45,240+32))
                pygame.display.update()
                pygame.time.wait(2000)
                
                # Consider packaging basic commands like this into a function that can be modified with params
                screen.blit(background, (0,0))
                screen.blit(ball, (320-25,240-25))
                pygame.display.update()
                
            elif event.key == pygame.K_RETURN:
                for q in range(5):
                    # Move ball to corner, then back
                    # Movement can be tied to frames (see .tick()) or to delta-time
                    screen.blit(background, (0,0)) # You can also clean the screen by calculating the dirty area as a subsurface
                    screen.blit(ball, (0,0))
                    pygame.display.update()
                    pygame.time.wait(500)

                    screen.blit(background, (0,0))
                    screen.blit(ball, (320-25,240-25))
                    pygame.display.update()
                    pygame.time.wait(500)
            
            elif event.key == pygame.K_s:
                # Sprites, check pygame.examples.testsprite.__file__
                pass
            else:
                j = j+chr(event.key)
                i+=1
        elif i>10:
            print j
            print '{:.3f}'.format(playtime/1000.0)
            i=0
            j=''
        
