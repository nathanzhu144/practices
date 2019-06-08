class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if set(list(s1) + list(s2)) != set(list(s3)):
            return False
        
        def helper(s1, s2, target, s1_index, s2_index, target_index, mem):
            key = (s1_index, s2_index)
            
            if key in mem:
                return mem[key]
            if target_index == -1 and s1_index == -1 and s2_index == -1:
                return True
            
            if target_index == -1:
                if s1_index != -1 or s2_index != -1:
                    return False
            
            if target_index != -1:
                if s1_index == -1 and s2_index == -1:
                    return False
            
            if s1_index == -1 and s2_index != -1:
                return s2[:s2_index + 1] == target[:target_index + 1]
            
            if s2_index == -1 and s1_index != -1:
                return s1[:s1_index + 1] == target[:target_index + 1]
            
            
            if target[target_index] == s1[s1_index] or target[target_index] == s2[s2_index]:
                if target[target_index] == s1[s1_index] and target[target_index] == s2[s2_index]:
                    return helper(s1, s2, target, s1_index - 1, s2_index, target_index - 1, mem) or \
                           helper(s1, s2, target, s1_index, s2_index - 1, target_index - 1, mem)
                
                if target[target_index] == s1[s1_index]:
                    return helper(s1, s2, target, s1_index - 1, s2_index, target_index - 1, mem)
                
                if target[target_index] == s2[s2_index]:
                    return helper(s1, s2, target, s1_index, s2_index - 1, target_index - 1, mem)
                
            return False
        
        return helper(s1, s2, s3, len(s1) - 1, len(s2) - 1, len(s3) - 1, {})