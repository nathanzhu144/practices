/*  Nathan Zhu May 1st, 2020. 10:42 pm 3 days since 376 final, good times, watched code-8 with Heshal and crew today.
*   Leetcode 1195 | medium | medium
*   Category: multithreaded
*/

// Did not know that cv.wait(lock, []function) was equivalant to:
// 
// while(!function) 
//   wait
//
//
// Also cool use of std::functions, and lambdas in this one

using namespace std;
#include <functional>
#include <mutex>
#include <condition_variable>
class FizzBuzz {
private:
    int n;
    mutex m;
    condition_variable c;
    int curr;

public:
    FizzBuzz(int n) {
        this->n = n;
        this->curr = 1;
    }
    
    void run(function<void(int)> print, function<bool(int)> test){
        while(true){
            unique_lock<mutex> lk(m);
            c.wait(lk, [&]{ return curr > n || test(curr); });
            if(curr > n) return;
            print(curr++);
            lk.unlock();
            c.notify_all();
        }
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        run([&](int val) { printFizz();}, [&](int val){ return curr % 3 == 0 and curr % 5 != 0; });
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        run([&](int val) { printBuzz();}, [&](int val){ return curr % 5 == 0 and curr % 3 != 0; });
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        run([&](int val){ printFizzBuzz();}, [&](int val){ return curr % 3 == 0 and curr % 5 == 0; });
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        run(printNumber, [&](int val){ return curr % 3 != 0 and curr % 5 != 0; });
    }
};