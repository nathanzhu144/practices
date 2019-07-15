

#  [2, 1, 1, 1, 2, 2]
def remove_boxes(arr):
    # Takes in arr: [2, 1, 1, 1, 2, 2]
    #      indices   0  1  2  3  4  5
    # Returns:      [(0, 1), (1, 3), (4, 2)], form (start_i, number)
    # NOTE:  initializing cnt with 1 in beginning creates strange issues when only 1 val in arr
    def mark_boxes(arr):
        prev = arr[0]
        cnt = 0
        res = list()
        for i in range(0, len(arr)):
            # Need to do it for edge of arr, too
            if arr[i] != prev:
                res.append((i - cnt, cnt))
                cnt = 0
                prev = arr[i]
            cnt += 1
            if i == len(arr) - 1:
                res.append((i - cnt + 1, cnt))
        return res


    def helper(arr, mem):
        if not arr: return 0
        key = tuple(arr)
        if key in mem: return mem[key]

        ret = 0
        for start_i, num_box in mark_boxes(arr):
            ret = max(ret, helper(arr[:start_i] + arr[start_i + num_box:], mem) + num_box * num_box)
        mem[key] = ret
        return ret
    return helper(arr, dict())

if __name__ == "__main__":
    print(remove_boxes([2, 1, 1, 1, 2, 2]))