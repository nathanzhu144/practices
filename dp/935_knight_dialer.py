# Nathan Zhu 8/8/2019 Amex, Last few days.
# Leetcode 935 | medium | med
# Category: DP
#
# Hershal trolled me with this question for so long - it isn't even that hard

# Top-down
def knightDialer(N):
    """
    :type N: int
    :rtype: int
    """
    
    adjacent = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
    graph = dict()
    for i in range(len(adjacent)):
        graph[i] = adjacent[i]
        
    def helper(curr_pos, num_hops, graph, table):
        key = (curr_pos, num_hops)
        if key in table: return table[key]
        
        if num_hops == 1: return 1
        
        num_form_by_rest_digits = 0
        for node in graph[curr_pos]:
            num_form_by_rest_digits += helper(node, num_hops - 1, graph, table)
        
        table[key] = num_form_by_rest_digits % (10 ** 9 + 7)
        return table[key]
    
    
    ret = 0
    for i in range(10): ret += helper(i, N, graph, dict())
    return ret % (10 ** 9 + 7)
        
# Bottom-up
def knight_dialer_bottom_up(N):
    """
    :type N: int
    :rtype: int
    """
    mod = 10 ** 9 + 7
    graph = [[]] * 10
    graph[0] = [4, 6]
    graph[1] = [6, 8]
    graph[2] = [7, 9]
    graph[3] = [4, 8]
    graph[4] = [0, 3, 9]
    graph[5] = []
    graph[6] = [0, 1, 7]
    graph[7] = [2, 6]
    graph[8] = [1, 3]
    graph[9] = [2, 4]
    
    # i, j   i == curr spot, j = 
    ret = [1] * 10
    
    for i in range(N - 1):
        new = [0] * 10
        
        for number in range(10):
            for neighbor in graph[number]:
                new[neighbor] += ret[number]
                new[neighbor] %= mod
        ret = new
            
    return sum(ret) % mod
        