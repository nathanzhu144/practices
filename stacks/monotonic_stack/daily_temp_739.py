    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        returned = []
        stack = collections.deque(list())
        
        #
        for i in range(len(T) - 1, -1, -1):
            # 
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            
            if not stack: returned.append(0)
            else: returned.append(stack[-1] - i)
            
            stack.append(i)
        
        return returned[::-1]
            