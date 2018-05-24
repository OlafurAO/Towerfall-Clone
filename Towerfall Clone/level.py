import pygame;

class Level:
    def __init__(self, game_display, screen_size):
        self.game_display = game_display;
        self.screen_size = screen_size;
        self.level_list = [];

        self.initialize_level();

    def initialize_level(self):
        ######################################################################
        #Player 1 and 3 start
        for i in range(0 ,130, 5):
            self.level_list.append([i, 120]);
            self.level_list.append([i, self.screen_size[1] - 100]);
        #Player 2 and 4 start
        for i in range(self.screen_size[0] - 130 ,self.screen_size[0], 5):
            self.level_list.append([i, 120]);
            self.level_list.append([i, self.screen_size[1] - 100]);
        ######################################################################

        ############################Borders###################################
        for i in range(0, self.screen_size[0], 5):
            self.level_list.append([i, 0]);
            self.level_list.append([i, self.screen_size[1]]);

        for i in range(0, self.screen_size[1], 5):
            self.level_list.append([0, i]);
            self.level_list.append([self.screen_size[0], i]);
        ###################################################################

        ###########################Platforms###############################
        for i in range(int(self.screen_size[0] / 4), self.screen_size[0] - int(self.screen_size[0] / 4), 5):
            self.level_list.append([i, 200]);
            self.level_list.append([i, self.screen_size[1] - 200]);

        for i in range(int(self.screen_size[0] / 8), int(self.screen_size[0] / 4), 5):
            self.level_list.append([i, self.screen_size[1] / 2]);

        for i in range(int(self.screen_size[0] - self.screen_size[0] / 4), int(self.screen_size[0] - self.screen_size[0] / 8), 5):
            self.level_list.append([i, self.screen_size[1] / 2]);
        ################################################################

    def draw_level(self):
        for i in self.level_list:
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 5, 5]);