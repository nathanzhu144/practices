# Union find impl for EECS 376 Problem 3.
class UF:
    def __init__(self):
        self.num_subgraphs = 0
        self.parents = dict()
    
    # Private functions managing UF state
    def union(self, a, b):
        if self.find(a) == self.find(b): return
        self.parents[self.find(a)] = self.find(b)
        self.num_subgraphs -= 1
    # Private functions managing UF state
    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])  # Path compression.
        return self.parents[a]

    # Private functions managing UF state
    def add_subgraph(self, a):
        if a in self.parents: return
        self.parents[a] = a
        self.num_subgraphs += 1

    # Adds an edge to the graph
    def add_edge(self, a, b):
        self.add_subgraph(a)
        self.add_subgraph(b)
        self.union(a, b)
    # Sees if graph is connected.
    def is_connected(self):
        return self.num_subgraphs == 1

# Takes in a vector of pairs, where each pair represents an edge between two nodes
# is_connected returns if the graph input is connected
if __name__ == "__main__":
    nodes1 = [[1, 2], [3, 4]]
    UF1 = UF()

    for a, b in nodes1:
        UF1.add_edge(a, b)
    print(UF1.is_connected())







    UF1.add_edge(1, 8)
    UF1.add_edge(1, 1)
    print(UF1.is_connected())
    UF1.add_edge(2, 4)
    print(UF1.is_connected())