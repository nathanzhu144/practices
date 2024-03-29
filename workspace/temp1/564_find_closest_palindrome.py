# Nathan Zhu June 16th, 2020 9:22 pm Stockton, CA.  Called Mahammadou (sp?) today.  Haven't seen him in so long, a bit less than a yaer.  He's at BAC now in NY.
# Leetcode 795 | medium | medium
# Category: DP
#
# There's a kinda cool counting argument too with inclusion exclusion
# This DP solution is REALLY smart though

# Case 1:
# 
# One candidate is copying the left side over to right side
# 12367 -> 12321
# Why don't we cop right to left too?  Obviously, the left prefix being the same
# will give us a closer number than the right suffix being the same.
# Ex. 12321 is closer to 12367 than 76321 is to 12367
#     12367 -> 12321
# 
# Case 2:
# Another candidate is incrementing or decrementing the middle digit by one.
# This can give us a closer candidate.
# Ex. 8881111 -> 8880888 (closer, generated by decrementing middle before coping left to right)
#     8881111 -> 8881888 (farther, generated by copying left to right side)
#                8881111 (original)
# 
# Conversely, sometimes incrementing can give a closer digit as well
# Ex. 1118888 -> 1119111 (closer, generated by incrementing middle before copying left to right)
#     1118888 -> 1118111 (farther, generated by copying left to right side)
#                1118888 (original)
# 
# WE ONLY INCREMENT BY 1.  Think about it; the one where you increment by one or decrment by one will
# always be closer to original than any other increment and decrement values
#
# 
# Case 3: 
# Another candidate is taking the nearest 999 to the candidate.
# Ex. For 1000, 999 is correct as compared to 1001; while both are same dist, 999 is closer.
def nearestPalindromic(self, n):
    """
    :type n: str
    :rtype: str
    """
    N = len(n)
    cand = set(["9" * (N - 1), str(10 ** N + 1)])
    for diff in [-1, 0, 1]:
        prefix = str(int(n[:(N + 1) // 2]) + diff)
        if N & 1: cand.add(prefix + prefix[:-1][::-1])
        else: cand.add(prefix + prefix[::-1])
    cand.discard(n)
    cand.discard("")
    cand = sorted(list(map(int, cand)), key=lambda x: (abs(int(n) - x), x))
    return str(cand[0])