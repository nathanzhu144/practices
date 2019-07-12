# Nathan Zhu, Amex Building 36th floor, 200 Vessey Street
# Leetcode 980 | hard | I think hard/med
# 
# No tricks for this one.  We need to find all unique paths that go from start of board "1"
# to end "2", while covering all the squares, and not touching any "-1" squares.
# 

def unique_paths_III(matrix):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # we do a simple DFS here
    def dfs(matrix, row, col, steps, visited, target):
        key = (row, col)
        # Invalid if off board, -1 square, or visited already
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) \
            or matrix[row][col] == -1 or key in visited: return 0

        # If we reached end, check if we took correct number of steps
        if matrix[row][col] == 2: return int(steps == target)

        ret = 0
        visited.add(key)         # backtrack
        for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            new_row, new_col = row + d[0], col + d[1]
            ret += dfs(matrix, new_row, new_col, steps + 1, visited, target)   # add number of paths this path makes
        visited.remove(key)      # backtrack
        return ret

    # Here we do 2 things.
    # 1. we find the start position (row, col)
    # 2. we find the length of the path, since we need to traverse all non-negative-one squares,
    #    we count the number of them.
    target = 0
    start_r, start_c = -1, -1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != -1:
                target += 1
            if matrix[row][col] == 1:
                start_r, start_c = row, col

    return dfs(matrix, start_r, start_c, 1, set(), target)
