

#include <vector>
#include <unordered_map>
#include <map>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>

// Game where you can substract by 1, 2, 3.
// Whoever gets to <= 1, loses. 
F(<= 1) = LOSS 

if (F(N - 1) OR F(n - 2) OR F(N - 3) )

F(N) is a WIN if any of F(N - 1), F(N - 2), F(N - 3) o



using namespace std;

unordered_map<int, bool> table;

bool helper(int x){
    if (x <= 1) return false;
    if(table.count(x)) return table[x];

    bool ret = false;
    if(!helper(x - 1)){
        ret = true;
        table[x] = true;
        return ret;
    }

    for(int i = 3; i <= x; i += 2){
        if(x % i == 0 && !helper(x / i)){
            ret = true;
            table[x] = true;
            return ret;
        }
    }

    table[ret] = false;
    return false;
}

int winner(int x){
    if(helper(x)) cout <<"Ashishgup" << endl;
    else cout << "FastestFinger" << endl;
}
int main(){
    string buf;
    getline(cin, buf);

    while(getline(cin, buf)){
        int N = stoi(buf);
        winner(N);
    }
}