#  Nathan Zhu Amex Building 36th floor, Wednesday June 10th, 2019, 8:44 am
#  Leetcode 877 | medium | not too bad, easier medium
#  Type: DP, category 1.2
#  Runtime - 2^N naive as T(n) = T(n - 1) * 2 + O(1), N^2 DP, N is len of stones array.  
#  Space   - N^2 as implemented here, but can be done in O(n)
#  
#  This is actually a case of minimax.
#
#  https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-877-stone-game/
#
#  https://leetcode.com/problems/stone-game/
#  Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, 
#  and each pile has a positive integer number of stones piles[i].
#  The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
#  
# 
def stoneGame(self, arr):
    """
    :type piles: List[int]
    :rtype: bool
    """
    # note that i and j are inclusive indices
    def helper(arr, i, j, mem):
        if j < i: return 0
        if i == j: return arr[i]
        key = (i, j)
        if key in mem: return mem[key]

        # You try to take the maximum move, either stone at left end or stone at right end
        # assuming your opponent will attempt to maximize their score with the resulting stone row
        mem[key] = max(arr[i] - helper(arr, i + 1, j, mem), arr[j] - helper(arr, i, j - 1, mem))
        return mem[key]
    return helper(arr, 0, len(arr) - 1, dict())