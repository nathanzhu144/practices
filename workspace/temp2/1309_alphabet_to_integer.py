# /* Nathan Zhu Friday July 24rd, 2020 5:34 am Stockton, CA.  Rak joined leetcode group yesterday.  Also, watching kissing booth 2 apparently.
# *  Leetcode 1309 | easy | easy
# *  Category: fizzbuzz
# */


def freqAlphabets(self, s):
    """
    :type s: str
    :rtype: str
    """
    N, i = len(s), 0
    ret = []
    while i < N:
        if i + 2 < N and s[i + 2] == '#':
            ret.append(chr(int(s[i:i+2]) + ord('a') - 1))
            i += 3
        else:
            ret.append(chr(int(s[i]) + ord('a') - 1))
            i += 1
            
    return "".join(ret)