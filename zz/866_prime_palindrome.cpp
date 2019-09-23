/** Nathan Zhu Sunday Sept 22nd, 2019 10:16 pm
 *  Leetcode 866 | medium | is it though?
 *  Category: Primality
 * 
 *  Key insight here is that all prime palindromes w even number of digits are divisible by 11.
 *  Therefore, we can skip all the palindromes w even digits past 11.
 */

#include <string>
#include <cmath>

using namespace std;

// Normal trial division
int is_prime(int n){
    if(n < 2) return false;
    if(n % 2 == 0) return n == 2;

    for(int i = 3; i * i <= n; i += 2){
        if(n % i == 0) return false;
    }
    return true;

}

int primePalindrome(int n){
    // ONLY prime palindrome w even digits is 11.
    if(8 <= n && n <= 11) return 11;

    for(int i = 1; i < 100000; ++i){
        string num = to_string(i), right_part = string(num.rbegin(), num.rend());

        //Magic is here, we convert a number n to its palindrome equiv
        //Ex. 9 -> 9
        //   10 -> 101
        //   53 -> 535
        //  100 -> 10001
        //  345 -> 34543
        // NOTE: We always convert to an odd-length palindrome bc all even lenght palindromes are divisible by 11.
        string pot_palindrome = num + right_part.substr(1);
        int potential_palindrome = stoi(pot_palindrome);

        if(potential_palindrome >= n && is_prime(potential_palindrome)) return potential_palindrome;
    }
    return -1;
}

int main(){
    primePalindrome(7);
}