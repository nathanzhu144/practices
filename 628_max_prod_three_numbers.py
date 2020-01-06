# Nathan Zhu 7:27 am Sunday Sept 27th, 2019, going to winchester today
# Leetcode 628 | easy | cool idea
# 
# Maximum prod of 3 numbers is these two. 
# 1st largest * 2nd largest * 3rd largest
# smallest num * 2nd smallest num * 1st largest
#
# I have never found multiple maximums before, and that was kinda cool.  
def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    top1, top2, top3 = float('-inf'), float('-inf'), float('-inf')
    bot1, bot2 = float('inf'), float('inf')
    for num in nums:
        if num >= top1:
            top3 = top2
            top2 = top1
            top1 = num
        elif num >= top2:
            top3 = top2
            top2 = num
        elif num >= top3:
            top3 = num
            
        
        if num <= bot1:
            bot2 = bot1
            bot1 = num
        elif num <= bot2:
            bot2 = num
            
            
    return max(bot1 * bot2 * top1, top1 * top2 * top3)