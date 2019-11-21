#include <unordered_map>
#include <string>

using namespace std;


int lengthOfLongestSubstring(string s)
{
    int max = 0;
    int current = 0;
    int last_index = 0;
    unordered_map<char, int> past;

    for (int i = 0; i < (int)(s.size()); ++i)
    {
        if (past.find(s[i]) != past.end())
        {
            if (current > max)
            {
                max = current;
            }

            i = past[s[i]] + 1;
            past.clear();
            past.insert(make_pair(s[i], i));
            current = 1;
        }
        else
        {
            ++current;
            past.insert(make_pair(s[i], i));
        }

        if (i == s.size() - 1)
        {
            return std::max(max, current);
        }
    }

    return max;
}