import pygame
from colors import Color

TYPES = {
    'default': Color.get_color("white"),
    'wall': Color.get_color("black"),
    'start': Color.get_color("orange"),
    'end': Color.get_color("blue"),
    'open': Color.get_color("green"),
    'closed': Color.get_color("yellow"),
    'path': Color.get_color("purple")
}


class Block:

    def __init__(self, position, size):
        self.position = position
        self.type = TYPES['default']
        self.size = size

    def is_wall(self):
        return self.type == TYPES['wall']

    def change_type(self, type):
        self.type = TYPES[type]


BORDER_COLOR = Color.get_color("gray")


class Grid:
    def __init__(self, width, height, columns, screen):
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = height // (self.width // self.columns)
        self.grid = []
        self.block_size = self.width // self.columns
        self.screen = screen

        self.initialize_grid()

    def initialize_grid(self):
        self.grid = [[Block((row, column), self.block_size) for column in range(
            self.columns)] for row in range(self.rows)]

    def reset_grid(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.grid[row][column].change_type('default')

    def draw(self):
        self.draw_blocks()
        self.draw_column_borders()
        self.draw_row_borders()
        pygame.display.update()

    def draw_blocks(self):
        for row in self.grid:
            for block in row:
                block_rect = pygame.Rect(block.position[1] * self.block_size,
                                         block.position[0] * self.block_size,
                                         self.block_size, self.block_size)
                pygame.draw.rect(self.screen, block.type, block_rect)

    def draw_column_borders(self):
        for column in range(self.columns + 1):
            x = column * self.block_size
            pygame.draw.line(self.screen, BORDER_COLOR,
                             (x, 0), (x, self.height))

    def draw_row_borders(self):
        for row in range(self.rows + 1):
            y = row * self.block_size
            pygame.draw.line(self.screen, BORDER_COLOR,
                             (0, y), (self.width, y))

    def get_clicked_pos(self, pos):
        x, y = pos
        row = y // self.block_size
        col = x // self.block_size
        return row, col

    def get_block(self, row, column):
        return self.grid[row][column]
