# Nathan Zhu April 18th, 2020. 
# Leetcode 1416 | hard | not that bad?
# Category: DP
# Encountered this in a biweekly contest.  I got the DFS memoized version, which didn't pass
# the largest test cases. Should've got this one.  :()
# Timre complexity: O(N * log10K)

# dp[i] records all the possible arrays that can be 
# printed as a string s[i:]
#
# Base case:
# 1 way to construct an empty string
#
# State transition:
# Find all possible number we can input, starting at s[i],
# thus, dp[i] = sum(dp[j] for all valid j) where valid j means that 
# 1 <= int(dp[i:j]) <= k
def numberOfArrays(s: str, k: int) -> int:
    const = 10 ** 9 ++ 7
    N = len(s)
    dp = [0] * N + [1]
    string = [*map(int, s)] + [float('inf')]
    
    for i in range(N - 1, -1, -1):
        num = string[i]
        # j indicates character we will add on next to end of string
        for j in range(i + 1, N + 1):
            if not 1 <= num <= k: break
            dp[i] = (dp[i] + dp[j]) % const
            num = num * 10 + string[j]
            
    return dp[0]


# My solution, which I think is optimal for DFS, but timed out at the end.
# Also runs in O(NlogK)
def numberOfArrays_DFS(s: str, k: int) -> int:
    table = dict()

    def helper(s, k, idx):
        if not s: return 1
        N = len(s)
        if idx in table: return table[idx]

        ret = 0
        for i in range(1, N + 1):
            if int(s[:i]) <= k and s[:i][0] != "0":
                ret += helper(s[i:], k, i + idx)
                ret %= (10 ** 9 + 7)

        table[idx] = ret
        return ret

    return helper(s, k, 0) 

if __name__ == "__main__":
    print(numberOfArrays("1317", 2000))