#  Nathan Zhu, American Exp tower, New York, Manhattan, got rained on the way here
#  Leetcode 17 | medium | I think easy
#  Tuesday June 25th, 2019, 7:56 am, this is literally the easiest
#                                    backtracking problem you can ge.

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    mapping = { 
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    if not digits: return [] 
    
    def helper(digits, curr_index, curr_path, returned):
        if curr_index == len(digits):
            returned.append("".join(curr_path))
            return
        
        for letter in mapping[digits[curr_index]]:
            helper(digits, curr_index + 1, curr_path + [letter], returned)
            
    returned = []
    helper(digits, 0, [], returned)
    return returned