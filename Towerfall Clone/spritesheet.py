import pygame;

class Sprite_Sheet:
    def __init__(self, image, cols, rows):
        self.sheet_right = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (150, 150));

        self.sheet_left = pygame.transform.flip(self.sheet_right, True, False);

        self.cols = cols;
        self.rows = rows;
        self.total_cell_count = cols * rows;

        self.rect = self.sheet_right.get_rect();

        self.cell_width = int(self.rect.width / cols);
        self.cell_height = int(self.rect.height / rows);
        self.cells = [];

        for index in range(self.total_cell_count):
            self.cells.append((index % self.cols * self.cell_width,
                               int(index / cols) * self.cell_height,
                               self.cell_width, self.cell_height));

    def draw(self, game_display, cell_index, x, y, direction):
        if(direction == 'left'):
            game_display.blit(self.sheet_left, (x, y), self.cells[cell_index]);
        else:
            game_display.blit(self.sheet_right, (x, y), self.cells[cell_index]);