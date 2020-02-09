# Nathan zhu Saturday January 10:08 pm Foundry Lofts aboutta go to bed
# Leetcode 282 | hard | kinda hard w edge cases
# Category: backtracking
#
# Edge cases: "105", target = 5,
# We don't want to use numbers like "05"
#
# Also, we need to consider order of ops for getting to target.
# 2 + 5 * 6 = 2 + 30 = 32
# To account for this, we pass in prev_val which is essentially last value, and we manipulate value as 
# value = value - prev_val + prev_val * tmp in multiplication recursive call

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []
        
        # We care about prev_val in cares of multiplication
        def helper(idx, path, value, prev_val):
            if idx == len(num) and value == target:
                ret.append("".join(path))
                return
            
            for i in range(idx + 1, len(num) + 1):
                # Handing the "05" edge case is done on this line
                if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
                    section = num[idx:i]
                    tmp = int(section)
                    if prev_val is None:
                        helper(i, [section], tmp, tmp)
                    else:
                        helper(i, path + ["+", section], value + tmp, tmp)
                        helper(i, path + ["-", section], value - tmp, -tmp)
                        helper(i, path + ["*", section], value - prev_val + prev_val * tmp, prev_val * tmp)
                        
        helper(0, [], 0, None)
        return ret
if __name__ == "__main__":
    print(addOperators("123", 6))