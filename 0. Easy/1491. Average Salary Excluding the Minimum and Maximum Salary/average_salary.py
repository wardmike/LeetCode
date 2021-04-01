# Prompt: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Runtime: 16 ms, faster than 80.56% of Python online submissions for Average Salary Excluding the Minimum and Maximum Salary.
# Memory Usage: 13.7 MB, less than 6.75% of Python online submissions for Average Salary Excluding the Minimum and Maximum Salary.


class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sortedSalaries = sorted(salary)
        return sum(sortedSalaries[1:-1]) / float(len(salary) - 2)

