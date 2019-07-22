# Nathan Zhu Amex Floor 36th, Sunday July 21st, 2019. 
# Leetcode 4 | Hard | Man...
#
# So, there are some insights here:
#
# ...
#  https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation

def find_median_two_sorted(A, B):
    m = len(A)
    n = len(B)
    if m > n: return find_median_two_sorted(B, A)

    left, right = 0, m
    while left <= right:
        i = (right - left) // 2 + left
        j = (m + n + 1) // 2 - i

        A_left = float('-inf') if i == 0 else A[i - 1]
        B_left = float('-inf') if j == 0 else B[j - 1]
        A_right = float('inf') if i == m else A[i]
        B_right = float('inf') if j == n else B[j]

        # We want A_left <= B_right, so in this case decrease i
        if A_left > B_right:
            right = i - 1
        elif B_left > A_right:
            left = i + 1
        else:
            max_left = max(A_left, B_left)
            min_right = min(A_right, B_right)

            #If it is odd:
            if ((m + n) % 2 == 1): return max_left
            else: return (max_left + min_right) / 2.0

