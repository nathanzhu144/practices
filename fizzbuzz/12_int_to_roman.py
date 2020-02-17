def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    nums    = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    returned = []
    
    i = 0
    while num != 0:
        if num / nums[i] == 0: 
            i += 1
            continue
        returned.append(symbols[i])
        num -= nums[i]
    
    return "".join(returned)