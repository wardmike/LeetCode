# Prompt: https://leetcode.com/problems/minimum-time-visiting-all-points/
# Runtime: 44 ms, faster than 49.55% of Python online submissions for Minimum Time Visiting All Points.
# Memory Usage: 13.4 MB, less than 60.86% of Python online submissions for Minimum Time Visiting All Points.

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        totalDist = 0
        for i in range(len(points) - 1):
            totalDist += self.distanceBetweenPoints(points[i], points[i+1])
            
        return totalDist
        
        
    def distanceBetweenPoints(self, point1, point2):
        """
        :type point1: List[int]
        :type point2: List[int]
        :rtype: int
        """
        xDist = abs(point1[0] - point2[0])
        yDist = abs(point1[1] - point2[1])
        
        
        # return the larger of the two, because the shorter axis distance can be made up
        # by taking diagonal steps while moving along the longer axis distance
        return max(xDist, yDist)
        