import sys
import pygame
import pygame.font
pygame.init()
from pygame.sprite import Sprite, Group
import time

class CreatePlayer(Sprite):
    def __init__(self, settings, xpos, ypos):
        self.screen = settings.screen
        self.screen_rect = self.screen.get_rect()
        super(CreatePlayer, self).__init__()
        self.color = (0,255,0)
        self.number_of_spaces = settings.number_of_spaces
        self.xpos = xpos
        self.ypos = ypos
        self.width = self.screen_rect.width / self.number_of_spaces
        self.height = self.screen_rect.height / self.number_of_spaces
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left = 0
        self.rect.top = 0
        
    def draw_player(self):
        self.rect.left = self.width * self.xpos
        self.rect.top = self.height * self.ypos
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def move_player(self, event, player_group, 
            player_movable_down, player_movable_up, player_movable_right, player_movable_left):
        if event.key == pygame.K_UP:
            if player_movable_up:
                self.ypos -= 1
        elif event.key == pygame.K_DOWN:
            if player_movable_down:
                self.ypos += 1
        elif event.key == pygame.K_RIGHT:
            if player_movable_right:
                self.xpos += 1
        elif event.key == pygame.K_LEFT:
            if player_movable_left:
                self.xpos -= 1

class CreateYellowBox(Sprite):
    def __init__(self, settings, player, xpos, ypos):
        self.screen = settings.screen
        self.screen_rect = self.screen.get_rect()
        self.player = player
        super(CreateYellowBox, self).__init__()
        self.color = (255,255,0)
        self.width = player.width
        self.height = player.height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.xpos = xpos
        self.ypos = ypos
        
    def draw_box(self):
        self.rect.left = self.xpos * self.width
        self.rect.top = self.ypos * self.height
        pygame.draw.rect(self.screen, self.color, self.rect)

class CreateRedBox(Sprite):
    def __init__(self, settings, player, xpos, ypos):
        self.screen = settings.screen
        self.screen_rect = self.screen.get_rect()
        self.player = player
        super(CreateRedBox, self).__init__()
        self.color = (255,0,0)
        self.width = player.width
        self.height = player.height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.xpos = xpos
        self.ypos = ypos
            
    def draw_box(self):
        self.rect.left = self.xpos * self.width
        self.rect.top = self.ypos * self.height
        pygame.draw.rect(self.screen, self.color, self.rect)

class CreateGrayBox(Sprite):
    pass

class CreateEachLine(Sprite):
    def __init__(self, screen, player, n, vertical):
        super(CreateEachLine, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = (50,50,50)
        
        if vertical:
            self.rect = pygame.Rect((player.width * n) - 1, 0, 2, self.screen_rect.height)
        else:
            self.rect = pygame.Rect(0, (player.height * n) - 1, self.screen_rect.width, 2)
        
    def draw_line(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class CreateLines():
    def __init__(self, settings, player):
        self.group = Group()
        for line in self.group:
            self.group.remove(line)
        self.screen = settings.screen
        self.screen_rect = self.screen.get_rect()
        self.number_of_spaces = settings.number_of_spaces
        
        number_of_lines_x = int(self.screen_rect.width / player.width)
        n = 0
        for line in range(self.number_of_spaces):
            line = CreateEachLine(self.screen, player, n, vertical=True)
            self.group.add(line)
            n += 1
        
        number_of_lines_y = int(self.screen_rect.height / player.height)
        n = 0
        for line in range(number_of_lines_y):
            line = CreateEachLine(self.screen, player, n, vertical=False)
            self.group.add(line)
            n += 1
    
    def draw_lines(self):
        for line in self.group:
            line.draw_line()

class Settings():
    def __init__(self):
        self.screen = pygame.display.set_mode((800,800))
        self.bg_color = (0,0,0)
        self.number_of_spaces = 2
        self.game_active = False
        self.completed = False
        
        self.level_1 = False
        self.level_1_finished = False
        self.level_1_ready = True
        self.level_2 = False
        self.level_2_finished = False
        self.level_2_ready = False
        self.level_3 = False
        self.level_3_finished = False
        self.level_3_ready = False
        self.level_4 = False
        self.level_4_finished = False
        self.level_4_ready = False
        self.level_5 = False
        self.level_5_finished = False
        self.level_5_ready = False
        self.level_6 = False
        self.level_6_finished = False
        self.level_6_ready = False
        self.level_7 = False
        self.level_7_finished = False
        self.level_7_ready = False
        self.level_8 = False
        self.level_8_finished = False
        self.level_8_ready = False
        self.level_9 = False
        self.level_9_finished = False
        self.level_9_ready = False
        self.level_10 = False
        self.level_10_finished = False
        self.level_10_ready = False
        self.level_11 = False
        self.level_11_finished = False
        self.level_11_ready = False
        self.level_12 = False
        self.level_12_finished = False
        self.level_12_ready = False

class LevelButtons():
    def __init__(self, settings):
        self.one = Words(settings, "1", bg_color=(255,0,0), font_size=50, top=400, left=50, width=50, height=50, text_color=(255,255,255), button=True)
        self.two = Words(settings, "2", bg_color=(255,0,0), font_size=50, top=400, left=150, width=50, height=50, text_color=(255,255,255), button=True)
        self.three = Words(settings, "3", bg_color=(255,0,0), font_size=50, top=400, left=250, width=50, height=50, text_color=(255,255,255), button=True)
        self.four = Words(settings, "4", bg_color=(255,0,0), font_size=50, top=400, left=350, width=50, height=50, text_color=(255,255,255), button=True)
        self.five = Words(settings, "5", bg_color=(255,0,0), font_size=50, top=400, left=450, width=50, height=50, text_color=(255,255,255), button=True)
        self.six = Words(settings, "6", bg_color=(255,0,0), font_size=50, top=400, left=550, width=50, height=50, text_color=(255,255,255), button=True)
        self.seven = Words(settings, "7", bg_color=(255,0,0), font_size=50, top=400, left=650, width=50, height=50, text_color=(255,255,255), button=True)
        self.eight = Words(settings, "8", bg_color=(255,0,0), font_size=50, top=500, left=50, width=50, height=50, text_color=(255,255,255), button=True)
        self.nine = Words(settings, "9", bg_color=(255,0,0), font_size=50, top=500, left=150, width=50, height=50, text_color=(255,255,255), button=True)
        self.ten = Words(settings, "10", bg_color=(255,0,0), font_size=50, top=500, left=250, width=50, height=50, text_color=(255,255,255), button=True)
        self.eleven = Words(settings, "11", bg_color=(255,0,0), font_size=50, top=500, left=350, width=50, height=50, text_color=(255,255,255), button=True)

class AllOtherWords():
    def __init__(self, settings):
        self.title = Words(settings, "Green vs. Red", bg_color=settings.bg_color, font_size=100, top=0, left=0, width=800, height=200, text_color=(255,255,0))
        self.title_timer = 1000
        self.rules_1 = Words(settings, "Directions:", bg_color=settings.bg_color, 
            font_size=40, top=150, left=300, width=200, height=30, text_color=(255,255,255))
        self.rules_2 = Words(settings, "Use the arrow keys to move the green box.", bg_color=settings.bg_color, 
            font_size=20, top=180, left=300, width=200, height=30, text_color=(255,255,255))
        self.rules_3 = Words(settings, "If you touch a yellow box, it will turn green.", bg_color=settings.bg_color, 
            font_size=20, top=200, left=300, width=200, height=30, text_color=(255,255,255))
        self.rules_4 = Words(settings, "Get rid of all the yellow boxes to pass the level.", bg_color=settings.bg_color, 
            font_size=20, top=220, left=300, width=200, height=30, text_color=(255,255,255))
        self.rules_5 = Words(settings, "Touch a red box and lose the level.", bg_color=settings.bg_color, 
            font_size=20, top=240, left=300, width=200, height=30, text_color=(255,255,255))
    
    def draw_all_words(self):
        self.title_timer -= 1
        if self.title_timer <= 1:
            if self.title.text_color == (0, 255, 0):
                self.title.text_color = (255, 255, 0)
                self.title.prep_msg(self.title.msg)
                self.title_timer = 1000
            elif self.title.text_color == (255, 255, 0):
                self.title.text_color = (255, 0, 0)
                self.title.prep_msg(self.title.msg)
                self.title_timer = 1000
            elif self.title.text_color == (255, 0, 0):
                self.title.text_color = (0, 255, 0)
                self.title.prep_msg(self.title.msg)
                self.title_timer = 1000
        
        self.title.draw_words()
        self.rules_1.draw_words()
        self.rules_2.draw_words()
        self.rules_3.draw_words()
        self.rules_4.draw_words()
        self.rules_5.draw_words()

class Words():
    def __init__(self, settings, msg, bg_color, font_size=20, top=0, left=0, width=200, height=50, text_color=(255,255,255), button=False):
        """initialize button attributes"""
        self.screen = settings.screen
        self.screen_rect = settings.screen.get_rect()
        self.button = button
        
        #Set the dimensions and properties of the word(s)
        self.width, self.height = width, height
        self.word_rect_color = bg_color
        self.button_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None,font_size)
        
        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.left = left
        self.rect.top = top
        
        #The button message needs to be prepped only once.
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        
        self.msg = msg
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.word_rect_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_words(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
    def draw_button(self, level_buttons, finished, ready):
        #Draw blank button and then draw message.
        if finished:
            self.button_color = (0,255,0)
        elif ready:
            self.button_color = (255,255,0)
        else:
            self.button_color = (255,0,0)
        if self.button_color != self.word_rect_color:
            self.word_rect_color = self.button_color
            self.prep_msg(self.msg)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
    def check_button(self):
        if self.button:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = self.rect.collidepoint(mouse_x, mouse_y)
            return button_clicked

def check_if_player_movable(player_group):
    player_movable_down = True
    player_movable_up = True
    player_movable_right = True
    player_movable_left = True
    for player in player_group:
        if player.ypos >= player.number_of_spaces - 1:
            player_movable_down = False
    for player in player_group:
        if player.ypos <= 0:
            player_movable_up = False
    for player in player_group:
        if player.xpos >= player.number_of_spaces - 1:
            player_movable_right = False
    for player in player_group:
        if player.xpos <= 0:
            player_movable_left = False
    
    return player_movable_down, player_movable_up, player_movable_right, player_movable_left
    
def check_for_input(player_group, yellow_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player_movable_down, player_movable_up, player_movable_right, player_movable_left = check_if_player_movable(player_group)
            for player in player_group:
                player.move_player(event, player_group, 
                    player_movable_down, player_movable_up, player_movable_right, player_movable_left)

def check_if_player_touching_yellow(settings, player_group, yellow_group):
    for player in player_group:
        for yellow in yellow_group:
            
            if player.xpos == yellow.xpos:
                if player.ypos == yellow.ypos + 1 or player.ypos == yellow.ypos - 1:
                    new_player = CreatePlayer(settings, yellow.xpos, yellow.ypos)
                    player_group.add(new_player)
                    yellow_group.remove(yellow)
            
            elif player.ypos == yellow.ypos:
                if player.xpos == yellow.xpos + 1 or player.xpos == yellow.xpos - 1:
                    new_player = CreatePlayer(settings, yellow.xpos, yellow.ypos)
                    player_group.add(new_player)
                    yellow_group.remove(yellow)

def check_if_player_touching_red(player_group, yellow_group, red_group, settings):
    for player in player_group:
        for red in red_group:
            
            if player.xpos == red.xpos:
                if player.ypos == red.ypos + 1 or player.ypos == red.ypos - 1:
                    end_game(player_group, yellow_group, red_group, settings)
            
            elif player.ypos == red.ypos:
                if player.xpos == red.xpos + 1 or player.xpos == red.xpos - 1:
                    end_game(player_group, yellow_group, red_group, settings)

def start_level_1(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 2
    
    player = CreatePlayer(settings, 0, 0)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 1, 1)
    yellow_group.add(yellow)
    
    settings.lines = CreateLines(settings, player)

def start_level_2(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 3
    
    player = CreatePlayer(settings, 2, 2)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 1, 0)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 2,0)
    red_group.add(red)
    
    settings.lines = CreateLines(settings, player)

def start_level_3(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 4
    
    player = CreatePlayer(settings, 0, 0)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 2, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 3, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 1, 3)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 3,1)
    red_group.add(red)
    
    settings.lines = CreateLines(settings, player)

def start_level_4(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 5
    
    player = CreatePlayer(settings, 4, 2)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 1, 2)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 2)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 4)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 4, 4)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 3, 3)
    red_group.add(red)
    
    settings.lines = CreateLines(settings, player)

def start_level_5(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 4
    
    player = CreatePlayer(settings, 0, 0)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 3, 3)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 2)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 2, 0)
    red_group.add(red)
    red = CreateRedBox(settings, player, 3, 0)
    red_group.add(red)
    red = CreateRedBox(settings, player, 3, 1)
    red_group.add(red)
    red = CreateRedBox(settings, player, 0, 3)
    red_group.add(red)

    settings.lines = CreateLines(settings, player)

def start_level_6(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 8
    
    player = CreatePlayer(settings, 0, 0)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 0, 2)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 0, 7)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 6, 3)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 4, 0)
    red_group.add(red)
    red = CreateRedBox(settings, player, 3, 1)
    red_group.add(red)
    red = CreateRedBox(settings, player, 4, 2)
    red_group.add(red)
    red = CreateRedBox(settings, player, 5, 2)
    red_group.add(red)
    red = CreateRedBox(settings, player, 0, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 7, 6)
    red_group.add(red)
    red = CreateRedBox(settings, player, 4, 7)
    red_group.add(red)
    red = CreateRedBox(settings, player, 5, 7)
    red_group.add(red)
    red = CreateRedBox(settings, player, 6, 7)
    red_group.add(red)


    settings.lines = CreateLines(settings, player)

def start_level_7(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 6
    
    player = CreatePlayer(settings, 0, 1)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 1, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 3, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 4, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 5, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 5, 2)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 3, 4)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 4, 5)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 4, 2)
    red_group.add(red)
    red = CreateRedBox(settings, player, 5, 3)
    red_group.add(red)
    red = CreateRedBox(settings, player, 0, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 0, 5)
    red_group.add(red)
    red = CreateRedBox(settings, player, 1, 5)
    red_group.add(red)

    settings.lines = CreateLines(settings, player)

def start_level_8(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 10
    
    player = CreatePlayer(settings, 0, 0)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 2, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 4, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 6, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 8, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 1, 3)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 3)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 7, 3)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 8, 3)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 5, 6)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 1, 8)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 3, 8)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 4, 3)
    red_group.add(red)
    red = CreateRedBox(settings, player, 5, 3)
    red_group.add(red)
    red = CreateRedBox(settings, player, 4, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 5, 4)
    red_group.add(red)

    settings.lines = CreateLines(settings, player)

def start_level_9(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 6
    
    player = CreatePlayer(settings, 0, 2)
    player_group.add(player)
    player = CreatePlayer(settings, 4, 2)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 3, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 5, 1)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 3, 3)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 5, 4)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 0, 0)
    red_group.add(red)
    red = CreateRedBox(settings, player, 1, 0)
    red_group.add(red)
    red = CreateRedBox(settings, player, 2, 1)
    red_group.add(red)
    red = CreateRedBox(settings, player, 0, 5)
    red_group.add(red)
    red = CreateRedBox(settings, player, 2, 5)
    red_group.add(red)

    settings.lines = CreateLines(settings, player)

def start_level_10(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 12
    
    player = CreatePlayer(settings, 9, 2)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 0, 0)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 0, 8)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 11, 1)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 1, 4)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 4)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 3, 6)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 5, 7)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 0, 8)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 8, 8)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 9, 8)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 0, 9)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 0, 10)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 0, 11)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 11, 11)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 10, 0)
    red_group.add(red)
    red = CreateRedBox(settings, player, 0, 2)
    red_group.add(red)
    red = CreateRedBox(settings, player, 8, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 9, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 10, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 11, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 11, 5)
    red_group.add(red)
    red = CreateRedBox(settings, player, 5, 10)
    red_group.add(red)
    red = CreateRedBox(settings, player, 8, 10)
    red_group.add(red)
    red = CreateRedBox(settings, player, 8, 11)
    red_group.add(red)

    settings.lines = CreateLines(settings, player)

def start_level_11(player_group, yellow_group, red_group, settings):
    settings.game_active = True
    settings.number_of_spaces = 20
    
    player = CreatePlayer(settings, 0, 1)
    player_group.add(player)
    player = CreatePlayer(settings, 10, 1)
    player_group.add(player)
    player = CreatePlayer(settings, 0, 11)
    player_group.add(player)
    player = CreatePlayer(settings, 10, 11)
    player_group.add(player)
    
    yellow = CreateYellowBox(settings, player, 3, 1)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 1, 2)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 11, 2)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 19, 5)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 8, 6)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 16, 9)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 9)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 11)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 1, 13)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 1, 13)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 5, 13)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 11, 13)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 11, 14)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 10, 14)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 14)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 2, 14)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 7, 14)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 6, 14)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 7, 17)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 8, 17)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 7, 18)
    yellow_group.add(yellow)
    yellow = CreateYellowBox(settings, player, 8, 18)
    yellow_group.add(yellow)
    
    red = CreateRedBox(settings, player, 12, 4)
    red_group.add(red)
    red = CreateRedBox(settings, player, 12, 5)
    red_group.add(red)
    red = CreateRedBox(settings, player, 3, 6)
    red_group.add(red)
    red = CreateRedBox(settings, player, 0, 9)
    red_group.add(red)
    red = CreateRedBox(settings, player, 7, 11)
    red_group.add(red)
    red = CreateRedBox(settings, player, 13, 11)
    red_group.add(red)
    red = CreateRedBox(settings, player, 7, 12)
    red_group.add(red)
    red = CreateRedBox(settings, player, 4, 15)
    red_group.add(red)
    red = CreateRedBox(settings, player, 9, 19)
    red_group.add(red)
    red = CreateRedBox(settings, player, 18, 19)
    red_group.add(red)

    settings.lines = CreateLines(settings, player)

def check_if_completed_level(settings, player_group, yellow_group, red_group):
    if len(yellow_group) == 0:
        settings.game_active = False
        settings.completed = True
        
        settings.screen.fill(settings.bg_color)
    
        for player in player_group:
            player.draw_player()
            
        for box in red_group:
            box.draw_box()
    
        settings.lines.draw_lines()
        pygame.display.flip()
        time.sleep(0.5)
        settings.screen.fill(settings.bg_color)
        
        for player in player_group:
            player.draw_player()
            
        for box in red_group:
            red_group.remove(box)
    
        settings.lines.draw_lines()
        pygame.display.flip()
        time.sleep(0.5)
        settings.screen.fill(settings.bg_color)
        for player in player_group:
            player_group.remove(player)
        
        if settings.level_1:
            settings.level_1 = False
            settings.level_1_finished = True
            settings.level_1_ready = False
            if not settings.level_2_finished:
                settings.level_2_finished = False
                settings.level_2_ready = True
        
        if settings.level_2:
            settings.level_2 = False
            settings.level_2_finished = True
            settings.level_2_ready = False
            if not settings.level_3_finished:
                settings.level_3_finished = False
                settings.level_3_ready = True
            
        if settings.level_3:
            settings.level_3 = False
            settings.level_3_finished = True
            settings.level_3_ready = False
            if not settings.level_4_finished:
                settings.level_4_finished = False
                settings.level_4_ready = True
                
        if settings.level_4:
            settings.level_4 = False
            settings.level_4_finished = True
            settings.level_4_ready = False
            if not settings.level_5_finished:
                settings.level_5_finished = False
                settings.level_5_ready = True
        
        if settings.level_5:
            settings.level_5 = False
            settings.level_5_finished = True
            settings.level_5_ready = False
            if not settings.level_6_finished:
                settings.level_6_finished = False
                settings.level_6_ready = True
        
        if settings.level_6:
            settings.level_6 = False
            settings.level_6_finished = True
            settings.level_6_ready = False
            if not settings.level_7_finished:
                settings.level_7_finished = False
                settings.level_7_ready = True
        
        if settings.level_7:
            settings.level_7 = False
            settings.level_7_finished = True
            settings.level_7_ready = False
            if not settings.level_8_finished:
                settings.level_8_finished = False
                settings.level_8_ready = True
        
        if settings.level_8:
            settings.level_8 = False
            settings.level_8_finished = True
            settings.level_8_ready = False
            if not settings.level_9_finished:
                settings.level_9_finished = False
                settings.level_9_ready = True
        
        if settings.level_9:
            settings.level_9 = False
            settings.level_9_finished = True
            settings.level_9_ready = False
            if not settings.level_10_finished:
                settings.level_10_finished = False
                settings.level_10_ready = True
                
        if settings.level_10:
            settings.level_10 = False
            settings.level_10_finished = True
            settings.level_10_ready = False
            if not settings.level_11_finished:
                settings.level_11_finished = False
                settings.level_11_ready = True
        
        if settings.level_11:
            settings.level_11 = False
            settings.level_11_finished = True
            settings.level_11_ready = False
            if not settings.level_12_finished:
                settings.level_12_finished = False
                settings.level_12_ready = True

def draw_buttons(settings, level_buttons):
    level_buttons.one.draw_button(level_buttons, settings.level_1_finished, settings.level_1_ready)
    level_buttons.two.draw_button(level_buttons, settings.level_2_finished, settings.level_2_ready)
    level_buttons.three.draw_button(level_buttons, settings.level_3_finished, settings.level_3_ready)
    level_buttons.four.draw_button(level_buttons, settings.level_4_finished, settings.level_4_ready)
    level_buttons.five.draw_button(level_buttons, settings.level_5_finished, settings.level_5_ready)
    level_buttons.six.draw_button(level_buttons, settings.level_6_finished, settings.level_6_ready)
    level_buttons.seven.draw_button(level_buttons, settings.level_7_finished, settings.level_7_ready)
    level_buttons.eight.draw_button(level_buttons, settings.level_8_finished, settings.level_8_ready)
    level_buttons.nine.draw_button(level_buttons, settings.level_9_finished, settings.level_9_ready)
    level_buttons.ten.draw_button(level_buttons, settings.level_10_finished, settings.level_10_ready)
    level_buttons.eleven.draw_button(level_buttons, settings.level_11_finished, settings.level_11_ready)

def check_if_button_click(level_buttons, player_group, yellow_group, red_group, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if settings.level_1_ready or settings.level_1_finished:
                if level_buttons.one.check_button():
                    settings.level_1 = True
                    start_level_1(player_group, yellow_group, red_group, settings)
            if settings.level_2_ready or settings.level_2_finished:
                if level_buttons.two.check_button():
                    settings.level_2 = True
                    start_level_2(player_group, yellow_group, red_group, settings)
            if settings.level_3_ready or settings.level_3_finished:
                if level_buttons.three.check_button():
                    settings.level_3 = True
                    start_level_3(player_group, yellow_group, red_group, settings)
            if settings.level_4_ready or settings.level_4_finished:
                if level_buttons.four.check_button():
                    settings.level_4 = True
                    start_level_4(player_group, yellow_group, red_group, settings)
            if settings.level_5_ready or settings.level_5_finished:
                if level_buttons.five.check_button():
                    settings.level_5 = True
                    start_level_5(player_group, yellow_group, red_group, settings)
            if settings.level_6_ready or settings.level_6_finished:
                if level_buttons.six.check_button():
                    settings.level_6 = True
                    start_level_6(player_group, yellow_group, red_group, settings)
            if settings.level_7_ready or settings.level_7_finished:
                if level_buttons.seven.check_button():
                    settings.level_7 = True
                    start_level_7(player_group, yellow_group, red_group, settings)
            if settings.level_8_ready or settings.level_8_finished:
                if level_buttons.eight.check_button():
                    settings.level_8 = True
                    start_level_8(player_group, yellow_group, red_group, settings)
            if settings.level_9_ready or settings.level_9_finished:
                if level_buttons.nine.check_button():
                    settings.level_9 = True
                    start_level_9(player_group, yellow_group, red_group, settings)
            if settings.level_10_ready or settings.level_10_finished:
                if level_buttons.ten.check_button():
                    settings.level_10 = True
                    start_level_10(player_group, yellow_group, red_group, settings)
            if settings.level_11_ready or settings.level_11_finished:
                if level_buttons.eleven.check_button():
                    settings.level_11 = True
                    start_level_11(player_group, yellow_group, red_group, settings)
            
def end_game(player_group, yellow_group, red_group, settings):
    settings.screen.fill(settings.bg_color)
    
    for box in yellow_group:
        box.draw_box()
    
    for player in player_group:
        player.draw_player()
            
    for box in red_group:
        box.draw_box()
    
    settings.lines.draw_lines()
    pygame.display.flip()
    time.sleep(0.5)
    settings.screen.fill(settings.bg_color)
    for box in yellow_group:
        yellow_group.remove(box)
        
    for player in player_group:
        player.draw_player()
            
    for box in red_group:
        box.draw_box()
    
    settings.lines.draw_lines()
    pygame.display.flip()
    time.sleep(0.5)
    settings.screen.fill(settings.bg_color)
    for player in player_group:
        player_group.remove(player)
        
    for box in red_group:
        box.draw_box()
    
    settings.lines.draw_lines()
    pygame.display.flip()
    time.sleep(0.5)
    settings.screen.fill(settings.bg_color)
    settings.lines.draw_lines()
    for box in red_group:
        red_group.remove(box)
    
    settings.game_active = False
    settings.level_1 = False
    settings.level_2 = False
    settings.level_3 = False

def run_game():
    settings = Settings()
    player_group = Group()
    player = CreatePlayer(settings, 0, 0)
    settings.lines = CreateLines(settings, player)
    yellow_group = Group()
    red_group = Group()
    words = AllOtherWords(settings)
    level_buttons = LevelButtons(settings)
    
    while True:
        settings.screen.fill(settings.bg_color)
        
        if settings.game_active:
            check_for_input(player_group, yellow_group)
            
            check_if_player_touching_yellow(settings, player_group, yellow_group)
            check_if_completed_level(settings, player_group, yellow_group, red_group)
            
            if not settings.completed:
                check_if_player_touching_red(player_group, yellow_group, red_group, settings)
                for player in player_group:
                    player.draw_player()
        
                for box in yellow_group:
                    box.draw_box()
            
                for box in red_group:
                    box.draw_box()
            
            settings.lines.draw_lines()
            settings.completed = False
        else:
            words.draw_all_words()
            check_if_button_click(level_buttons, player_group, yellow_group, red_group, settings)
            draw_buttons(settings, level_buttons)
        pygame.display.flip()

run_game()
