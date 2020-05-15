# Nathan Zhu Jan 10th, 2019, Google Mock Interview
# Leetcode 975 | hard | effing hard
#
# Category: DP / Monotonic stack
# This question requires two insights to make work...
def oddEvenJumps(A):
    """
    :type A: List[int]
    :rtype: int
    """
    
    
    def get_order(idx_sorted_by_val):
        ret = [None] * len(idx_sorted_by_val)
        
        stack = []
        for i in idx_sorted_by_val:
            while stack and i > stack[-1]:
                ret[stack[-1]] = i
                stack.pop()
            stack.append(i)
        return ret
    
    N = len(A)
    idx_sort_inc_odd = sorted(range(N), key=lambda i: A[i])
    odd_order = get_order(idx_sort_inc_odd)
    idx_sort_dec_even = sorted(range(N), key=lambda i: -A[i])
    even_order = get_order(idx_sort_dec_even)
    
    odd, even = [False] * N, [False] * N
    odd[N - 1] = True
    even[N - 1] = True
    
    for i in range(N - 1, -1, -1):
        next_odd, next_even = odd_order[i], even_order[i]
        if next_odd: odd[i] = even[next_odd]
        if next_even: even[i] = odd[next_even]
            
    return sum(odd)