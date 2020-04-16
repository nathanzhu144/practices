# Nathan Zhu Monday Feb 17th, 2020.  11:15 am.  Palmer commons.  
# Leetcode ? | n/a | medium
# Category: DP
#
# 
# WE want to weld several pieces of a pipe together.  The original pipe pieces follow a certain order, and we can only weld pipes
# that are next to each other in order.  Cost of welding two pieces length l1 and l2 is max(l1, l2), and resulting price has length l1 + l2
#
# Piece1 [4] Piece2[2] Piece3 [10]
#
# Ex. we can weld p1 and p2 for a cost of max(4, 2) = 4.  Then, we weld final 2 pieces together.
#     we can also weld p2 and p3 for a cost of max(2, 10) = 10.  Then, we weld final 2 pieces together.
#
#
# Number of subproblems is N^2, as there are n possible entries for left and right.
# This soln below is N^4, as each of the N^2 problems, minimizes over N possible values of i, and each of those takes two sums,
# each of which takes O(N) time.
#
# If we use a presum array, we can get the runtime down to N^3.

def weld_rods(arr):
    table = dict()
    def helper(l, r):
        if l == r: return 0
        key = (l, r)
        if key in table: return table[key]

        ret = float('inf')
        for i in range(l, r):
            ret = min(helper(l, i) + helper(i + 1, r) + max(sum(arr[l:i + 1]), sum(arr[i + 1:r + 1])), ret)

        table[key] = ret
        return ret

    return helper(0, len(arr) - 1)

if __name__ == "__main__":
    print(weld_rods([3, 5, 1]))

    
