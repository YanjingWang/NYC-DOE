class BFS:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.frontier = [self.start]
        self.explored = set()
        self.came_from = {self.start: None}
        self.cost_so_far = {self.start: 0}

    def neighbors(self, node):
        # Assuming that 'node' is a tuple (row, column)
        directions = [('N', -1, 0), ('S', 1, 0), ('E', 0, 1), ('W', 0, -1)]
        row, col = node
        result = []
        for direction, dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) in self.grid and self.grid[new_row, new_col]:
                result.append((new_row, new_col))
        return result

    def cost(self, from_node, to_node):
        return 1  # constant cost for BFS

    # ... (other methods like search and reconstruct_path as before)
    def search(self):
        self.frontier.append(self.start)
        while self.frontier:
            current = self.frontier.pop(0)
            self.explored.add(current)
            if current == self.goal:
                return self.reconstruct_path()
            for next_node in self.neighbors(current):
                if next_node not in self.explored and next_node not in self.frontier:
                    self.frontier.append(next_node)
                    self.came_from[next_node] = current
                    self.cost_so_far[next_node] = self.cost_so_far[current] + self.cost(current, next_node)
        return None  # Goal was not reached

    def reconstruct_path(self):
        # Reconstruct the path from start to goal
        current = self.goal
        path = []
        while current is not None:  # Checks if the node has a parent
            path.append(current)
            current = self.came_from.get(current, None)
        path.reverse()
        return path
    
grid_layout = {
    (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): True,  # Row A
    (2, 1): False,  (2, 2): True, (2, 3): False, (2, 4): True, (2, 5): True, # Row B
    (3, 1): True,  (3, 2): True,  (3, 3): True,  (3, 4): True,  (3, 5): True,  # Row C
    (4, 1): False,  (4, 2): True, (4, 3): False, (4, 4): True, (4, 5): True,  # Row D
    (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): True  # Row E
}
# Make sure the start and goal are tuples representing the coordinates
# Convert 'A5' to (1, 5) and 'D1' to (4, 1) as per the grid definition
start = (1, 5)  # A5
goal = (4, 1)  # D1

# Now you can create a BFS object with the start, goal, and grid
bfs = BFS(start, goal, grid_layout)
bfs_path = bfs.search()
print(bfs_path)
