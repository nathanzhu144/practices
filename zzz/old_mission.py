import collections


# def solution(S):
#     N = len(S)
#     ret = float('inf')
#     for i in range(N):
#         for j in range(N):
#             if len(S[i:j+1]) < 2: continue
#             counts = collections.Counter()
#             for ch in S[i:j+1]:
#                 if ch.isupper():
#                     counts[ch.lower()] -= 1
#                 else:
#                     counts[ch] += 1
            
#             if all(v == 0 for k, v in counts.items()):
#                 ret = min(ret, len(S[i:j+1]))
#     return ret
            


def solution(S):
    N = len(S)
    ret = float('inf')
    for i in range(N):
        for j in range(N):
            countsUpper = set()
            countsLower = set()
            exists = set()
            print(S[i:j+1])

            if S[i:j+1] == 'AcZCbaBz':
                print(1)
            for ch in S[i:j+1]:
                exists.add(ch.lower())
                if ch.isupper():
                    countsUpper.add(ch.lower())
                else:
                    countsLower.add(ch)
            if all(item in countsLower and item in countsUpper for item in exists):
                ret = min(ret, len(S[i:j + 1]))
    
    return ret if ret != float('inf') else -1
print(solution('AcZCbaBz'))
# def solution(U, L, C):
#     N = len(C)
#     cells = [['0' for n in range(N)] for j in range(2)]

#     for c in range(N):
#         if C[c] == 2:
#             cells[0][c] = '1'
#             cells[1][c] = '1'
#             U -= 1
#             L -= 1
#         elif C[c] == 1:
#             if U > L:
#                 cells[0][c] = '1'
#                 U -= 1
#             else:
#                 cells[1][c] = '1'
#                 L -= 1

#         if U < 0 or L < 0: return 'IMPOSSIBLE'
    
#     fin = "".join(cells[0]) + ',' + "".join(cells[1])
#     return 'IMPOSSIBLE' if (U != 0 or L != 0) else fin
# if __name__ == "__main__":
#     print(solution(3, 2, [2, 1, 1, 0, 1]))


# class A:
#     def __init__(self):
#         self._x = '1'
#     def set_x(self, x):
#         self._x = x

#     def __str__(self):
#         return f'A[x={self._x}]'

# a = A()
# print(a)
# a.set_x(2)
# print(a)

