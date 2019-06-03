
## simple longest palindromic subsequence
def lps(arr, i, j):
    if i == j:
        return 1
    if j - i == 1:
        if arr[i] == arr[j]:
            return 2
        else:
            return 1
    
    if arr[i] == arr[j]:
        return 2 + lps(arr, i + 1, j - 1)
    else:
        return max(lps(arr, i + 1, j), lps(arr, i, j - 1))




if __name__ == "__main__":
    list1 = [7, 5, 23, 1, 3, 2, 2, 31, 3, 1, 33, 5, 34, 7] #[7 5 1 3 2 2 3 1 5 7]
    print(lps(list1, 0, len(list1) - 1)) # should be 10
    list2 = [7] 
    print(lps(list2, 0, len(list2) - 1)) # should be 1
    list3 = [7, 2] 
    print(lps(list3, 0, len(list3) - 1)) # should be 1
    list4 = [7, 7] 
    print(lps(list4, 0, len(list4) - 1)) # should be 2
    list5 = [7, 1, 7] 
    print(lps(list5, 0, len(list5) - 1)) # should be 3
