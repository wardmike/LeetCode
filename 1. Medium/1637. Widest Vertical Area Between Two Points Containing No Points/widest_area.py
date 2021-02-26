# Prompt: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
# Runtime: 684 ms, faster than 98.45% of Python online submissions for Widest Vertical Area Between Two Points Containing No Points.
# Memory Usage: 57.3 MB, less than 38.86% of Python online submissions for Widest Vertical Area Between Two Points Containing No Points.


class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        # find x-vals of points (we can ignore y-values
        # since they have no effect on the width)
        xVals = []
        for p in points:
            xVals.append(p[0])
            
        xVals.sort()
        
        biggestGap = 0
        for i in range(len(xVals) - 1):
            if xVals[i+1] - xVals[i] > biggestGap:
                biggestGap = xVals[i+1] - xVals[i]
        return biggestGap
