
#   Unique binary search trees
#   Nathan Zhu 55th John Street, Saturday June 8th, 2019. 9:03 pm
#   First weekend of internship.  It is nice to not have hw at school
#   
#  This is actually a dp question, and you do not need to go thru
#  generating all the possibilities.
# 
#  Let N(n) be number of unique binary trees from 1..n
#  F(i, n) be the number of unique BSTS where number is the root of BST
#  and sequence ranges from 1 to n
#
#  Note that N(n) = F(1, n) + F(2, n) + .. + F(n,n)
#  Also...
#  N(0) is 1
#  N(1) is 1
#  N(2) is 2
#
#          1           2
#           \         /
#            2       1
#  N(3) is 5
# 
#        3    3    2    1       1 
#       /    /    / \    \       \
#      2     1   1  3     2       3
#      /      \           \       /
#     1        2           3     2
#  
# 
#  Let's look at a calculation like F(3, 7)
#
#          3
#        /   \ 
#     [1, 2]  [4, 5, 6, 7]
# 
#   So F(3, 7) is just N(2) * N(4)
# 
#  
#  Therefore...
#
#  N(5) = F(1, n) + F(2, n) + F(3, n) + F(4, n) + F(5, n)
#        = N(0) * N(n - 0 - 1) + N(1) * N(n - 1 - 1) + N(2) * N(n - 3) + N(3) * N(n - 4) + N(4) * N(n - 5)
#        = ...
#  

def unique_binary_trees(n):
    def helper(n, mem):
        if n in mem:
            return mem[n]

        if n == 0 or n == 1:
            return 1

        sum = 0
        for i in range(0, n):
            sum += helper(i, mem) * helper(n - i - 1, mem)
        
        mem[n] = sum
        return mem[n]

    return helper(n, {})

print(unique_binary_trees(4))