
from collections import defaultdict, Counter
def validArrangement(pairs):
    g = defaultdict(list)  # graph
    din, dout = Counter(), Counter()  #in degree, out degree
    for u, v in pairs:
        g[u].append(v)
        dout[u] += 1
        din[v] += 1

    S = pairs[0][0]  # Start anywhere if it's an Eulerian cycle.
    for p in dout:
        if dout[p] - din[p] == 1:  # It's an Eulerian trail. Have to start here
            S = p
            break
    
    # Hierholzer's Algorithm:
    route = []
    st = [S]
    while st:
        while g[st[-1]]:
            st.append(g[st[-1]].pop())
        route.append(st.pop())
    route.reverse()
    return [[route[i], route[i+1]] for i in range(len(route)-1)]

if __name__ == "__main__":
    test_graph = [[0, 2], [2, 2], [1, 0], [0, 1], [1, 1], [1, 2], [2, 1]]
    print(validArrangement(test_graph))