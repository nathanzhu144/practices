
import collections
# [2, 6, 8, 5]
# [0, 1, 2, 2] left
# [1, 2, 2, 3] right


# question 2
def solution(arr):
    N = len(arr)
    
    lmove, rmove = [-1] * N, [-1] * N
    def helper_left(i):
        if i == 0 or arr[i - 1] < arr[i]: return 0
        if lmove[i] != -1: return lmove[i]
        lmove[i] = 1 + helper_left(i - 1)
        return lmove[i]

    def helper_right(i):
        if i == N - 1 or arr[i + 1] < arr[i]: return 0
        if rmove[i] != -1: return rmove[i]
        rmove[i] = 1 + helper_right(i + 1)
        return rmove[i]

    ret = 0
    for i in range(N):
        ret = max(helper_left(i) + helper_right(i), ret)
    return ret


# # question 2
# def solution(arr):
#     N = len(arr)
    
#     def helper_l(i):
#         if i == 

# question 3
def solution3(string, cost):
    N = len(string)
    previ, ret = -1, 0
    for i in range(N):
        if previ >= 0 and string[previ] == string[i]:
            if cost[previ] > cost[i]:
                ret += cost[i]
            else:
                ret += cost[previ]
                previ = i
        else: previ = i

    return ret



if __name__ == "__main__":
    #assert(solution3("aaabb", [1, 1, 1, 2, 2]))
    assert(solution([1]) == 0)
    print(solution([2, 3, 6, 7, 1, 8] + [2] * (2 **10)))
    #assert(solution([2, 3, 6, 7, 1, 8, 9, 10, 11]) == 7)
    assert(solution([2, 6, 8, 5]) == 2)
    assert(solution([1, 5, 5, 2, 6]) == 3)
    assert(solution([1, 1,]) == 1)


    # S = "abccbd"
    # B = [0, 1, 2, 3, 4, 5]
    # print(solution(S, B))