import heapq


def heuristic(node, end):
    x1, y1 = node.position
    x2, y2 = end.position
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(parent, current_node, start):
    current_node = parent[current_node]

    while current_node != start:
        current_node.change_type('path')
        current_node = parent[current_node]


class AStar:
    def __init__(self, grid):
        self.grid = grid

    def get_neighbours(self, node):
        neighbours = []
        x, y = node.position

        # DOWN
        if x < self.grid.rows - 1 and not self.grid.grid[x + 1][y].is_wall():
            neighbours.append(self.grid.grid[x + 1][y])

        # UP
        if x > 0 and not self.grid.grid[x - 1][y].is_wall():
            neighbours.append(self.grid.grid[x - 1][y])

        # RIGHT
        if y < self.grid.columns - 1 and not self.grid.grid[x][y + 1].is_wall():
            neighbours.append(self.grid.grid[x][y + 1])

        # LEFT
        if y > 0 and not self.grid.grid[x][y - 1].is_wall():
            neighbours.append(self.grid.grid[x][y - 1])

        return neighbours

    def find_path(self, start, end):
        counter = 0
        open_list = [(0, counter, start)]
        parent = {}
        g_values = {start: 0}

        while open_list:
            _, _, current_node = heapq.heappop(open_list)

            if current_node != start and current_node != end:
                current_node.change_type('closed')

            if current_node == end:
                reconstruct_path(parent, current_node, start)
                return True

            neighbours = self.get_neighbours(current_node)

            for neighbour in neighbours:
                temp_g = g_values[current_node] + 1

                if neighbour not in g_values or temp_g < g_values[neighbour]:
                    g_values[neighbour] = temp_g
                    f_value = temp_g + heuristic(neighbour, end)
                    counter += 1
                    heapq.heappush(open_list, (f_value, counter, neighbour))
                    parent[neighbour] = current_node

                    if neighbour != end:
                        neighbour.change_type('open')

            self.grid.draw()

        return False
