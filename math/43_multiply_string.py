# Nathan Zhu Saturday January 4th, 2019 1:49 pm Think I'm sick today.
# Leetcode 43 | medium | medium
# Category: Math/misc tricks
# 

def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    arr = [0] * (len(num1) + len(num2))
    
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    for i in range(len(num1)):
        for j in range(len(num2)):
            prod = int(num1[i]) * int(num2[j])
            
            arr[i + j] += prod % 10
            arr[i + j + 1] += prod // 10
            
            idx = 0
            
            # To flatten out the carries we may get.
            # We don't worry about out of bounds
            while arr[i + j + idx] > 9:
                num = arr[i + j + idx]
                arr[i + j + idx] = num % 10
                arr[i + j + idx + 1] += num // 10
                idx += 1
    
    # We need to still get rid of leading zeroes in array
    final_w_zero = "".join(map(str,arr[::-1]))
    zidx = 0
    
    
    while zidx < len(final_w_zero):
        if final_w_zero[zidx] != "0": break
        zidx += 1
    # If our final res is 0, we still have to return 0, so beware of that.
    if zidx == len(final_w_zero): return "0"
    else: return final_w_zero[zidx:]
        
                
        
        