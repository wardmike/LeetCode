/* PROMPT: Implement function ToLowerCase() that has a string parameter str
  and returns the same string in lowercase. 
  NOTE: This solution is completed without using <cctype>'s tolower() function */

#include <string>
class Solution {
    private:
        std::string lower = "abcdefghijklmnopqrstuvwxyz";
        std::string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public:
        std::string toLowerCase(std::string str) {
            for (int i = 0; i < str.length(); ++i) {
                std::size_t pos = upper.find(str[i]);
                // see if i is upper case
                if (pos != std::string::npos) {
                    str[i] = lower[pos]; // replace i if upper case
                }
            }
            return str;
        }
};
