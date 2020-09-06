import collections

def maxSubstring(s):
    mchar = max(list(s))
    for i in range(len(s)):
        if s[i] == mchar: return s[i:]
    return ""


def getMinimumUniqueSum(arr):
    ret, num = 0, 0
    arr.sort()
    for nextnum in arr:
        ret += max(num - nextnum, 0)
        num = max(num + 1, nextnum + 1)
    return ret + sum(arr)

# 1, 2, 2
# 
def getNumTriples(arr, target):
    arr.sort()
    ret, N = 0, len(arr)

    i = 0
    while i < N:
        j = i + 1
        while j < N:
            k = j + 1
            while k < N:
                if arr[i] + arr[j] + arr[k] <= target:
                    ret += 1
                    print([arr[i], arr[j], arr[k]])
                while k + 1 < N and arr[k] == arr[k + 1]: k += 1
                k += 1
            while j + 1 < N and arr[j] == arr[j + 1]: j += 1
            j += 1
        while i + 1 < N and arr[i] == arr[i + 1]: i += 1
        i += 1
    return ret

if __name__ == "__main__":
    #print(getNumTriples([1, 2, 3, 3, 3, 3, 4, 3, 3, 3, 5], 8))
    #assert(getMinimumUniqueSum([3, 2, 1, 2, 7]) == 17)
    print(getMinimumUniqueSum([3, 1, 2, 2]))


    assert(maxSubstring('baca') == 'ca')