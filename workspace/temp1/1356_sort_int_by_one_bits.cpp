int get_set(int n){
    int ret = 0;
    for(; n != 0; ret++) n &= (n - 1);
    return ret;
}

vector<int> sortByBits(vector<int>& arr) {
    auto func = [&](int n1, int n2){
        //int b1(__builtin_popcount(n1)), b2(__builtin_popcount(n2));
        int b1(get_set(n1)), b2(get_set(n2));
        if(b1 != b2) return b1 < b2;
        else return n1 < n2;
    };
    
    sort(begin(arr), end(arr), func);
    return arr;
}