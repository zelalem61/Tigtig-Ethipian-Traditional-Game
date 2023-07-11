import sys
from globals import *
from startScreen import disp_text

selected_color = theme_colors[0][0]




def theme_screen(screen, clock, scr_width, scr_height, music_paused):

    # initialised font
    smallfont = pygame.font.Font("AbyssinicaSIL-Regular.ttf", 35)

    if not music_paused:
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.1)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((60, 90, 100))

        # using the global color which is initialized
        global selected_color

        # mouse data
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # positions of four boxes
        pos_of_boxes = [[200, 150], [scr_width-500, 150]]

        # This loop will draw the four boxes
        i = 0
        
        meda1 = True
        for xy in pos_of_boxes:
            if (mouse[0] > xy[0]) and (mouse[0] < xy[0] + 300) and (mouse[1] > xy[1]) and (mouse[1] < xy[1] + 150):
                # pygame.draw.rect(screen, theme_colors[i][0], (xy[0], xy[1], 300, 150), 0)  # rect fill
                if click[0] == 1:
                    selected_color = theme_colors[i][0]
                    print(selected_color)
                    
            # else:
            pygame.draw.rect(screen, theme_colors[i][1], (xy[0], xy[1], 300, 150), 0)   # rect fill
                    
    
            
           
            image = pygame.image.load("assets/sarmeda.jpg")
            image = pygame.transform.scale(image,(300,180))
            screen.blit(image, (200,130))
            
    # right small rect
        
            image = pygame.image.load("assets/melatameda.jpg")
            image = pygame.transform.scale(image,(300,180))
            screen.blit(image, (700,130))
            
            
            i = i+1
            
            

        # displaying the selected color
        disp_text(screen, "ሜዳ  ምረጥ", (width / 2, 450), smallfont, selected_color)

        # start
        x, y = width / 2 - 50, 500
        if (mouse[0] > x) and (mouse[0] < x + 90) and (mouse[1] > 500) and (mouse[1] < 530):
            pygame.draw.rect(screen, colors[0][1], (width / 2 - 50, 500, 90, 50), 0)
            if click[0] == 1:
                return selected_color
        else:
            pygame.draw.rect(screen, colors[0][0], (width / 2 - 50, 500, 90, 50), 0)
        text_start = smallfont.render("ጀምር", True, const.BLACK)
        screen.blit(text_start, [width / 2 - 44, 500])

        pygame.display.update()
        clock.tick(10)
