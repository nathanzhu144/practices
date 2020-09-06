import collections


def makeGood(s):
    """
    :type s: str
    :rtype: str
    """
    def valid(s):
        i = 0
        for a, b in zip(s, s[1:]):
            large, small = max(a, b), min(a, b)
            if ord(large) - (ord('a') - ord('A')) == ord(small): return i
            i += 1
        return -1
    
    while True:
        i = valid(s)
        if i == -1: return s
        s = s[:i] + s[i + 2:]
    return None


if __name__ == "__main__":
    print(makeGood("leEeetcode"))
    #print(canConvertString("zzaa", "aazz", 100))
    #print(canConvertString("atmtxzjkz","tvbtjhvjd",35))




# def solution(src, dest):
#     R, C = 8, 8
#     start, end = None, None
#     for r in range(R):
#         for c in range(C):
#             val = r * 8 + c
#             if val == src: start = (r, c)
#             if val == dest: end = (r, c)

#     q = collections.deque([start])
#     visited = set([start])
#     ret = 0

#     while q:
#         csize = len(q)
#         for i in range(csize):
#             r, c = q.popleft()
#             if (r, c) == end: return ret

#             for dr, dc in [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
#                 newr, newc = r + dr, c + dc
#                 newpos = (newr, newc)
#                 if newpos in visited: continue
#                 visited.add(newpos)
#                 q.append(newpos)

#         ret += 1
#     return -1


# def findParent(height, node):
#     start, end = 1, 2 ** height - 1
#     if end == node: return -1

#     while node >= 1:
#         end = end - 1

#         mid = start + (end - start) // 2

#         if mid == node or end == node:
#             return end + 1
#         elif node < mid:
#             end = mid
#         else:
#             start = mid
    
