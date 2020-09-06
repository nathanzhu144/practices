# /* Nathan Zhu June 13th, 2020  
# *  Leetcode 1472 | medium | medium
# *  Category: Stack
# */


def finalPrices(prices):
    """
    :type prices: List[int]
    :rtype: List[int]
    """
    N = len(prices)
    st = [(float('-inf'), -1)]
    arr = [-1 for i in range(N)]
    ret = [0 for i in range(N)]
    for i, p in enumerate(prices):
        while p <= st[-1][0]:
            arr[st[-1][1]] = i
            st.pop()
            
        st.append((p, i))
        
    for i, disc_index in enumerate(arr):
        if disc_index != -1:
            ret[i] = prices[i] - prices[disc_index]
        else:
            ret[i] = prices[i]
            
    return ret
        
        # minimum index where j > i and prices[j] <= prices[i]