# Nathan Zhu Friday Dec 26th, 2019 10:22 pm
# Leetcode 733 | easy | EZ
# if you can do number islands you can do this
# Edge case, new color is same as old color can lead to infinite recursion
# 
def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    def helper(image, row, col, oldcolor, newcolor):
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] != oldcolor: 
            return
        
        image[row][col] = newcolor
        helper(image, row + 1, col, oldcolor, newcolor)
        helper(image, row - 1, col, oldcolor, newcolor)
        helper(image, row, col + 1, oldcolor, newcolor)
        helper(image, row, col - 1, oldcolor, newcolor)
        
    if image[sr][sc] == newColor: return image
    helper(image, sr, sc, image[sr][sc], newColor)
    return image