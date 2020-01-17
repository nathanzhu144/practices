# Nathan Zhu Sunday Jan 12th, 2020
# Leetcode 1062 | medium | hard
# The average time NlogN soln is pretty hard IMO
# It involves a binary search + rabin karp rolling hash.

PRIME = 10 ** 9 + 7
BASE = 26
def longestRepeatingSubstring(self, S):
    """
    :type S: str
    :rtype: int
    """
    # Idea behind Rabin-Karp rolling hash is for each substring we calculate a 
    # hash value that can be "rolled" esily.
    # 
    #        [A   D   O   G ]
    #         97 100 111 103
    #   idx   0   1   2   3
    # "ADO" ->   97 * 26^2 + 100 * 26 + 100
    # "DOG" = ("ADO" - 97 * 26 ^ 2) * 26 + 103
    # We can go from "ADO" to "DOG" with:
    #  1 subtraction
    #  1 multiplication by 26
    #  1 addition
    # Essentially O(1)
    #
    # Therefore, this is a hash we can "roll through" a string in O(N) time.
    # NOTE: WE mod everything by a large prime to keep an even distribution of numbers because most numbers are coprime to large primes.
    def helper(S, lenstr):
        bigbase = 26 ** (lenstr - 1) % PRIME
        
        curr = 0
        for char in S[:lenstr]: curr = (curr * 26 + ord(char)) % PRIME
        table = collections.defaultdict(list)
        table[curr].append(0)
        
        for i, ch in enumerate(S[lenstr:], lenstr):
            curr -= (bigbase * ord(S[i - lenstr])) % PRIME
            curr = (curr * 26 + ord(S[i])) % PRIME
            if curr in table:
                for sidx in table[curr]:
                    if S[i - lenstr + 1: i + 1] == S[sidx: sidx + lenstr]: return True
            table[curr].append(i - lenstr + 1)
            
        return False
    ret = 0
    left, right = 0, len(S)
    
    while left <= right:
        mid = (right - left) // 2 + left
        print(mid)
        if helper(S, mid):
            ret = mid
            left = mid + 1
        else: right = mid - 1
            
    return ret