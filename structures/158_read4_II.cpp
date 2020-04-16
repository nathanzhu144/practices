
/* Nathan Zhu March 19th, 2020, 10:04 pm 
 * Leetcode 158 | hard | hard
 * Category: structures
*/

// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int i = 0;
        
        while (i < n and (i4 < n4 || (i4 = 0) < (n4 = read4(buf4))))  // I like this line, lol.
            buf[i++] = buf4[i4++];
        return i;
    }
    char buf4[4];
    int i4 = 0, n4 = 0;
};