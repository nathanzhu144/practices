#  Nathan Zhu Amex Building 36th floor, Wednesday June 10th, 2019, 9:11 am
#  Leetcode 486 | medium | not too bad, easier medium
#  Type: DP
#  Runtime - 2^N naive as T(n) = T(n - 1) * 2 + O(1), N^2 DP, N is len of stones array.  
#  Space   - N^2 as implemented here, but can be done in O(n)
#  Similar problems: Leetcode 877 stone game (same problem basically)
#  This is actually a case of minimax.
#  
#  https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-877-stone-game/
#  https://leetcode.com/problems/predict-the-winner/
#  

def predict_winner(arr):
    # note that i and j are inclusive
    def helper(arr, i, j, mem):
        if j < i: return 0
        if j == i: return arr[i]
        key = (i, j)
        if key in mem: return mem[key]

        mem[key] = max(arr[i] - helper(arr, i + 1, j, mem), arr[j] - helper(arr, i, j - 1, mem))
        return mem[key]
    return False if helper(arr, 0, len(arr) - 1, dict()) < 0 else True