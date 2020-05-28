/**
 * Nathan Zhu May 21st, 2020.  Third day at Salesforce just finished!  I know my projejct now
 * Leetcode 158 | hard | yeah kinda tricky
 * Category: Misc tricks
 * 
 * So, I guess there are several cases:
 * 1. We have or do not have previous characters left-over from a prev call of read4.
 * 2. After considering reading previous characters, we either have enough characters left
 *    from successive calls of read4 to population the rest of the chars. 
 *    Or we do not.
 * 
 *    If we do not have enough chars to populate the rest of the array, we have to end early,
 *    leaving our arr[4] empty.  (Next time read4 is called, there will be no chars left)
 * 
 *    If we do have enough chars to populate the rest of the array, there may be characters
 *    left over.
 */

int read4(char *buf);

class Solution {
private:
    int valid_len;
    char arr[4];
    int curri;
public:
    Solution(): curri(4), valid_len(0){}
    
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        char* currptr = buf;
        int ret = 0;
        bool succ_read = true;
        
        // clear any chars from previous read4 call if avail
        for(int i = curri; ret < n && i < valid_len; ++i){
            *currptr = arr[i];
            currptr++;
            ret++;
            if(ret == n) curri = i + 1;      // saving spot for leftover chars
        }
        
        // continue reading if we still need more chars
        while(ret < n && succ_read){
            succ_read = false;
            valid_len = read4(arr);
            if(valid_len > 0) succ_read = true;
            
            for(int i = 0; ret < n && i < valid_len; ++i){
                *currptr = arr[i];
                currptr++;
                ret++;
                if(ret == n) curri = i + 1;   // saving spot for leftover chars
            }
        }
        
        return ret;
        
    }
};