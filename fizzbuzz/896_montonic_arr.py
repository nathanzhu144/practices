    # Nathann Zhu Jan 11th, 2019 8:09 pm
    # Leetcode 896 | easy | EZ
    # Category: Fizzbuzz 
    # 
    # Lmaooo this sooo easy
    
    
    
    def isMonotonic(A):
        return all([A[i] <= A[i + 1] for i in range(len(A) - 1)]) or all([A[i] >= A[i + 1] for i in range(len(A) - 1)])