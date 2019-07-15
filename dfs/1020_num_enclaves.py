#  Nathan Zhu 8:12 pm, Amex tower, 36th floor, New York
#  Leetcode 1020 | medium | I think med
#
#  An enclave is an island where there's no path leading off.
#  
#  I count the number of enclaves by checking if there's a way 
#  off of the island, and if not coloring it to 2
#  If you can get off, color it -1.
#  The color function returns how big the island is
#  
#  This would be a good way of counting the number of islands 
#  that you cannot get off of.
#
#  NOTE: Better solution. Take the squares on all four edges of the grid, and 
#        do a DFS from each of them, coloring all squares seen
#
#        Iterate thru grid, and add one for every un-colored square.
#  https://leetcode.com/problems/number-of-enclaves/discuss/265555/C%2B%2B-with-picture-DFS-and-BFS



def num_enclaves(matrix):
    def is_valid(matrix, row, col):
        return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])

    # Is there a way off of this island?
    def is_way_out(matrix, row, col, visited):
        if (row, col) in visited: return False
        visited.add((row, col))
        if matrix[row][col] != 1: return False

        if row == 0 or col == 0 or row == len(matrix) - 1 or col == len(matrix[0]) - 1: 
            return True

        ret = False
        for d in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            new_row, new_col = row + d[0], col + d[1]
            if is_valid(matrix, new_row, new_col) and (new_row, new_col) not in visited:
                ret = ret or is_way_out(matrix, new_row, new_col, visited)
        return ret

    # color island to desired color, to not visit it again.
    def color_isle(matrix, row, col, color):
        if matrix[row][col] != 1: return 0
        matrix[row][col] = color
        ret = 1

        for d in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            new_row, new_col = row + d[0], col + d[1]
            if is_valid(matrix, new_row, new_col):
                ret += color_isle(matrix, new_row, new_col, color)
        return ret

    color = 2
    enclaves = 0
    # If an island can be escaped from, we color it -1, so we don't do a DFS on it again.
    # If an island cannot be escaped from, we color it 2, and we increment enclaves
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and not is_way_out(matrix, row, col, set()):
                enclaves += color_isle(matrix, row, col, 2)
            elif matrix[row][col] == 1:  # and is way out
                color_isle(matrix, row, col, -1)

    return enclaves

if __name__ == "__main__":
    print(num_enclaves([[0,0,0,0],
                        [1,0,1,0],
                        [0,1,1,0],
                        [0,0,0,0]]))