#   //        [[2]                 [[2]
#   //      [3, 4]]              [5, 6]
#   //    [6, 5, 7]]           [11, 10, 11]
#   //  [4, 1, 8, 3]]        [15, 11, 18, 14]]

# [[-1],
# [  2,3],o
# [  1,-1,-3]]
def min_triangle_path(triangle):
    def helper(triangle, index, mem):
        layer = len(triangle) - 1
        key = (index, layer)
        if key in mem: return mem[key]
        if layer == 0: return triangle[0][0]   # this is tip of triangle.
        if not triangle: return 0              # empty triangle has 0 paths

        ret = float('inf')
        for i in range(index, len(triangle[layer])):
            left, mid, right = float('inf'), float('inf'), float('inf')
            left = helper(triangle[:-1], i - 1, mem) + triangle[layer][i] if i >= 0 else float('inf')
            mid = helper(triangle[:-1], i, mem) + triangle[layer][i] if i < len(triangle[:-1]) else float('inf')
            ret = min(ret, left, mid)

        mem[key] = ret
        return ret

    mem = dict()
    temp = float('inf')
    for i in range(len(triangle[-1])):
        temp = min(temp, helper(triangle[:-1], i, mem) + triangle[-1][i]) 
    
    return temp

if __name__ == "__main__":
    print(min_triangle_path([[-1], [ 2,3], [ 1,-1,-3]]))
