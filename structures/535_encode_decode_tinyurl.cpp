/* Nathan Zhu 
*  Leetcode 535 | medium | medium
*  Category: Design
*/
#include <string>
#include <utility>
#include <unordered_map>

using namespace std;

class Solution {
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        string code;
        if(!url_to_code.count(longUrl)){
            //We keep generating a new code until we do not find a unique code
            while(code_to_url.count(code)){
                code = "";
                for(int i = 0; i < 6; ++i)
                    code.push_back(charset[rand() % charset.size()]);
            }
           
            url_to_code.insert(std::pair<string, string>(longUrl, code));
            code_to_url.insert(std::pair<string, string>(code, longUrl));
        }
        else code = url_to_code[longUrl];
        
        return tinyurl + code;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        string code = shortUrl.substr(tinyurl.size());
        return code_to_url[code];
        
    }
private:
    const string tinyurl = "https://tinyurl.com/";
    const string charset = "abcdef";
    //ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
    unordered_map<string, string> url_to_code, code_to_url;
};
