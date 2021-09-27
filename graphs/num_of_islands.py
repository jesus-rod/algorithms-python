""""

Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land.
The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3

"""


def island_count(grid):
    visited = set()
    num_of_islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                num_of_islands += 1
    return num_of_islands


def explore(grid, row, col, visited):

    row_in_bounds = 0 <= row < len(grid)
    col_in_bounds = 0 <= col < len(grid[0])

    if not row_in_bounds or not col_in_bounds:
        return False

    if grid[row][col] == 'W':
        return False

    if (row, col) in visited:
        return False

    visited.add((row, col))

    explore(grid, row - 1, col, visited)
    explore(grid, row + 1, col, visited)
    explore(grid, row, col + 1, visited)
    explore(grid, row, col - 1, visited)

    return True


result = island_count(grid=[
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
])

print(result)
