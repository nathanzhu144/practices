/** Nathan Zhu 8/9/2019, At airport. 
 *  Leetcode 204 | easy | EZ
 * 
 *  This is a super useful algorithm
*/

#include <vector>

using namespace std;

int countPrimes(int n) {
    // We mark it as 1 if it is prime, and as 0 if it is not prime
    vector<bool> is_prime(n, 1);
    int numprimes = 0;
    
    // Primes start at 2.
    for(int i = 2; i < n; ++i){
        if(is_prime[i]){
            numprimes += 1;
            
            // Marking multiples of our prime up to N, as non-primes.
            for(int multiples = i; multiples < n; multiples += i){
                is_prime[multiples] = 0;
            }
        }
    }
    
    return numprimes;
}