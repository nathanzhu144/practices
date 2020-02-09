# Nathan Zhu Jan 26th, 2020 Ugli 3rd floor, I'm kinda hungry.
# Leetcode 465 | hard | yeah kinda hard
# This is just a classic backtracking problem. Tricks are hard because this is a NP-hard problem reducible to 3-partitioning.
# 
import collections
# person0 gave person1 250 dollars [[0, 1, 250]]
def min_transfers(arr):
    temp = collections.defaultdict(int)
    debts = list()

    for person1, person2, debt in arr:
        temp[person1] += debt
        temp[person2] -= debt

    for key in temp:
        if temp[key] != 0: debts.append(temp[key])

    # curr
    # [-2, 5, -3, 7, -7]
    # Recursive call 1
    #          curr
    #          next
    #       [-2, 3, -3, 7,  -7]
    # 
    # Recursive call 2
    #           curr
    #                  next
    #       [-2, 3, -3, 5,  -7]
    # 
    def helper(curr):
        while curr < len(debts) and debts[curr] == 0: curr += 1
        if curr == len(debts): return 0

        ret = float('inf')
        for next in range(curr + 1, len(debts)):
            if debts[curr] * debts[next] < 0:
                debts[next] += debts[curr]
                ret = min(1 + helper(curr + 1), ret)
                debts[next] -= debts[curr]

        return ret

    return helper(0)






