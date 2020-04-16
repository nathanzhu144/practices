// Nathan Zhu March 19th, 2020 10:19 pm Foundry Lofts, it is spring break
// Leetcode 342 | easy | not that easy lol
// Category: binary
// Note that 9x5555555 is the mask 0b10101010101...
// We want to take the powers of 2, but also the ones that are pwoer of 4

bool isPowerOfFour(int num) {
    return num > 0 and ((num & (num - 1)) == 0) and ((0x55555555 & num) != 0);
}