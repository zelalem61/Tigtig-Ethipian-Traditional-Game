import sys
import random
from globals import *
from constants import MUTE_BUTTON_RADIUS, INFO_BUTTON_RADIUS

x = squareSide+30
positionGrid = [145, 145+x, 145+2*x, 145+3*x+250, 145+4*x+250, 145+5*x+250]

# function to render font


def text_obj(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# function to render interactive button


def button_circle(screen, butt_color, button_pos, text, text_size, text_color,
                  text_pos):
    pygame.draw.circle(screen, butt_color, button_pos, buttonRadius)
    text_surf, text_rect = text_obj(text, text_size, text_color)
    text_rect.center = text_pos
    screen.blit(text_surf, text_rect)


# function to display text


def disp_text(screen, text, center, font_and_size, color):
    text_surf, text_rect = text_obj(text, font_and_size, color)
    text_rect.center = center
    screen.blit(text_surf, text_rect)


# class of the selection box for color


class SelBox:
    def __init__(self, pid, grid_position):
        self.playerId = pid
        self.gridPos = grid_position
        self.length = squareSide + 10
        self.breadth = squareSide + 10
        self.init_gridPos = grid_position

    def move_left(self):
        if self.init_gridPos+2 >= self.gridPos > self.init_gridPos:
            self.gridPos -= 1

    def move_right(self):
        if self.init_gridPos <= self.gridPos < self.init_gridPos+2:
            self.gridPos += 1

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, (255, 255, 255),
                         (x, y, self.length, self.breadth))


# INFO
# This functions renders a in-game help


def show_info(screen, scr_width, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
       

# function for creating a start screen


def air_start(screen, clock, scr_width, scr_height, mute):

    pygame.mixer.music.load(os.path.join(auxDirectory, 'StartScreenBack.mp3'))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.1)

    # Variables set to none initially
    p1_color_select = 1     # used to store present color's
    p2_color_select = 1    # position in the matrix
    player1_color = colors[p1_color_select][1]  # Default colors of the
    player2_color = colors[p2_color_select][1]  # player paddles
    sel_p1 = SelBox(1, 0)        # Default boxes selected
    sel_p2 = SelBox(2, 3)        # for players's color
    player_1_key = False     # this is used to carry over mouse event if player 1 name box is clicked after player 2

    music_paused = False  # to check if music is playing or paused

    # player names
    player_1_name = ""
    player_2_name = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                # player 1 controls: move highlight with a and d
                elif event.key == pygame.K_a:
                    if p1_color_select > 1:
                        p1_color_select -= 1
                    sel_p1.move_left()
                elif event.key == pygame.K_d:
                    if p1_color_select < 3:
                        p1_color_select += 1
                    sel_p1.move_right()

                # player 2 controls: move highlight with left and right
                elif event.key == pygame.K_LEFT:
                    if p2_color_select > 1:
                        p2_color_select -= 1
                    sel_p2.move_left()
                elif event.key == pygame.K_RIGHT:
                    if p2_color_select < 3:
                        p2_color_select += 1
                    sel_p2.move_right()

                # selecting easy mode with 'e' button
                elif event.key == pygame.K_e:
                    if player_1_name is "":
                        player_1_name = "Player 1"
                    if player_2_name is "":
                        player_2_name = "Player 2"
                    return 1, player1_color, player2_color, mute, player_1_name, player_2_name
                # selecting hard mode with 'h' button
                elif event.key == pygame.K_h:
                    if player_1_name is "":
                        player_1_name = "Player 1"
                    if player_2_name is "":
                        player_2_name = "Player 2"
                    return 2, player1_color, player2_color, mute, player_1_name, player_2_name

        screen.fill((60, 90, 100))
        celeb_text = pygame.font.Font('AbyssinicaSIL-Regular.ttf', 70)
        large_text = pygame.font.Font('AbyssinicaSIL-Regular.ttf', 50)
        small_text = pygame.font.Font('AbyssinicaSIL-Regular.ttf', 30)
        color_x = random.randint(0, 4)
        color_y = random.randint(0, 1)
        disp_text(screen, "ጨዋታ", (scr_width / 2, 100), celeb_text, colors[color_x][color_y])

        # mute and unmute audio code
        if mute and (not music_paused):
            pygame.mixer.music.pause()
            music_paused = True
        elif (not mute) and music_paused:
            pygame.mixer.music.unpause()
            music_paused = False

        # mouse data
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # choose colors for paddle

        x_pos_rect_left = 150
        y_pos_rect_left = scr_height/2 - 70

        x_pos_rect_right = scr_width - 150 - 320
        y_pos_rect_right = scr_height/2 - 70

      

        # difficulty button 'Easy'
        if abs(mouse[0] - 200) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            button_circle(screen, colors[0][0], (200, 470), "ቀላል", large_text, (255, 255, 255),
                          (scr_width / 2 - 400, scr_height / 2 + 170))
            if click[0] == 1:
                if music_paused:
                    pygame.mixer.music.unpause()
                pygame.mixer.music.stop()
                if player_1_name is "":
                    player_1_name = "Player 1"
                if player_2_name is "":
                    player_2_name = "Player 2"
                return 1, player1_color, player2_color, mute, player_1_name, player_2_name

        else:
            button_circle(screen, colors[0][0], (200, 470), "ቀላል", small_text, (255, 255, 255),
                          (scr_width / 2 - 400, scr_height / 2 + 170))

        # difficulty button 'Hard'
        if abs(mouse[0] - 600) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            button_circle(screen, colors[4][1], (600, 470), "ከባድ", large_text, (255, 255, 255),
                          (scr_width / 2, scr_height / 2 + 170))
            if click[0] == 1:
                if music_paused:
                    pygame.mixer.music.unpause()
                pygame.mixer.music.stop()
                if player_1_name is "":
                    player_1_name = "Player 1"
                if player_2_name is "":
                    player_2_name = "Player 2"
                return 2, player1_color, player2_color, mute, player_1_name, player_2_name

        else:
            button_circle(screen, colors[4][1], (600, 470), "ከባድ", small_text, (255, 255, 255),
                          (scr_width / 2, scr_height / 2 + 170))

        # quit button
        if abs(mouse[0] - 1000) < buttonRadius and abs(mouse[1] - 470) < buttonRadius:
            button_circle(screen, colors[1][1], (1000, 470), "ውጣ", large_text, (255, 255, 255),
                          (scr_width / 2 + 400, scr_height / 2 + 170))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            button_circle(screen, colors[1][0], (1000, 470), "ውጣ", small_text, (255, 255, 255),
                          (scr_width / 2 + 400, scr_height / 2 + 170))

        # info button
        # screen.blit(info_image, (40, 20))
        if abs(mouse[0] - (40 + 32)) < INFO_BUTTON_RADIUS and abs(mouse[1] - (20 + 32)) < INFO_BUTTON_RADIUS:
            if click[0] == 1:
                show_info(screen, scr_width, clock)

        # mute status toggle using mouse
        if abs(mouse[0] - (width - 100 + 32)) < MUTE_BUTTON_RADIUS and abs(mouse[1] - (20 + 32)) < MUTE_BUTTON_RADIUS \
                and click[0] == 1:
            mute = not mute

        # displaying mute and unmute button
        if mute:
            screen.blit(mute_image, (width - 100, 20))
        else:
            screen.blit(unmute_image, (width - 100, 20))

        # # player 1 and player 2 name box dimensions
        x1, y1 = 140, 170
        x2, y2 = scr_width / 2 + 120, 170
       

        # player 2
        if (mouse[0] > x2) and (mouse[0] < x2 + 320) and (mouse[1] > y2) and (mouse[1] < y2 + 50):
            if click[0] == 1:
                ret = 0
                blink = 0
                while True:
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()

                    color_x = random.randint(0, 4)
                    color_y = random.randint(0, 1)
                    disp_text(screen, "ምትትር", (scr_width / 2, 100), celeb_text, colors[color_x][color_y])

                    # blink
                    if blink:
                        blink_ch = "|"
                        blink = 0
                    else:
                        blink_ch = ""
                        blink = 1

                    if (mouse[0] < x2) or (mouse[0] > x2 + 320) or (mouse[1] < y2) or (mouse[1] > y2 + 50):
                        if click[0] == 1:
                            ret = 1
                        if (mouse[0] > x1) and (mouse[0] < x1 + 320) and (mouse[1] > y1) and (mouse[1] < y1 + 50):
                            if click[0] == 1:
                                player_1_key = True
                    if ret:
                        break
                    for event in pygame.event.get():
                        if event.type == pygame.locals.QUIT:
                            sys.exit()
                        if event.type == pygame.locals.KEYDOWN:
                            if event.unicode.isalpha() and not (len(player_2_name) > 8):
                                player_2_name = "{0}{1}".format(player_2_name, event.unicode)
                            elif event.key == pygame.locals.K_BACKSPACE:
                                player_2_name = player_2_name[:-1]
                            elif event.key == pygame.locals.K_RETURN:
                                ret = 1
                    pygame.draw.rect(screen, const.WHITE, (x2, y2, 320, 50), 0)
                    if not (player_2_name is ""):
                        player_2_text = small_text.render("{0}{1}".format(player_2_name, blink_ch), True, const.BLACK)
                        screen.blit(player_2_text, [scr_width / 2 + 130, 180])
                    pygame.display.flip()
                    clock.tick(10)
       
        pygame.display.update()
        clock.tick(10)
