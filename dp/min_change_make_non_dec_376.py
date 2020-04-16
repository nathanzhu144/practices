# Nathan Zhu Feb 15th, 2020.  My birthday.  We are at tea ninja doing practice exams for 376.  This is a damn cool question.  I figured this
#                             question out on my own.  This was on a practice 376 exam.
# Leetcode n/a | n/a | medium
# Category: DP

# Given an array of integers, we can increase or decrease any integer.  The cost of inc/dec this integer is
# abs(new height - old height).  What's the min cost of making the array non-decreasing?
# 
# We memoize on two things [curr idx in arr, height all numbers to left of this idx have to be <= to]

def min_change(arr):
    max_h = max(arr)
    table = dict()
    def helper(i, k):
        if i < 0: return 0
        key = (i, k)

        ret = float('inf')
        for height in range(k + 1):
            ret = min(ret, abs(arr[i] - height) + helper(i - 1, height))

        table[key] = ret
        return ret

    return helper(len(arr) - 1, max_h)

if __name__ == "__main__":
    print(min_change([9, 9, 8]))
    print(min_change([8, 9, 8]))
    print(min_change([3, 4, 8]))