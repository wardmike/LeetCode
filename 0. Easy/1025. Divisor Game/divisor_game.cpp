// https://leetcode.com/problems/divisor-game
/*
 * Notes: The first player always wins if the number is even, and the second
 * player always wins if the number is odd. I'm not sure why; I just noticed
 * a correlation in the test cases and decided to try various other test cases
 * to see if it worked. I plan to revisit this later and figure
 */
// Runtime: 4 ms, faster than 100.00% of C++ online submissions for Divisor Game.
// Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for Divisor Game.

class Solution {
public:
    bool divisorGame(int N) {
        return (N % 2 == 0);
    }
};
