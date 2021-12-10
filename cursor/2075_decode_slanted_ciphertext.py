# Nathan Zhu, 3:57 pm, Stockton, CA.  
# Leetcode 2090 | medium | fun one
# Category: Cursor on matrix
# Runtime O(N)

def decodeCiphertext(encodedText, rows):
    # Edge case: empty string will cause range(0, 0, 0)
    # which will throw an error bc inf loop in python.
    if not encodedText: return ""
    
    R, C = rows, len(encodedText) / rows
    matrix, ret = [], []
    
    num_chars = sum([1 if ch != ' ' else 0 for ch in encodedText])
    for i in range(0, len(encodedText), C):
        matrix.append(encodedText[i:i+C])
    
    r, c, sc = 0, 0, 0
    while num_chars:
        sc += 1
        while num_chars and r < R and c < C:
            ret.append(matrix[r][c])
            if matrix[r][c] != ' ': num_chars -= 1
            r += 1
            c += 1
        c, r = sc, 0
        
    return "".join(ret)
            