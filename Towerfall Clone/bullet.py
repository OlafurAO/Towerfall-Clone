import pygame;

class Bullet:
    def __init__(self, game_display, screen_width, x, y, direction):
        self.game_display = game_display;
        self.screen_width = screen_width;
        self.x = x;
        self.y = y;
        self.direction = direction;

        self.bullet_speed = 20;

    def draw_bullet(self):
        self.move_bullet();
        pygame.draw.rect(self.game_display, (255, 255, 255), [self.x, self.y, 5, 5]);

    def move_bullet(self):
        if(self.direction == 'right'):
            self.x += self.bullet_speed;
        elif(self.direction == 'left'):
            self.x -= self.bullet_speed;

    def bullet_offscreen(self):
        return self.x >= self.screen_width or self.x < 0;