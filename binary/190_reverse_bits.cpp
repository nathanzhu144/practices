/** Nathan Zhu Jan 10th, 2020, 7:27 pm, Foundry Lofts couch
 *  Leetcode 190 | easy | kinda easy, but not that easy
 *  Category: Bitshifting
 */

#include <stdint.h>

uint32_t reverseBits(uint32_t n) {
    uint32_t ret = 0;
    
    for(int i = 0; i < 32; ++i){
        ret <<= 1;
        ret |= n & 1;
        n >>= 1;
    }
    return ret;
}