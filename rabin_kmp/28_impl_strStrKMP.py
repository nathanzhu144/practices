# Nathan Zhu May 30th, 2020.
# Leetcode 28 | easy | not easy
# Category: KMP
# I do this with KMP, but also can be done with rabin-karp


def strStr(string, pat):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    def helper(pat):
        N = len(pat)
        arr = [0] * N

        i, j = 1, 0
        while i < N:
            if pat[i] == pat[j]:
                arr[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = arr[j - 1]
                else:
                    j = 0
                    arr[i] = 0
                    i += 1
        return arr

    if not string or not pat:
        return -1 if pat else 0
    arr = helper(pat)
    i, j = 0, 0
    N = len(string)
    while i < N:
        if string[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = arr[j - 1]
            else:
                i += 1
        if j == len(pat): return i - len(pat)

    return -1