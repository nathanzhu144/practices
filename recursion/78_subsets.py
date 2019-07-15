# Nathan Zhu,  10:08 am


def power_set(arr):
    # For every step, we either add onto current path or do not. 
    # When index >= len(curr_path), we add the set onto returned
    def helper(arr, index, curr_path, returned):
        if index >= len(arr):
            returned.append(curr_path)
            return
        helper(arr, index + 1, curr_path + [arr[index]], returned)
        helper(arr, index + 1, curr_path, returned)
    
    ret = list()
    helper(arr, 0, list(), ret)
    return ret

if __name__ == "__main__":
    print(power_set([1, 2, 3]))


