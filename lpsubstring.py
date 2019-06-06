## simple longest palindromic subsequence


def expand(arr, i, j):
    while i > 0 and j < len(arr) and arr[i] == arr[j]:
        i -= 1
        j += 1
    return (i + 1, j - 1)

def findlongestpalindromicsubstring(arr):
    longest = []
    
    for index in range(len(arr)):
        i = expand(arr, index, index)[0]
        j = expand(arr, index, index)[1]
        if j - i > len(longest):
            longest = arr[i : j + 1]
    
    return longest






    # starting_index = -1
    # ending_index = -1
    # substring_len = -1

    # #print(mem)

    # for key in mem:
    #     if key[1] - key[0] > substring_len:
    #         substring_len = key[1] - key[0]
    #         starting_index = key[0]
    #         ending_index = key[1]

    # return arr[starting_index : ending_index]

if __name__ == "__main__":
    print(findlongestpalindromicsubstring([1, 2, 2, 3]))     #should be 3
