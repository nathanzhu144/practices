

def numWays(steps, N):
    """
    :type steps: int
    :type arrLen: int
    :rtype: int
    """
    arr = [0] * N
    arr[0] = 1
    MOD = 10 ** 9 + 7
    
    for j in range(steps):
        newarr = [0] + [sum(arr[i - 1 : i + 2]) % MOD for i in range(1, N + 1)]
        arr = newarr
        
    return arr[1]
        


if __name__ == "__main__":
    print(numWays(2, 4))