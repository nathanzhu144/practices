
#include <vector>
#include <string>

using namespace std;

string func(string s){
    auto idx = s.find('/', 7); // http//:
    auto ret = (idx != string::npos ? s.substr(0, idx) : s);
    return ret;
}

int main(){
    func("http://google.com");
    func("http://news.yahoo.com/news");
}