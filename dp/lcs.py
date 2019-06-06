

# top-down memoized LCS
#  
# Classic problem.
#  
# June 4th, 2019, 55th John Street, New York 8:24 pm
# 
#  This is a variation of minimum edit distance between two strings, except
#  with just deletion and insertion.
#
#  There are 2 cases:
#   
#     1. If list1 and list2 have the same last character, 
#             lcs(????A, ??????A) = 1 + lcs(????, ??????)
#
#     2. If list1 and list2 have different last char, clearly a LCS cannot contani
#        both of the different last characters, so a LCS is this:
#              lcs(????B, ??????A) = max(lcs(????, ??????A), lcs(????B, ??????)
#
#   Base case is that if either string is empty, LCS is empty string.
#
def helper(mem, list1, list2, index1, index2):
    if mem.has_key((index1, index2)):
        return mem[(index1, index2)]

    if index1 < 0 or index2 < 0:
        mem[(index1, index2)] = 0
    elif list1[index1] == list2[index2]:
        mem[(index1, index2)] = helper(mem, list1, list2, index1 - 1, index2 - 1) + 1
    else:
        mem[(index1, index2)] = max(helper(mem, list1, list2, index1 - 1, index2),
                                    helper(mem, list1, list2, index1, index2 - 1))    
    return mem[(index1, index2)]

def lcs(list1, list2):
    return helper({}, list1, list2, len(list1) - 1, len(list2) - 1)
    
if __name__ == "__main__":
    print(lcs(['n', 'e', 'm', 'a', 't', 'o', 'd'], ['e', 'm', 'p', 't', 'y']))