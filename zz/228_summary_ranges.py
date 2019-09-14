Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

def summaryRanges(self, nums):
    if not nums:
        return []
    res, i, start = [], 0, 0
    while i < len(nums)-1:
        if nums[i]+1 != nums[i+1]:
            res.append(self.printRange(nums[start], nums[i]))
            start = i+1
        i += 1
    res.append(self.printRange(nums[start], nums[i]))
    return res

def printRange(self, l, r):
    if l == r:
        return str(l)
    else:
        return str(l) + "->" + str(r)