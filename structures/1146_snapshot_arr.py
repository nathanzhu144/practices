# Nathan Zhu Aug 27th 2019 2:14 am at Stockton Cali
# Leetcode 1146 | medium | I think not too bad
# Category: System design, binary search
# 
# Done in real-time in a "google phone interview", time limit 1hr 30 for 2 questions
# Rating was 7.69/10, beating 92% of all users.
# 
class SnapshotArray(object):
    
    def __init__(self, length):
        """
        :type length: int
        """
        self.vals = [[[-1, 0]] for i in range(length)]
        self.snap_idx = 0
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        #  we take last snapshot at index, and look at the snapshot val of it
        if self.vals[index][-1][0] == self.snap_idx:
            self.vals[index][-1][1] = val
        else:
            self.vals[index].append([self.snap_idx, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snap_idx += 1
        return self.snap_idx - 1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # So, the goal here is to find the first snapshot before or at snap_id,
        # We are trying to find the biggest less than or eq a number.
        
        left, right = 0, len(self.vals[index]) - 1
        ret = -1  # in this case, it can be anything cause it is not possible for all values in arr
                  # to be greater than snap_id
        while left <= right:
            mid = (right - left) // 2 + left
            if self.vals[index][mid][0] <= snap_id:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return self.vals[index][ret][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)