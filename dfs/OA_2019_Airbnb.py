# Nathan Zhu Feb 1st, 2020.  Starbucks State Street.  Just ate two oranges.  This is a 2019 question.
# Leetcode n/a (airbnb oa) | - | medium?
# Category: DFS / topological sort
# Intuition: You have to reverse the graph like you do in topological sort questions.
#            Then, do a dfs on each task, and see how many tasks you can cover with each dfs.
# 
# Input
# 
# lines is a list of strings
# ["AENS"
#  "SHN"
#  "EN"
#  "H"
#  "N"
# ]
# 

import collections

# Runtime, N^2, where N is number of vertices in the graph.
def cost_of_nodes(lines):
    # Step 1: Make input into a table of  "task A" -> "task B that has task A as a DIRECT dependency"
    # table should look like after step 1.
    # { A : [],
    #   S : [A],
    #   E : [A],
    #   H : [S],
    #   N : [A, S, E]
    # }
    table = collections.defaultdict(list)
    nodes = []
    for line in lines:
        if line[0] not in table: table[line[0]] = list() # some tasks have no tasks that depend on them, 
                                                         # this ensure they are assigned an empty list.
        nodes.append(line[0])
        for i in range(1, len(line)):
            table[line[i]].append(line[0])
    nodes = sorted(nodes)

    # Step 2: Use table to do a DFS on each node.
    def dfs(curr, visited):
        if curr in visited: return 0  # avoid double-counting dependencies
        visited.add(curr)

        # we find a new dependency.
        deps = 1   
        # recursively count dependencies.
        for neigh in table[curr]:
            deps += dfs(neigh, visited)
        return deps

    ret = []
    for node in nodes:
        ret.append("".join([node, ",", str(dfs(node, set()))]))
    return ret


        
if __name__ == "__main__":
    print(cost_of_nodes(["AENS", "SHN", "EN", "H", "N"]))
    



        