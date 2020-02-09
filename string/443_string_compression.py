

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    ret, idx = list(), 0
    
    # [a 4 b 2 c b c d d d e]
    #         Widx   0 1 2 3
    #                L     R
    # 
    # Visually widx keeps track of which index we have written to in the past
    # and is used to calculate where we will write in the future
    #
    # L, R are pointers used to find boundaries of the continuous subarrays
    # L, R are at or head widx.
    #
    # widx + 1 is length of final string
    
    widx = -1
    left, right = 0, 0
    
    if not chars: return 0

    while left < len(chars):
        while right < len(chars) and chars[left] == chars[right]:
            right += 1
            
        # writing in correct letter
        widx += 1
        chars[widx] = chars[left]
        
        # If length of subarray > 1, we need to write a number in.
        if right - left > 1:
            count = str(right - left)
            
            # in case we have "a b b b b b b b b b b b b"
            #            ret  "a b 1 2"
            #     NOT         "a b 12"
            for c in count:
                widx += 1
                chars[widx] = c
            
        left = right
        
    return widx + 1