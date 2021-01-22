# Prompt: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
# Runtime: 28 ms, faster than 46.15% of Python online submissions for Number of Students Doing Homework at a Given Time.
# Memory Usage: 13.3 MB, less than 91.03% of Python online submissions for Number of Students Doing Homework at a Given Time.

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        students = 0
        for i, t in enumerate(startTime):
            if t <= queryTime and endTime[i] >= queryTime:
                students += 1
                
        return students
