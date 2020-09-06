import heapq

def minPushBox(grid):
    free = set((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell != '#')
    target = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'T')
    boxi, boxj = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'B')
    si, sj = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'S')
    visited = set()
    heap = [(0, si, sj, boxi, boxj)]
    while heap:
        moves, si, sj, boxi, boxj = heapq.heappop(heap)
        if (boxi, boxj) == target:
            return moves
        if (si, sj, boxi, boxj) in visited:
            continue
        visited.add((si, sj, boxi, boxj))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = si + dx, dy + sj
            if (ni, nj) == (boxi, boxj) and (boxi + dx, boxj + dy) in free and (ni, nj, boxi + dx, boxj + dy) not in visited:
                heapq.heappush(heap, (moves + 1, ni, nj, boxi + dx, boxj + dy))
            elif (ni, nj) in free and (ni, nj) != (boxi, boxj) and (ni, nj, boxi, boxj) not in visited:
                heapq.heappush(heap, (moves, ni, nj, boxi, boxj))
    return -1


if __name__ == "__main__":
    print(minPushBox([["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]))