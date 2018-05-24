import pygame;
from bullet import Bullet;
from spritesheet import Sprite_Sheet;

class Player:
    def __init__(self, player_id, game_display, screen_size, level):
        self.player_id = player_id;
        self.game_display = game_display;
        self.screen_size = screen_size;
        self.level = level;

        self.player_moving = False;
        self.player_jumping = False;
        self.player_shooting = False;
        self.player_dead = False;

        self.jump_counter = 0;
        self.speed = 10;
        self.jump_speed = 10;

        self.bullet_list = [];

        self.initialize_position();
        self.initialize_sprite();
        self.initialize_hitboxes();

    def initialize_position(self):
        if(self.player_id == 1):
            self.location = [40, 20];
            self.direction = 'right';
        elif(self.player_id == 2):
            self.location = [self.screen_size[0] - 60, 20];
            self.direction = 'left';
        elif(self.player_id == 3):
            self.location = [40, self.screen_size[1] - 200];
            self.direction = 'right';
        elif(self.player_id == 4):
            self.location = [self.screen_size[0] - 60, self.screen_size[1] - 200];
            self.direction = 'left';

    def initialize_sprite(self):
        self.sprite_sheet = Sprite_Sheet('C:\\Users\\Ólafur\\Desktop\\Python\\Towerfall Clone\\Grafix\\Playable Characters\\blue_archer.png', 1, 1);
        self.cell_index = 0;

    def initialize_hitboxes(self):
        self.hitbox_right = [];
        self.hitbox_left = [];
        self.hitbox_top = [];
        self.hitbox_bottom = [];

        for i in range(self.location[1] - 30, self.location[1] + 20):
            self.hitbox_right.append([self.location[0] + 10, i]);
            self.hitbox_left.append([self.location[0] - 10, i]);

        for i in range(self.location[0] - 10, self.location[0] + 10):
            self.hitbox_top.append([i, self.location[1] - 30]);
            self.hitbox_bottom.append([i, self.location[1] + 20]);

    def update_player(self, player_list):
        if(self.player_bullet_collision(player_list)):
            print('Player ' + str(self.player_id) + ' dead!');
            self.player_dead = True;
            return self.player_dead;

        if(not self.player_dead):
            self.player_movement();
            self.draw_bullets();
            self.draw_player();

        return False;

    def draw_player(self):
        #pygame.draw.rect(self.game_display, (255, 255, 255), [self.location[0], self.location[1], 20, 20]);
        self.sprite_sheet.draw(self.game_display, self.cell_index, self.location[0] - 70, self.location[1] - 80, self.direction);

        '''
        for i, j in zip(self.hitbox_right, self.hitbox_left):
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 5, 5]);
            pygame.draw.rect(self.game_display, (255, 255, 255), [j[0], j[1], 5, 5]);

        for i, j in zip(self.hitbox_top, self.hitbox_bottom):
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 5, 5]);
            pygame.draw.rect(self.game_display, (255, 255, 255), [j[0], j[1], 5, 5]);
        '''

    def draw_bullets(self):
        for i in self.bullet_list:
            if(i.bullet_offscreen()):
                self.bullet_list.remove(i);
            else:
                i.draw_bullet();

    def controller_movement(self, axis, event_axis, player_moving):
        if(player_moving):
            if(event_axis == 0):
                if(axis == 0.999969482421875):
                    self.player_moving = True;
                    self.direction = 'right';
                    self.player_movement();
                elif(axis == -1.0):
                    self.player_moving = True;
                    self.direction = 'left';
                    self.player_movement();
                else:
                    self.player_moving = False;

    def controller_action(self, button):
        if(button == 1 and not self.player_in_air()):
            self.player_jumping = True;
            self.jump_counter = 15;
            self.player_movement();
        elif(button == 0):
            self.bullet_list.append(Bullet(self.game_display, self.screen_size[0],
                                           self.location[0], self.location[1], self.direction));

    def player_movement(self):
        if(self.player_moving):
            if(self.direction == 'right' and not self.player_collision(self.direction)):
                self.location[0] += self.speed;
                self.update_hitbox_location(1, 0);
            elif(self.direction == 'left' and not self.player_collision(self.direction)):
                self.location[0] -= self.speed;
                self.update_hitbox_location(-1, 0);
        if(self.player_jumping):
            self.location[1] -= self.jump_speed;
            self.update_hitbox_location(0, -1);
        self.gravity();

    def gravity(self):
        if(self.player_in_air()):
            if(self.jump_counter <= 0):
                self.location[1] += self.jump_speed;
                self.update_hitbox_location(0, 1);
                self.player_jumping = False;
            if(self.jump_counter > 0):
                self.jump_counter -= 1;
        if(self.player_jumping and self.location[1] == 10):
            self.jump_counter = 0;
            self.location[1] += self.jump_speed;
            self.update_hitbox_location(0, 1);

    def update_hitbox_location(self, x, y):
        for i in self.hitbox_right:
            if(x > 0):
                i[0] += self.speed
            elif(x < 0):
                i[0] -= self.speed
            if(y > 0):
                i[1] += self.speed;
            elif(y < 0):
                i[1] -= self.speed;

        for i in self.hitbox_left:
            if (x > 0):
                i[0] += self.speed
            elif (x < 0):
                i[0] -= self.speed
            if (y > 0):
                i[1] += self.speed;
            elif (y < 0):
                i[1] -= self.speed;

        for i in self.hitbox_top:
            if (x > 0):
                i[0] += self.speed
            elif (x < 0):
                i[0] -= self.speed
            if (y > 0):
                i[1] += self.speed;
            elif (y < 0):
                i[1] -= self.speed;

        for i in self.hitbox_bottom:
            if (x > 0):
                i[0] += self.speed
            elif (x < 0):
                i[0] -= self.speed
            if (y > 0):
                i[1] += self.speed;
            elif (y < 0):
                i[1] -= self.speed;

    def player_in_air(self):
        for i in self.level.level_list:
            if(i[0] == self.location[0] and i[1] - 20 == self.location[1]):
                return False;
        return True;

    def player_collision(self, direction):
        for i in self.level.level_list:
            if(direction == 'right'):
                if(i[0] - 20 == self.location[0] and i[1] == self.location[1]):
                    return True;
            elif(direction == 'left'):
                if(i[0] == self.location[0] and i[1] == self.location[1]):
                    return True;
        return False;

    def player_bullet_collision(self, player_list):
        for i in player_list:
            for j in i.bullet_list:
                for k in self.hitbox_right:
                    if((k[0] - 10 == j.x or k[0] == j.x or k[0] + 10 == j.x) and k[1] == j.y):
                        if (i.player_id != self.player_id):

                            i.bullet_list.remove(j);
                            return True;
                for k in self.hitbox_left:
                    if((k[0] - 10 == j.x or k[0] == j.x or k[0] + 10 == j.x) and k[1] == j.y):
                        if (i.player_id != self.player_id):
                            i.bullet_list.remove(j);
                            return True;
                for k in self.hitbox_top:
                    if((k[0] - 10 == j.x or k[0] == j.x or k[0] + 10 == j.x) and k[1] == j.y):
                        if (i.player_id != self.player_id):
                            i.bullet_list.remove(j);
                            return True;
                for k in self.hitbox_bottom:
                    if((k[0] - 10 == j.x or k[0] == j.x or k[0] + 10 == j.x) and k[1] == j.y):
                        if (i.player_id != self.player_id):
                            i.bullet_list.remove(j);
                            return True;
        return False;

    def destroy_hitboxes(self):
        self.hitbox_top = [];
        self.hitbox_bottom = [];
        self.hitbox_left = [];
        self.hitbox_right = [];