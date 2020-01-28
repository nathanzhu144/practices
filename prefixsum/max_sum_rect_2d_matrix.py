# Nathan Zhu 9:54 am Ugli 
# Geeks for geeks DP-17 | hard? | yeah hard i think
# Category: Subarray sum / DP
#
# https://www.geeksforgeeks.org/maximum-sum-rectangle-in-a-2d-matrix-dp-27/
# So, this uses Kadane's algorithm.
# Rumtime (col ^ 2 * rows)
# This structure seems relatively common for 2d matrix problems.

def func(matrix):
    ret = float('-inf')
    if not matrix or not matrix[0]: return 0
    R, C = len(matrix), len(matrix[0])

    for sc in range(C):
        column = [[0] for r in range(R)]
        for ec in range(sc, C):
            for r in range(R):
                column[r][0] += matrix[r][ec]
            presum = 0

            for r in range(R):
                if presum < 0: presum = 0
                presum += column[r][0]
                ret = max(ret, presum)
            
    return ret

if __name__ == "__main__":
    print(func([[1, 2, -1, -4, -20],
                [-8, -3, 4, 2, 1],
                [3, 8, 10, 1, 3],
                [-4, -1, 1, 7, -6]]))
    print(func([[-10, -20], [-1, -2]]))
    print(func([[6, -5, -7, 4, -4], 
                [-9, 3, -6, 5, 2], 
                [-10, 4, 7, -6, 3],
                [-8, 9, -3, 3, -7]]))


