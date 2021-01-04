# Prompt: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# Runtime: 360 ms, faster than 49.57% of Python online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.5 MB, less than 71.03% of Python online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # the largest digit within the number is equal to the number of deci-binary numbers
        # needed to sum up to the original number
        # this is because it takes x deci-binary numbers to sum to a digit of x (since the max digit in each deci-binary number is 1),
        # and all smaller digits can be made up by 1s or 0s in the deci-binary numbers needed to create the largest digit

        largest = 0
        for digit_str in n:
            digit_int = int(digit_str)
            if digit_int > largest:
                largest = digit_int

        return largest
