# Nathan Zhu April 1st, 2020.  Foundry Lofts, final week, COVID-19
# Leetcode 1220 | hard | nt bad,
# Category: DP
# Runtime: O(N), possible O(logN) with big brain
# Similar problem: Knight's dialer.


def countVowelPermutation(n):
    """
    :type n: int
    :rtype: int
    """
    #     Transition function
    #         a -> e
    #         e -> a
    #         e -> i

    #         i -> a
    #         i -> e
    #         i -> o
    #         i -> u

    #         o -> i
    #         o -> u

    #         u -> a
    CONST = 10 ** 9 + 7
    table = dict()
    table["a"] = "e"
    table["e"] = "ai"
    table["i"] = "aeou"
    table["o"] = "iu"
    table["u"] = "a"
    mem = dict()
    def helper(first_ch, i):
        key = (first_ch, i)
        if key in mem: return mem[key]
        
        if i == 1: return 1
        ret = 0
        for neigh in table[first_ch]:
            ret += helper(neigh, i - 1)
        mem[key] = ret % CONST
        return ret
    
    ret = 0
    for ch in "aeiou": ret = (ret + helper(ch, n)) % CONST
    return ret 
            
