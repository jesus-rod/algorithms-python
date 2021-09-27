""""
minimum island
Write a function, minimum_island, that takes in a grid containing Ws and Ls.
W represents water and L represents land. The function should return the size of the smallest island. 
An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.
"""

# 1. created a set for visited
# 2. set the min_size of island to a very high number
# 3. explore the grid 
# 4. this requires dfs so we need several base cases
# 5. check that the current row, col is inbounds. If not, return 0
# 6. if current row,col is water 'W', we don't need to traverse it. return 0
# 7. if already visited, return 0.
# 8. Otherwise... add to visited
# 9. Created a size of 1 and explore in all directions (dfs) up, down, left, right
# 10. return size


def minimum_island(grid):
    visited = set()
    min_size = float("inf")

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore(grid, row, col, visited)
            if size > 0:
                min_size = min(min_size, size)
    return min_size


def explore(grid, row, col, visited):

    row_in_bounds = 0 <= row < len(grid)
    col_in_bounds = 0 <= col < len(grid[0])

    if not row_in_bounds or not col_in_bounds:
        return 0

    if grid[row][col] == 'W':
        return 0

    if (row, col) in visited:
        return 0

    visited.add((row, col))

    size = 1
    size += explore(grid, row - 1, col, visited)
    size += explore(grid, row + 1, col, visited)
    size += explore(grid, row, col + 1, visited)
    size += explore(grid, row, col - 1, visited)

    return size


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

result = minimum_island(grid)

print(result)
