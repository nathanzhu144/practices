import math

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
    
    front_x_gen = x
    back_x_gen = x
    
    while front_x_gen and back_x_gen:
        if 10 ** int(math.log10(front_x_gen)) == 0: return True
        
        front = front_x_gen // (10 ** int(math.log10(front_x_gen)))
        back = back_x_gen % 10
        if front != back: return False
        
        back_x_gen = back_x_gen // 10
        front_x_gen = front_x_gen - (front_x_gen // (10 ** int(math.log10(front_x_gen)))) * (10 ** int(math.log10(front_x_gen)))
    
    return True
            
        
if __name__ == "__main__":
    print(isPalindrome(1001))
        