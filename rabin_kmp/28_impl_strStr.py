# Nathan Zhu Friday January 17th, 2020, 3:47 pm Duderstadt basement, next to 376 OH
# Leetcode 28 | easy | not to easy
# Category: Rabin-Karp rolling hash / KMP
#
# Didn't use KMP, but most people do.

# Pretty sure the collision checking works, as when I changed the PRIME from 10 ** 9 + 7 
# to 7, I still passed all the test cases correctly.

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle: return 0
    
    PRIME = 10 ** 9 + 7
    hash1, hash2 = 0, 0
    N, H = len(needle), len(haystack)
    BASE = 10 ** (N - 1)

    for c in needle: hash1 = (hash1 * 10 + ord(c)) % PRIME

    for i, c in enumerate(haystack):
        if i - N >= 0:
            delnumber = ord(haystack[i - N]) * BASE
            hash2 = (hash2 - delnumber) % PRIME
        hash2 = (hash2 * 10 + ord(c)) % PRIME

        if hash1 == hash2 and needle == haystack[i - N + 1: i + 1]: return i - N + 1

    return -1

if __name__ == "__main__":
    print(strStr("miss", "iss"))