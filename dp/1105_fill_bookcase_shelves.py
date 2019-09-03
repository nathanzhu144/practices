# Nathan Zhu August 27th, 2019 10:57 pm
# Category: DP
# Google- On-Site Interview
# Your interview score of 7.03/10 beats 90% of all users.
# Time Spent: 1 hour 4 minutes 24 seconds
# Time Allotted: 2 hours


# Question:
# We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

# We want to place these books in order onto bookcase shelves that have total width shelf_width.

# We choose some of the books to place on this shelf (such that the sum of their thickness is 
# <= shelf_width), then build another level of shelf of the bookcase so that the total height
# of the bookcase has increased by the maximum height of the books we just put down.
# We repeat this process until there are no more books to place.



def minHeightShelves(books, shelf_width):
    """
    :type books: List[List[int]]
    :type shelf_width: int
    :rtype: int
    """
    n = len(books)
    dp = [float('inf') for _ in range(n + 1)]
    dp[0] = 0
    
    for i in range(1, n + 1):
        max_width = shelf_width
        max_height = 0
        j = i - 1
        
        # We continue while we can keep grabbing books for our new shelf.
        # 1. We still have books to grab j >= 0
        # 2. The books aren't too wide for our current shelf.
        while j >= 0 and max_width - books[j][0] >= 0:
            max_width -= books[j][0]
            max_height = max(max_height, books[j][1])
            dp[i] = min(dp[i], max_height + dp[j])
            j -= 1
            
    return dp[n]