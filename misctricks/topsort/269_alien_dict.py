# Nathan Zhu EHS 55 John Street.  I'm the only one in the room.  Friday August 9th, 2019, 11:59 pm.  Last night in New York before going home.  Got a returns offer today!
# Leetcode 269 | hard | took ages before I understood this question lol
# Category: DFS / Topological sort
# The topological sort isn't that bad when you get the idea.

import collections


class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()

def alien_order(words):
    
    # add characters to dictionary.
    # Do not use defaultdict for this edge case ["w", "w"]
    # In that case, nothing gets added to the dict, and there is no ordering, but there actually is...
    graph = dict()
    for word in words:
        for character in word:
            graph[character] = Node()

    # This block of code figures which characters must come before other chars.
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                graph[b].IN.add(a)
                graph[a].OUT.add(b)
                break
    
    # Topological sort
    ret = ""
    while graph:
        old_len = len(graph)
        for character in graph:
            # 1. We can remove this node, as it has no dependencies
            # 2. We add this character to our topological ordering
            # 3. For all other nodes w this dependency, we take the dependency out of their dependency set
            # 4. We take this node out of the graph
            # 5. BREAK. Technically not necessary, but otherwise python throws an error when iterating as 
            #    size of dictionary changes.  We have successfully removed a node, and can attempt to remove
            #    another node with the next iteration.
            if not graph[character].IN:
                ret = ret + character
                for c in graph[character].OUT:
                    graph[c].IN.remove(character)
                del graph[character]
                break
        # we have a cycle, fail to remove any other nodes, impossible to make top order
        if len(graph) == old_len:
            return ""
    return ret


if __name__ == "__main__":
    print(alien_order([  "w",
                         "w"]))