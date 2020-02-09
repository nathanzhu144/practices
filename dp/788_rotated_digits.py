# Nathan Zhu Friday Jan 3rd, 2020.  5:46 pm, Google practice OA, Wes Weimer is lecture about code review.
# Leetcode 788 | easy | ehh medium
# Category: DP

def rotatedDigits(N):
    """
    :type N: int
    :rtype: int
    """
    dp = [0] * (N + 1)
    ret = 0
    for i in range(N + 1):
        if i < 10:
            if i in [0, 1, 8]: dp[i] = 1
            elif i in [2, 5, 6, 9]: 
                dp[i] = 2
                ret += 1
        else:
            a, b = dp[i // 10], dp[i % 10]
            if a == 1 and b == 1: dp[i] = 1
            elif a >= 1 and b >= 1: 
                dp[i] = 2
                ret += 1
                
    return ret

if __name__ == "__main__":
    print(rotatedDigits(20))