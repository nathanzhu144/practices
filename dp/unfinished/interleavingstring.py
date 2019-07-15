class Solution(object):
    #  Saturday June 15th, 2019, 11:29 pm Chicago time, Chicago
    #  * -- D -- * -- O -- * -- G -- *
    #  |         |         |         |
    #  B         B         B         B
    #  |         |         |         |
    #  * -- D -- * -- O -- * -- G -- *
    #  |         |         |         |
    #  U         U         U         U
    #  |         |         |         |
    #  * -- D -- * -- O -- * -- G -- *
    #  |         |         |         |
    #  G         G         G         G
    #  |         |         |         |
    #  * -- D -- * -- O -- * -- G -- *
    #
    #  DFS solution.
    #
    #  Starting from position (0, 0) in the graph, if you can get to position (3, 3) and have
    #  both strings be empty, then you know s1 and s2 interleave to get s3.
    #
    #  Note that an easy way to make sure that if both strings are empty is to check if len(s1) + len(s2) == len(s3)
    #  That way if you ever reach the end position (3, 3), you know that you have found that s1 and s2 interleave to s3.
    #
    

def is_interleave_bfs(s1, s2, target):
    if len(s1) + len(s2) != len(target):
        return False

    BFS_curr = [(0, 0)]
    BFS_next = []
    visited = set((0, 0))

    while BFS_curr:
        while BFS_curr:
            front = BFS_curr.pop(0)
            x, y = front

            if (x, y) == (len(s1), len(s2)):
                return True
            if x + 1 <= len(s1) and (x + 1, y) not in visited and s1[x] == target[x + y]:
                BFS_next.append((x + 1, y))
                visited.insert((x + 1, y))
            if y + 1 <= len(s2) and (x, y + 1) not in visited and s1[y] == target[x + y]:
                BFS_next.append((x, y + 1))
                visited.insert((x, y + 1))

        BFS_curr = BFS_next[:]
        BFS_next = list()

    return False
            

# Note that we have to recompute the same problem with str1 and str2 multiple times. So, we use 
# mem to store past results.
def is_interleave_dp(s1, s2, target):
    # This ensures that we don't have to do checks for if s1 & s2 are empty, but target not empty.
    #     target is empty <-> s1 & s2 are empty
    # Saves us ugly base cases
    if len(s1) + len(s2) != len(target): return False

    def helper(s1, s2, target, s1_index, s2_index, target_index, mem):
        key = (s1_index, s2_index)
        if key in mem: return mem[key]
        
        # If s1 or s2 become empty, see remaining of other string is equal to target
        if s1_index == -1: return s2[:s2_index + 1] == target[:target_index + 1]
        if s2_index == -1: return s1[:s1_index + 1] == target[:target_index + 1]

        # We CAN return true in two cases.  Note that both cases can happen, and both can lead to a correct interleaving
        mem[key] = False
        # 1. string_1 has the same last char as target string
        # 2. string_2 has the same last char as target string
        if s1[s1_index] == target[target_index]: mem[key] = mem[key] or helper(s1, s2, target, s1_index - 1, s2_index, target_index - 1, mem)
        if s1[s2_index] == target[target_index]: mem[key] = mem[key] or helper(s1, s2, target, s1_index, s2_index - 1, target_index - 1, mem)
        
        return mem[key]
    return helper(s1, s2, target, len(s1) - 1, len(s2) - 1, len(target) - 1, {})
            


#  Lol, so for this implementation, I literally forgot to memoize, so I kept getting TLE.  I was super frustrated.
#  I got some insights on how to write the code cleaner, so I rewrote, and it ended up being faster than 94% of all python submissions...
#  Plus, I decreased LoC by 50$
# def isInterleave(self, s1, s2, s3):
#     """
#     :type s1: str
#     :type s2: str
#     :type s3: str
#     :rtype: bool
#     """
#     if set(list(s1) + list(s2)) != set(list(s3)):
#         return False
    
#     def helper(s1, s2, target, s1_index, s2_index, target_index, mem):
#         key = (s1_index, s2_index)
        
#         if key in mem:
#             return mem[key]
#         if target_index == -1 and s1_index == -1 and s2_index == -1:
#             return True
        
#         if target_index == -1:
#             if s1_index != -1 or s2_index != -1:
#                 return False
        
#         if target_index != -1:
#             if s1_index == -1 and s2_index == -1:
#                 return False
        
#         if s1_index == -1 and s2_index != -1:
#             return s2[:s2_index + 1] == target[:target_index + 1]
        
#         if s2_index == -1 and s1_index != -1:
#             return s1[:s1_index + 1] == target[:target_index + 1]
        
        
#         if target[target_index] == s1[s1_index] or target[target_index] == s2[s2_index]:
#             if target[target_index] == s1[s1_index] and target[target_index] == s2[s2_index]:
#                 return helper(s1, s2, target, s1_index - 1, s2_index, target_index - 1, mem) or \
#                         helper(s1, s2, target, s1_index, s2_index - 1, target_index - 1, mem)
            
#             if target[target_index] == s1[s1_index]:
#                 return helper(s1, s2, target, s1_index - 1, s2_index, target_index - 1, mem)
            
#             if target[target_index] == s2[s2_index]:
#                 return helper(s1, s2, target, s1_index, s2_index - 1, target_index - 1, mem)
            
#         return False
    
#     return helper(s1, s2, s3, len(s1) - 1, len(s2) - 1, len(s3) - 1, {})