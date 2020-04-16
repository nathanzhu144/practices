def balancedSum(sales):
    # Write your code here
    N = len(sales)
    presum = sales[:]
    postsum = sales[:]

    for i in range(1, N):
        presum[i] += presum[i - 1]

    for i in range(N - 2, -1, -1):
        postsum[i] += postsum[i + 1]

    for i in range(N):
        if postsum[i] == presum[i]: return i
    return -1


def reverse(node):
    if not node: return None
    