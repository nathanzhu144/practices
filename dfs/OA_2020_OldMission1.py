


from collections import defaultdict
from collections import deque

graph = defaultdict(list)

def solution(dependencies, dirty):
    for target in graph:
        graph[target] = list()

    for i in range(len(dependencies)):
        inst = dependencies[i]
        pair = inst.split(":")
        target, depend = pair
        for dep in depend.split(" "):
            if dep != " " and dep != "": 
                graph[dep].append(target)


    pq = deque([dirty])
    seen = set()
    while pq:
        node = pq.pop()
        if node in seen:
            continue
        else:
            seen.add(node)
        for adj in graph[node]:
            pq.appendleft(adj)

    final = list(seen)
    return sorted(final, reverse=False)




        
if __name__ == "__main__":
    print(solution(["A: E"], "E"))
    print(solution(["A: E N S", "S: H N", "E: N", "H: ", "N: "], "A"))
    print(solution(["A: E N S", "S: H N", "E: N", "H: ", "N: "], "N"))
    print(solution(["a: b c d",
                    "b: c d",
                    "c: ",
                    "hello: world",
                    "world: a b c d",
                    "e: f",
                    "g: ",
                    "z: b"],
                    "hello"
                    ))
    
