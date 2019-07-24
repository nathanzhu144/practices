# Nathan Zhu, July 8th, 2019, 3:44 pm.  Amex tower 36th floor, Monday
# Renying and Wendy left yesterday.  Now I do leetcode.
#
#  So, we are given adj matrix of an undirected graph. Find number of friend circles.
#  If A is connected with B, and B is connected with C, A is connected with C.  A, B, C are all in same friend group
#
# 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
#
#  This is actually pretty similar to counting number islands, but each island are all friends
#  that are transitively connected to each other.  

def find_circle_num(adj_matrix):

    def dfs(n):
        for index, connected in enumerate(adj_matrix[n]):
            if connected and index not in seen:
                seen.add(index)
                dfs(index)

    num_fr_circle = 0
    seen = set()
    for i in range(len(adj_matrix)):
        if i not in seen:
            dfs(i)
            num_fr_circle += 1

    return num_fr_circle
