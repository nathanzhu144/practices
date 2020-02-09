# Nathan Zhu Friday January 17th, 2020 11:45 pm Duderstadt Basement next to 376 OH doing proof of karatsuba algo.
# Leetcode 274 | medium | hard-ish
# Category: Counting sort
# This one is not-so-simple to do in O(N) time

def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    # Insights:
    # 1. We don't need to do a comparison-based sort, as there are 2 ways to come to this conclusion.  
    #    - H-index is bounded by number of papers they write
    #    - H-index is usually a small number, as paper are hard to write, H-indices are small in real world
    # 
    # [3, 0, 6, 1, 5]
    # COUNTS IS 1 BIGGER THAN CITATIONS
    # Pass 1:
    # counts: [1, 1, 0, 1, 0, 2]
    #    idx   0  1  2  3  4  5  
    # 
    # Pass 2:
    # counts: [5, 4, 3, 3, 2, 2]   (represents number of papers with citations k or more than)
    #    idx   0  1  2  3  4  5
    # 
    #
    # 
    N = len(citations) + 1
    counts = [0] * N
    
    # Pass 1 counting sort
    for c in citations:
        if c >= N - 1: counts[N - 1] += 1
        else: counts[c] += 1
    
    # Pass 2 calculating post-sum   
    for i in range(N - 2, -1, -1):
        counts[i] += counts[i + 1]
    
    # Pass 3 figuring out tipping point
    for i in range(N - 1, -1, -1):
        if i <= counts[i]: return i
    
    return 0