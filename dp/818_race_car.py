# Nathan Zhu Nov 27th, 2019.  Going to Johnny's house with Renying today! I left for the dude at 6:20 in the morning
#                             and it is 9:49 pm, and I finally understand the DP version for this problem well enough
#                             to write about it.  It was raining heavily when I left, and my feet are wet.
# Leetcode 818 | hard | effing hard for DP, eZ for BFS
# Category: BFS / DP

import collections
import math

# This one is fucking cool man.
# There are several insights:
# 1. Assuming we keep moving forward, after moving forward n times, we have taken 2^(n-1) steps.
#    Ex. (pos, speed)
#        (0, 1) -> (1, 2) -> (3, 4) -> (7, 8) -> (15, 16) -> (31, 32) -> (2^6 - 1, 2^6) ...
# 
# 2. This one is hard to prove, but suppose we have a target, T.
#    Let n be log(T + 1, 2). 
#  
#    First, note that 2^(n - 1) < T < 2 ^(n)
#    
#    Ex. T = 254  Log(255, 2) = 7.988, so N = 8.    128 < 254 < 256
#        T = 255  Log(256, 2) = 8,     so N = 8.    128 < 255 < 256
#        T = 256  Log(257, 2) = 8.005  so N = 9.    256 < 257 < 512
# 
#    Then, there are 3 major cases.
#    
#    The optimal strategy will either: 
#      1. Case 1: AA...AA -> target
#         Only accelerating can reach target.
#         We move and 2 ** n - 1 == target.
#      
#      2. Case 2: We accelerate n times, and are past the target.
#         However, given how we calculated n, we are no farther than 2 * T.
#         
#         Thus, distance left is (2 ** (N - 1) - T)
#      3. Case 3: We accelerate n - 1 times, and are before the target.
#         Given how we calculated n, accelerating again would go past the target.
#         
#         Then, we reverse, and then accelerate m times where m ranges (0, n-2) inclusive.
#         
#         Finally, we reverse again, and have T - (2^(N - 1) - 2^M) distance left.
#
#     Hand-wavey part that this relies on.  An optimal path will first accelerate to 2^N or 2^N-1 first.
#     Thinking about cases makes this relatively convincing.
#
#     Suppose your target is 534, which is bigger than 512.  
#      
#     We could go to 511, 2^(n-1) - 1 first in 9 steps, leaving 23 units to go.
#     If we stopped at 255, 2^(n-2) - 1, we have taken 8 steps. In another 10 steps, we can get to 512,
#     We have to reverse, reverse, and walk another 8 steps.
#     However, if we just continued to 511 without stopping, we can get to 512 by reversing, reversing, and accelerating by 1.
#
#     Therefore, it seems pretty likely that this would work.

def racecar_DP(target):
    def helper(target, table):
        if target in table: return table[target]

        n = int(math.ceil(math.log(target + 1, 2)))

        if 2 ** n - 1 == target:
            return n

        # At this point, we know 2^n - 1 is strictly greater than target
        # n steps because we have moved n steps to get past target
        # 1 step for reverse
        # Therefore, we have 2 ** n - 1 - target steps left to target
        ret = n + 1 + helper(2 ** n - 1 - target, table)

        # Now we assume that we first move 2^(n - 1) - 1 steps, which must be strictly
        # less than target, we reverse m times where m < n - 1, and walk backwards 2^(m - 1) -1 steps,
        # reverse again, and we have...
        # target - (2^(n - 1) - 2^m steps left.  Note: the -1s cancel out from subtraction
        # n - 1 for n - 1 steps
        # 1 for reversing
        # m for m steps.
        # 1 for reversing
        for m in range(n - 1):
            curr = (n - 1) + 1 + m + 1 + helper(target - (2 ** (n - 1) - 2 ** m), table)
            ret = min(ret, curr)

        table[target] = ret
        return ret
    return helper(target, dict())



# This one is simple, but runtime is O(2^N)
# Just normal BFS with some pruning.
def racecar_BFS(target):
    """
    :type target: int
    :rtype: int
    """
       
    Pos = collections.namedtuple('Pos', ['position', 'speed'])

    q  = [Pos(0, 1)]
    ret = 0
    visited = set()

    while q:
        new_q = []
        while q:
            curr = q.pop()
            if curr in visited: continue
            visited.add(curr)
            if curr.position == target: return ret
            
            # We try to prune all positions where we will be greater than 2 * T for obvious reasons
            # Removing this will make it too slow to pass all test cases.
            if abs(curr.position + curr.speed) < target * 2:
                new_q.append(Pos(curr.position + curr.speed, curr.speed * 2))
            new_q.append(Pos(curr.position, curr.speed / abs(curr.speed) * -1))

        q = new_q
        ret += 1

    return ret


if __name__ == "__main__":
    print(racecar_DP(6))