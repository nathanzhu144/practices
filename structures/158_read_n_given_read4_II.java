/* Nathan Zhu April 9th, 2020 
*  Leetcode 158 | hard | hard?
*  Category: Misc tricks
*/

/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char[] buf); 
 */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    private int buffPtr = 0;
    private int buffCount = 0;
    private char[] temp = new char[4];
    public int read(char[] buf, int n) {
        int ptr = 0;
        while (ptr < n) {
            //no remaining characters in the temp
            if (buffPtr == 0) {
                buffCount = read4(temp);
            }
            if (buffCount == 0) {
                break;// end of file
            }
            // copy from temp buffer to buf
            while (ptr < n && buffPtr < buffCount) {
                buf[ptr++] = temp[buffPtr++];
            }
            // not because of ptr < n broken out of loop, read to the end of temp buffer
            if (buffPtr >= buffCount) {
                buffPtr = 0;
            }
        }
        return ptr;
    }
}