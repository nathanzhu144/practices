# Nathan Zhu Friday August 2nd, 2019 8:59 am
# Leetcode 54 | medium | medium?
# This question is not intuitive when you first see it.
# 
# Intuition:
# 
# We have a cursor that starts at row 0, col -1, (0, -1).
# To go in a clockwise spiral order:
#    1. drag it to the right numcols places         A
#    2. drag it down numrows - 1 places             B
#    3. drag it to the left numcols - 1 places      A
#    4. drag it up numrows - 2 places               B
#    5. drag it to the right numcols - 2 places     A
#    6. drag it down numrows - 3 places             B
# 
# We continue until numrows - N == 0 or numcols - M == 0
#
# 
#  Followup: How to make it go counterclockwise instead of clockwise?
#            Easy, just change the directions array.

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """ 
    if not matrix: return []

    ret = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # NOTE: numrows - 1 is intentional
    bounds = [len(matrix[0]), len(matrix) - 1]    # bounds = [numcols, numrows - 1]
    row, col = 0, -1
    counter = 0

    while bounds[counter % 2] > 0:
        for i in range(bounds[counter % 2]):
            row += directions[counter % 4][0]
            col += directions[counter % 4][1]
            ret.append(matrix[row][col])
        bounds[counter % 2] -= 1
        counter += 1

    return ret

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    
    matrix = [[0 for col in range(n + 1)] for row in range(n + 1)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    counter = 0
    row, col = 0, -1
    integer = 1

    bounds = [n + 1, n]
    while bounds[counter % 2]:
        for i in range(bounds[counter % 2]):
            row += directions[counter % 2][0]
            col += directions[counter % 2][1]
            matrix[row][col] = integer
            integer += 1
        bounds[counter % 2] -= 1
        counter += 1
        
        
    return matrix
            

if __name__ == "__main__":
    print(generateMatrix(2))
    print(spiralOrder([
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9,10,11,12]

                        ]))
                    