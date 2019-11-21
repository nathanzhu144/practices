
def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def helper(candidates, target, index, curr_path, returned):
        if target ==  0: 
            returned.append(curr_path)
        if index < 0 or target < 0: return
        else:
            helper(candidates, target - candidates[index], index - 1, curr_path + [candidates[index]], returned)
            helper(candidates, target, index - 1, curr_path, returned)
    
    returned = []
    helper(candidates, target, len(candidates) - 1, [], returned)
    process = list()
    for vec in returned:
        process.append(tuple(sorted(vec)))
        
    return list(set(process))