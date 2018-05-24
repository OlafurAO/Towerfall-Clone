import pygame;
from player import Player;
from level import Level;

pygame.mixer.pre_init(44100, 16, 2, 4096);
pygame.init();

screen_size = (800, 600);
game_display = pygame.display.set_mode(screen_size);
clock = pygame.time.Clock();

FPS = 60;

font = pygame.font.SysFont('hooge0555cyr2', 40);

def render_screen(player_list, level):
    game_display.fill((0, 0, 0));

    for i in player_list:
        if(i.update_player(player_list)):
            #player_list.remove(i);
            i.destroy_hitboxes();
            i = 'DEAD!';


    level.draw_level();

    pygame.display.update();
    clock.tick(FPS);

def render_player_select(joystick_list):
    start = False;

    player_one = 0;
    player_two = 0;
    player_three = 0;
    player_four = 0;

    while not start:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False;
            if(event.type == pygame.JOYBUTTONDOWN):
                if(event.button == 1):
                    if(joystick_list[event.joy].get_id() == 0 and player_one == 0):
                        player_one += 1;
                    elif(joystick_list[event.joy].get_id() == 1 and player_two == 0):
                        player_two += 1;
                    elif (joystick_list[event.joy].get_id() == 2 and player_three == 0):
                        player_three += 1;
                    elif (joystick_list[event.joy].get_id() == 3 and player_four == 0):
                        player_four += 1;

                if(event.button == 9 and player_one + player_two + player_three + player_four > 0):
                    return player_one + player_two + player_three + player_four;


        game_display.fill((0, 0, 0));

        player_select_art(player_one, player_two, player_three, player_four);

        pygame.display.update();

def player_select_art(player_one, player_two, player_three, player_four):
    screen_text = font.render('PRESS       A', True, (255, 255, 255));

    if(player_one > 0):
        screen_text = font.render('PLAYER 1 READY', True, (255, 255, 255));
        game_display.blit(screen_text, [50, 140]);
    else:
        game_display.blit(screen_text, [80, 140]);

    screen_text = font.render('PRESS       A', True, (255, 255, 255));

    if (player_three > 0):
        screen_text = font.render('PLAYER 3 READY', True, (255, 255, 255));
        game_display.blit(screen_text, [50, screen_size[1] - 140]);
    else:
        game_display.blit(screen_text, [80, screen_size[1] - 140]);

    screen_text = font.render('PRESS       A', True, (255, 255, 255));

    if (player_two > 0):
        screen_text = font.render('PLAYER 2 READY', True, (255, 255, 255));
        game_display.blit(screen_text, [screen_size[0] - 360, 140]);
    else:
        game_display.blit(screen_text, [screen_size[0] - 250, 140]);

    screen_text = font.render('PRESS       A', True, (255, 255, 255));



    if (player_three > 0):
        screen_text = font.render('PLAYER 3 READY', True, (255, 255, 255));
        game_display.blit(screen_text, [screen_size[0] - 220, screen_size[1] - 140]);
    else:
        game_display.blit(screen_text, [screen_size[0] - 250, screen_size[1] - 140]);

    screen_text = font.render('PRESS       A', True, (255, 255, 255));

    if(player_one + player_two + player_three + player_four > 0):
        start_text = font.render('PRESS START TO BEGIN', True, (255, 255, 255));
        game_display.blit(start_text, [screen_size[0]/2 - 190, screen_size[1]/2]);

    draw_a(player_one, player_two, player_three, player_four);

def draw_a(player_one, player_two, player_three, player_four):
    for i in range(235, 265, 5):
        if(player_one == 0):
            pygame.draw.rect(game_display, (255, 255, 255), [i, 140, 5, 5]);
            pygame.draw.rect(game_display, (255, 255, 255), [i, 180, 5, 5]);

        if(player_two == 0):
            pygame.draw.rect(game_display, (255, 255, 255), [i + 470, 140, 5, 5]);
            pygame.draw.rect(game_display, (255, 255, 255), [i + 470, 180, 5, 5]);
        
    for i in range(150, 175, 5):
        if(player_two == 0):
            pygame.draw.rect(game_display, (255, 255, 255), [270, i, 5, 5]);
            pygame.draw.rect(game_display, (255, 255, 255), [225, i, 5, 5]);
            pygame.draw.rect(game_display, (255, 255, 255), [695, i, 5, 5]);
            pygame.draw.rect(game_display, (255, 255, 255), [740, i, 5, 5]);

    if(player_one == 0):
        pygame.draw.rect(game_display, (255, 255, 255), [265, 145, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [265, 175, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [230, 145, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [230, 175, 5, 5]);

        pygame.draw.rect(game_display, (255, 255, 255), [265, 145, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [265, 175, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [230, 145, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [230, 175, 5, 5]);

    if(player_two == 0):
        pygame.draw.rect(game_display, (255, 255, 255), [700, 145, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [700, 175, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [735, 145, 5, 5]);
        pygame.draw.rect(game_display, (255, 255, 255), [735, 175, 5, 5]);

def setup_players(level, player_number):
    #player_number = 2;
    player_list = [];

    for i in range(0, player_number):
        player_list.append(Player(i + 1, game_display, screen_size, level));

    return player_list;

def setup_joysticks():
    joystick_list = [];
    for i in range(0, pygame.joystick.get_count()):
        joystick_list.append(pygame.joystick.Joystick(i));

    for i in joystick_list:
        i.init();
        print('Detected gamepad: ' + i.get_name(), i.get_id());
        print('Initializing ' + i.get_name());

    return joystick_list;

def main():
    game_over = False;
    joystick_list = setup_joysticks();
    level = Level(game_display, screen_size);

    num_of_players = render_player_select(joystick_list);

    if(not num_of_players):
        game_over = True;
    else:
        player_list = setup_players(level, num_of_players);

    pygame.mixer.music.load('C:\\Users\\Ólafur\\Desktop\\Python\\Towerfall Clone\\Sounds\Muzak\\Guile Theme SNES.mp3');
    pygame.mixer.music.set_volume(1);
    pygame.mixer.music.play(-1);

    while not game_over:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                game_over = True;

            if(event.type == pygame.JOYBUTTONDOWN):
                if (joystick_list[event.joy] != 'DEAD!'):
                    player_list[joystick_list[event.joy].get_id()].controller_action(event.button);

            if(event.type == pygame.JOYAXISMOTION):
                if(joystick_list[event.joy] != 'DEAD!'):
                    axis = joystick_list[event.joy].get_axis(event.axis);
                    player_list[joystick_list[event.joy].get_id()].controller_movement(axis, event.axis, True);

        render_screen(player_list, level);

if __name__ == '__main__':
    main();