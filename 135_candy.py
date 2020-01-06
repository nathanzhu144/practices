# Nathan Zhu 7:50 pm December 25th, 2019, Christmas Day after giving presents
# Leetcode 135 | hard | yeah not too easy
# Category: Misc tricks
# Runtime : O(N) space O(N)
#

def candy(ratings):
    # Note that 2 children sitting next to each other w same rating may not get
    # the same number of candies.
    #
    # We can easily enforce both of these rules with 1 pass from left
    # and 1 pass from right.
    #
    # In pass from left we give all children with a lower rating on their left 1 candy
    # more than the left child.
    #
    # In pass from right we give all children with a lower rating on their right 1 candy
    # more than right child.  When we assign to candy[i], we take the maximum of candy[i] and 
    # the new candy amount, as we may have assigned that child more candy on the left pass.
    # 
    # 
    if len(ratings) < 1: return len(ratings)
    
    candy = [1] * len(ratings)
    
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]: candy[i] = candy[i - 1] + 1
        
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]: candy[i] = max(candy[i], candy[i + 1] + 1)
            
    return sum(candy)