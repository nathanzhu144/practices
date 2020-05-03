# Nathan Zhu April 18th, 2020. 
# Leetcode 1415 | medium | easu
# Category: Backtracking
# Didn't have time to do this solution, but this is just a backtracking question.

def getHappyString(n, k):
    ret = [""]
    left = [k]
    def dfs(n, curr):
        if k <= 0: return
        if n == 0:
            if left[0] == 1:
                ret[0] = "".join(curr)
            left[0] -= 1
            return

        for ch in "abc":
            if not curr or ch != curr[-1]:
                dfs(n - 1, curr + [ch])
    dfs(n, [])
    return ret[0]

if __name__ == "__main__":
    print(getHappyString(1, 3))