import pygame
import sys
from grid import Grid
from algorithm import AStar

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
GRID_COLUMNS = 40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A* Path Finding Algorithm")

grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_COLUMNS, screen)

a_star = AStar(grid)


def main():
    start = None
    end = None
    is_running = True

    while is_running:
        grid.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_pos(pos)
                block = grid.get_block(row, col)
                if not start and block != end:
                    start = block
                    start.change_type('start')

                elif not end and block != start:
                    end = block
                    end.change_type('end')

                elif block != end and block != start:
                    block.change_type('wall')

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_pos(pos)
                block = grid.get_block(row, col)
                block.change_type('default')
                if block == start:
                    start = None
                elif block == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    a_star.find_path(start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid.reset_grid()

    pygame.quit()
    sys.exit()


main()
