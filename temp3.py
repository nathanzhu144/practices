def prisonAfterNDays(cells, N):
    """
    :type cells: List[int]
    :type N: int
    :rtype: List[int]
    """
    cells_pad, cells_pad_cpy = [0] + cells + [0], [0] + cells + [0]
    table = set()
    counter = 0
    
    # finds length of the cycle
    for index in range(1000):
        if tuple(cells_pad) in table: break
        table.add(tuple(cells_pad))
        counter += 1
        
        new_cells = []
        for i in range(1, 9):
            if cells_pad[i - 1] == cells_pad[i + 1]:
                new_cells.append(1)
            else:
                new_cells.append(0)
        cells_pad = [0] + new_cells + [0]
    
    cells_pad = cells_pad_cpy
    for index in range(N % counter):
        new_cells = []
        for i in range(1, 9):
            if cells_pad[i - 1] == cells_pad[i + 1]:
                new_cells.append(1)
            else:
                new_cells.append(0)
        cells_pad = [0] + new_cells + [0]
    return cells_pad[1:-1]

if __name__ == "__main__":
    print(prisonAfterNDays([0,1,0,1,1,0,0,1], 10000))