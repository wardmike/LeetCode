// Prompt: https://leetcode.com/problems/single-number/

// This algorithm works because we know that EVERY other number is added twice & only the
// one we want is added once. I'm going to revisit this later & try to do it without using
// extra memory.

// Runtime: 24 ms, faster than 39.44% of C++ online submissions for Single Number.
// Memory Usage: 11.4 MB, less than 15.68% of C++ online submissions for Single Number.

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::unordered_set<int> numsFound;
        for (size_t i = 0; i < nums.size(); ++i) {
            if (numsFound.find(nums[i]) == numsFound.end()) {
                numsFound.insert(nums[i]); // add if it's the first time we've seen
            } else {
                numsFound.erase(nums[i]); // remove if it's the second time we've seen it
            }
        }
        return *numsFound.begin(); // the only one left that's not removed is what we need
    }
};
