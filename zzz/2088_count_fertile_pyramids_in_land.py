


def count(grid):

    R, C, ret = len(grid), len(grid[0]), 0

    for r in range(1, R):
        for c in range(1, C - 1):
            if grid[r][c] and grid[r - 1][c]:
                grid[r][c] = min(grid[r - 1][c - 1], grid[r - 1][c + 1]) + 1
                ret += grid[r][c] - 1
    return ret


if __name__ == "__main__":
    grid = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]
    count(grid)