#  Nathan Zhu 
#  Saturday June 22nd 10:10 pm Amex Tower 36th floor, executive conf room
#  Monday, May 3rd, 2020, Stockton, CA, COVID-19, damn feel nostalgic of New York
#  There's a simple way to rotate a 2d matrix in-place
#  Leetcode 48 medium
#
# /*
#  * clockwise rotate
#  * first reverse up to down, then swap the symmetry 
#  * 1 2 3     7 8 9     7 4 1
#  * 4 5 6  => 4 5 6  => 8 5 2
#  * 7 8 9     1 2 3     9 6 3
# */
# void rotate(vector<vector<int> > &matrix) {
#     reverse(matrix.begin(), matrix.end());
#     for (int i = 0; i < matrix.size(); ++i) {
#         for (int j = i + 1; j < matrix[i].size(); ++j)
#             swap(matrix[i][j], matrix[j][i]);
#     }
# }

# /*
#  * anticlockwise rotate
#  * first reverse left to right, then swap the symmetry
#  * 1 2 3     3 2 1     3 6 9
#  * 4 5 6  => 6 5 4  => 2 5 8
#  * 7 8 9     9 8 7     1 4 7
# *  


# NOTE: col must start at row + 1, or at least at row (but matrix[i][i] == matrix[i][i]) ... so better
#       row + 1.  It CANNOT start at 0
def clockwiserotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    matrix.reverse()
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix[0])):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    
    return matrix

def counterclockwiserotate(matrix):
    for list_ in matrix:
        list_.reverse()

    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix


if __name__ == "__main__":
    print(clockwiserotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(counterclockwiserotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
