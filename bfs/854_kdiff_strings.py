#  Nathan Zhu 8:34 am, Amex Tower, New York NY.  June 20th, 2019
#  This is a damn hard problem.  Leetcode 854 | I think damn hard
#
#  I don't know if I completely buy its correctness.  The thing I'm not sure I believe is:
#
#  Suppose str1 and str2 differ at index i.  
#  Let's define j s.t. i < j < len(str2) = len(str1)
#
#  At least one of the j's for which swapping i and j make str1 and str2 not differ at index i
#  yields the fewest number of swaps.  (WHY IS THIS TRUE)
#
#  We 
# 
#  I agree that there are worse paths, as the number of differences between str1 and str2 decreases
#  by at least one.
#
# 
#  This could be why ...  Because in the optimal solution, swapping (a,b) does not effect (c,d), 
#                         otherwise you can always find a shorter path, hence the order doesn't matter.
#                         You can swap the last pair you see and it returns the same result. 
#
#
#  Anyway, intuition is that this is a BFS graph problem.  
#
#  We start with str1, and go to first index, i where str1 and str2 are different
#  Let's define j s.t. i < j < len(str2) = len(str1)
#
#  We generate all new strings where we swap j with i to  make str1 and str2 not differ at index i,
#  and push them to the queue if they are not visited.  
#
#  We then do the BFS thing.
#  
#  
#  NOTE: Seen map doubles as a visited, but also as a map from a string -> number swaps it took to get there
#        from str1
import collections

def kdiff(str1, str2):
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    # Returns all neighbors of a string
    def get_neighbors(string):
        # find char at which they differ
        for index, char in enumerate(string):
            if char != str2[index]:
                break

        string_list = list(string)

        #  Suppose str1 and str2 differ at index i.
        #  Let i < j < len(str2) = len(str1)
        #  yields all possible swaps between i and j s.t. str1 and str2 no longer differ at index i
        for i in range(index + 1, len(string_list)):
            if string[i] == str2[index]:
                string_list[i], string_list[index] = string_list[index], string_list[i]
                yield "".join(string_list)
                string_list[index], string_list[i] = string_list[i], string_list[index]


    q = collections.deque([str1])
    seen = {str1: 0}                 # maps string -> num swaps
    while q:
        curr = q.popleft()
        if curr == str2: return seen[curr]
        for possible in get_neighbors(curr):
            if possible not in seen:
                seen[possible] = seen[curr] + 1  # possible is 1 more swap than curr
                q.append(possible)

    return float('inf')  # should never get here

