



def validUtf8(data):
    """
    :type data: List[int]
    :rtype: bool
    """
    if not data: return False
    
    num_bytes = 0
    for d in data:
        if num_bytes == 0:
            if d >> 7 == 0b0: num_bytes = 0            # case for 1 byte character
            elif d >> 5 == 0b110: num_bytes = 1        # case for 2 byte char
            elif d >> 4 == 0b1110: num_bytes = 2       # case for 3 byte char
            elif d >> 3 == 0b11110: num_bytes = 3      # case for 4 byte char
            else: return False
        else:
            if d >> 6 != 0b10: return False
            else: num_bytes -= 1
    return num_bytes == 0
                

if __name__ == "__main__":
    print(validUtf8([197,130]))