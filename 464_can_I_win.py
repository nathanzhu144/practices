    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        # if 1+2+3+....+maxChoosableInteger < desiredTotal, then no player can ever acquire desiredTotal, returning False
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

    def helper(self, nums, desiredTotal):
        """
        :param num:              available number pool
        :param desiredTotal:  desired total for victory
        """
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash] # if number pool is already evaluated, return memoized answer
        
        if nums[-1] >= desiredTotal:   # if available number pool has desiredTotal (at the end? why?), then we're winning (what about self.memo? why not setting True here?)
            return True
            
        for i in range(len(nums)):
            # pick each number in the number pool, and see using that if we attain desired Total
            if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]): # whats the meaning of this condition?? why is this  ( "not" self.helper())?
                self.memo[hash]= True
                return True
        self.memo[hash] = False
        return False

   def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        seen = {}

        def can_win(choices, remainder):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1] >= remainder:
                return True

            # if we have seen this exact scenario play out, then we know the outcome
            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]

            # we haven't won yet.. it's the next player's turn.
            # importantly, if we win just one permutation then
            # we're still on our way to being able to 'force their hand'
            for index in range(len(choices)):
                if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
                    seen[seen_key] = True
                    return True

            # uh-oh if we got here then next player won all permutations, we can't force their hand
            # actually, they were able to force our hand :(
            seen[seen_key] = False
            return False


        # note: usefully, choices is already sorted
        choices = list(range(1, maxChoosableInteger + 1))

        # let's do some quick checks before we journey through the tree of permutations
        summed_choices = sum(choices)

        # if all the choices added up are less then the total, no-one can win
        if summed_choices < desiredTotal:
            return False

        # if the sum matches desiredTotal exactly, then as
        # long as there is an odd number of choices then first player wins
        if summed_choices == desiredTotal and len(choices) % 2:
            return True

        # slow: time to go through the tree of permutations
        return can_win(choices, desiredTotal)
