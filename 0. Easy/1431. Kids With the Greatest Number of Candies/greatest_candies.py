# Prompt: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Runtime: 28 ms, faster than 49.22% of Python online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.4 MB, less than 43.36% of Python online submissions for Kids With the Greatest Number of Candies.


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        most = max(candies)
        output = []
        
        for c in candies:
            if c + extraCandies >= most:
                output.append(True)
            else:
                output.append(False)
        
        return output
