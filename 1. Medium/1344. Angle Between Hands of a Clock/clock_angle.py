# Prompt: https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Runtime: 12 ms, faster than 96.46% of Python online submissions for Angle Between Hands of a Clock.
# Memory Usage: 13.3 MB, less than 91.15% of Python online submissions for Angle Between Hands of a Clock.


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
        # find angle of minute hand compared to 12:00
        minutesAngle = minutes * 6
        
        # find angle of hour hand compared to 12:00
        if hour == 12:
            hour = 0
        hourAngle = (hour * 30) + (minutes / 2.0)
        
        angleBetweenHands = abs(hourAngle - minutesAngle)
        
        # if over 180, go other direction
        return angleBetweenHands if angleBetweenHands <= 180 else 360 - angleBetweenHands
