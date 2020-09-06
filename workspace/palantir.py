def func(grid):
    R, C = len(grid), len(grid[0])
    ret = [[True for c in range(C)] for r in range(R)]

    for r in range(R):
        for c in range(C):
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                newr, newc = dr + r, dc + c
                if newr < 0 or newr >= R or newc < 0 or newc >= C: continue
                if grid[newr][newc] >= grid[r][c]: ret[r][c] = False
    return ret



def func3(grid):
    R, C = len(grid), len(grid[0])
    ret = [[False for c in range(C)] for r in range(R)]
    calculated = [[False for c in range(C)] for r in range(R)]

    def helper(r, c, visited):
        visited.add((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            newr, newc = r + dr, c + dc
            if newr < 0 or newr >= R or newc < 0 or newc >= C: continue
            if grid[newr][newc] == grid[r][c]:
                if calculated[newr][newc] and not ret[newr][newc]: return False
                if (newr, newc) not in visited and not helper(newr, newc, visited): return False
            elif grid[newr][newc] > grid[r][c]: return False
        return True
    
    for r in range(R):
        for c in range(C):
            if calculated[r][c]: continue
            visited = set()
            plateau = helper(r, c, visited)

            if plateau:
                for r, c in visited:
                    ret[r][c] = True
            for r, c in visited:
                calculated[r][c] = True

    return ret

def func2(grid):
    R, C = len(grid), len(grid[0])
    ret = [[0 for c in range(C)] for r in range(R)]

    def helper(r, c):
        flag = False
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            newr, newc = r + dr, c + dc
            if newr < 0 or newr >= R or newc < 0 or newc >= C: continue
            if grid[newr][newc] < grid[r][c]: 
                helper(newr, newc)
                flag = True

        if not flag:
            ret[r][c] += 1

    return ret



if __name__ == "__main__":
    grid = [[1, 2, 1, 3, 4], 
            [1, 5, 2, 2, 2]]
    grid3 = [[1, 2]]

    grid2 = [[1, 1, 2, 1],
             [1, 3, 1, 1],
             [2, 0, 2, 0],
             [1, 0, 1, 1]]
    # grid4 = [[1, 1, 1, 1, 1],
    #           ]
    print(func2(grid2))