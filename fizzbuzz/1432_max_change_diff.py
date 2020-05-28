# Nathan Zhu May 2nd, 2020. biweekly contest
# Leetcode 1432 | medium | medium
# Category: Fizzbuzz, honestly could've done it more cleanly with brute-force


def maxDiff(s):
    def replacesmall(s, substitute):
        arr = list(str(s))
        N, i = len(arr), 0
        victim = None

        while i < N:
            if substitute == '0' and s[i] == s[0]:
                i += 1
                continue
            if s[i] <= substitute: 
                i += 1
            else:
                victim = arr[i]
                while i < N:
                    if arr[i] == victim:
                        arr[i] = substitute
                    i += 1
        return "".join(arr)

    def replacebig(s, substitute):
        arr = list(str(s))
        N, i = len(arr), 0
        victim = None

        while i < N:
            if substitute == '0' and s[i] == s[0]:
                i += 1
                continue
            if s[i] == substitute: 
                i += 1
            else:
                victim = arr[i]
                while i < N:
                    if arr[i] == victim:
                        arr[i] = substitute
                    i += 1
        return "".join(arr)

    small = replacesmall(str(s), '0')
    other = replacesmall(str(s), '1')
    if int(other) < int(small):
        small = other
    return int(replacebig(str(s), '9')) - int(small)