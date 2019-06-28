#  Nathan Zhu 1:04 am, Amex tower, 200 Vessey Street, 36th floor, huddled in a dark focus room
#  Leetcode 74 | medium | I think cool - not too hard, not too easy, like I get it.
#  I'm impressed, I got the correct soln with only 1 syntax mistake! 
#
#  Complexity O(min(logM, logN)).
#
#  So, some solutions on leetcode treat the 2d matrix as 1d matrix.  This is BAD, as it converts the runtime to O(log(M * N)), rather
#  than O(min(logM, logN)).  
#
#  How to solve?
#
#  1. We find the right row.
#  2. We find the right col.
#  If we cannot find it, it doesn't exist in the matrix.
#
#  ##############33
#  Break down steps
#  ################
#
#  1. Finding the correct row is finding the upper bound of all the row where target > matrix[med][0].  This is true
#     becuase the smallest element in a row, is the 0th column.  Since we have handled the case where target == matrix[med][0],
#     we are left finding the BIGGEST row where target > matrix[med][0].
#  
#     We do this with a very familiar upper-bound structure.  See leetcode 69, sqrt x for similar structure.
#
#  2. Finding the correct column is much easier, actually.  We just need to check whether the element exists in the
#     correct row.  We do a regular binary search where right = med - 1 and left = me + 1.  We return true iff we have
#     found the target.  
#
#     If left == right + 1, then we return False, as target doesn't exist (on last loop iteration, we mid == left == right, so we 
#                           would find target if it were in the array)

def search_2d(matrix, target):
    if not matrix or not matrix[0]: return False

    # 
    ans = -1
    left, right = 0, len(matrix) - 1
    while left <= right:
        med = (right - left) // 2 + left

        if target == matrix[med][0]: return True
        elif target < matrix[med][0]: right = med - 1
        elif target > matrix[med][0]:
            ans = med
            left = med + 1

    correct_row = ans

    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        med = (right - left) // 2 + left

        if target == matrix[correct_row][med]: return True
        elif target < matrix[correct_row][med]: right = med - 1
        elif target > matrix[correct_row][med]: left = med + 1

    return False