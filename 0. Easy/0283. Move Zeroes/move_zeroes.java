// Prompt: https://leetcode.com/problems/move-zeroes/
// Runtime: 12 ms, faster than 14.35% of Java online submissions for Move Zeroes.
// Memory Usage: 39.9 MB, less than 34.47% of Java online submissions for Move Zeroes.
class Solution {
    private int zeroesAtEnd = 0; // to mark when non-zero numbers stop
    public void moveZeroToEnd(int[] nums, int zeroIndex) {
        // move everything else forward
        for (int i = zeroIndex; i < nums.length - zeroesAtEnd - 1; ++i) {
            nums[i] = nums[i+1];
        }
        zeroesAtEnd += 1;
        nums[nums.length - zeroesAtEnd] = 0;
    }
    public void moveZeroes(int[] nums) {
        for (int i = 0; i < nums.length - zeroesAtEnd; ++i) {
            if (nums[i] == 0) {
                moveZeroToEnd(nums, i);
                if (nums[i] == 0) { // a zero was shifted back
                    --i;
                }
            }
        }
    }
}
