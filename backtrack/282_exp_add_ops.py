# Nathan Zhu April 4th, 2020.  Damn, I did above average on the 376 final.  The binary search question was amazing.
# Leetcode 282 | hard | annoying
# Category: Backtracking
# 
# Thing I learned.  Suppose are trying to calculate a string of additions,
# multiplications, subtractions, but NO PARENS.
#
# If you do it greedily from left to right, you run into the problem where 1 - 2 * 3
# becomes 1 - 2 == -1 and -1 * 3 == -3.
# The right answer is -5
#
# What you do is you store a prev number that the multiplication is actually applied to
# called "multed."   A new multiplication gives the result:
#   tot - multed + currnum * numted
# Damn cool

def addOperators(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    def get_nums(num):
        ret = []
        def helper(i, currpath):
            N = len(num)
            if i == N:
                ret.append(currpath[:])
                return
            
            if num[i] == '0':
                helper(i + 1, currpath + ['0'])
            else:
                for j in range(1, N + 1):
                    if i + j > N: break
                    helper(i + j, currpath + [num[i:i+j]])
        helper(0, [])
        return ret
    
    def insert_ops(arr, target):
        ret = []
        def helper(i, currpath, multed, tot):
            if i == len(arr):
                if tot == target: ret.append("".join(currpath))
                return
            num = int(arr[i])
            
            # Damn this multiplication thing is tricky af
            helper(i + 1, currpath + ["+", arr[i]], num, tot + num)
            helper(i + 1, currpath + ["-", arr[i]], -num, tot - num)
            helper(i + 1, currpath + ["*", arr[i]], multed * num, tot - multed + num * multed)
            
            
        helper(1, [arr[0]], int(arr[0]), int(arr[0]))
        return ret
    if not num: return []
    ret = []
    for arr in get_nums(num):
        ret.extend(insert_ops(arr, target))
    return ret
                