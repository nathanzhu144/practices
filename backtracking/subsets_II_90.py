    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, index, curr_path, returned):
            if index == -1:
                returned.append(curr_path[:])
                return
            
            helper(nums, index - 1, curr_path + [nums[index]], returned)
            helper(nums, index - 1, curr_path, returned)
        
        returned = list()
        helper(nums, len(nums) - 1, [], returned)
        process = list()
        
        for vec in returned:
            process.append(tuple(sorted(vec)))

        return list(set(process))
            