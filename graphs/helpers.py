def print_grid(grid):
    for row in range(len(grid)):
        print("")
        for col in range(len(grid[0])):
            print(grid[row][col], end="", flush=True)

    print("")
