## simple longest palindromic subsequence


def helper(mem, arr, i, j):
    if mem.has_key((i, j)):
        return mem[(i, j)]

    if i == j:
        mem[(i, j)] = 1

    elif j - i == 1:
        if arr[i] == arr[j]:
            mem[(i, j)] = 2
        else:
            mem[(i, j)] = 0
    
    elif arr[i] == arr[j]:
        if helper(mem, arr, i + 1, j - 1) == 0:
            mem[(i, j)] = 0
        else:
            mem[(i, j)] = 2 + helper(mem, arr, i + 1, j - 1)
    else:
        mem[(i, j)] = max(helper(mem, arr, i + 1, j), helper(mem, arr, i, j - 1))
    
    return mem[(i, j)]


def lpsubstring(arr):
    mem = {}
    helper(mem, arr, 0, len(arr) - 1)
    starting_index = -1
    ending_index = -1
    substring_len = 0

    print(mem)

    for key in mem:
        if key[1] - key[0] > substring_len:
            substring_len = key[1] - key[0]
            starting_index = key[0]
            ending_index = key[1]

    return arr[starting_index : ending_index]

if __name__ == "__main__":
    print(lpsubstring([1, 2, 3, 2, 4]))
