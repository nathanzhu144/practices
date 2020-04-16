/**
 * @param buf Destination buffer
 * @param n   Number of characters to read
 * @return    The number of actual characters read
 */
int read(char *buf, int n) {
    int idx = 0;
    int times_to_read = n / 4;
    if(n % 4) times_to_read += 1;
    int chars_left = n;
    
    char temp[4] = {0};
    
    for(int i = 0; i < times_to_read; ++i){
        int chars_read = read4(temp);
        if(chars_read == 0) return idx;
        for(int j = 0; j < min(chars_left, min(4, chars_read)); ++j){
            buf[idx++] = temp[j];
        }
        chars_left -= 4;
    }
    return idx;