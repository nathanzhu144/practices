# Nathan Zhu Nov 27th, 2019.
#            At 370 thanksigiving party with her and indian girls.  It is boring, so I do leetcode.
#            Going to Johnny's house tomorrow.
# Leetcode 1130 | medium | not at all medium.


# Runtime of this one is pretty bad.
# No idea what runtime is
# Idea is:
#  
# We attempt all possible pairs of numbers.
# [13, 10, 15, 8]
#          ->   
#               [13, 15, 8] + 130
#               [13, 15, 8] + 150
#               [13, 10, 15] + 15 * 8
#                            ->  ...
# We try merging every pair of numbers, and so on, until we only get to two numbers.
# Notice we get [13, 15, 8] twice.  We memoize each of the arrays.
# Runtime: Really bad.
def mctFromLeafValues_backtrack(arr):
    def helper(arr, mem):
        # base case, for final node we only have a left and a right
        if len(arr) == 2: return arr[0] * arr[1]
        
        key = tuple(arr)
        if key in mem: return mem[key]
        
        ret = float('inf')
        for i in range(len(arr) - 1):
            curr = arr[i] * arr[i + 1] + helper(arr[: max(0, i)] + [max(arr[i], arr[i + 1])] + arr[i + 2 : ], mem)
            ret = min(curr, ret)
            
        mem[key] = ret
        return ret
    
    return helper(arr, dict())

# Runtime for this one is OK (N^2)
# Idea of this one is we first want to pair the smallest leaves,
# so we do a sliding window, finding the pair with the smallest product.
# We remove 
def mctFromLeafValues_better(arr):
    ret = 0
    while len(arr) > 1:
        del_idx = 0
        min_prod = float('inf')

        for i in range(len(arr) - 1):
            curr_prod = arr[i] * arr[i + 1]
            if curr_prod < min_prod:
                if arr[i] < arr[i + 1]: del_idx = i
                else: del_idx = i + 1
                min_prod = curr_prod

        ret += min_prod
        arr.pop(del_idx)
    
    return ret

if __name__ == "__main__":
    pass
    #print(mctFromLeafValues([11, 12, 12]))