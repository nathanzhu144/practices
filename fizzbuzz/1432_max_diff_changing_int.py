# Nathan Zhu April 2nd, 2020 Biweekly contest
# Leetcode 1432 | medium | yucky code
# Category: fizzbuzz
# 
# Damn this code was ugly. 
# I saw other ppl write much cleaner code by just brute forcoing it.
# Might be a better alternative.


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