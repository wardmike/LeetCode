# Prompt: https://leetcode.com/problems/rectangle-overlap/
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        # set left, bottom, right, top for each rect
        l1,b1,r1,t1 = rec1
        l2,b2,r2,t2 = rec2
        # find extremes (lowest top, highest bottom, etc)
        lowest_top = t1 if t1 < t2 else t2
        highest_bottom = b1 if b1 > b2 else b2
        leftmost_right = r1 if r1 < r2 else r2
        rightmost_left = l1 if l1 > l2 else l2
        # find overlap between two rectangles
        height_overlap = lowest_top - highest_bottom
        horiz_overlap = leftmost_right - rightmost_left
        # if the overlap is positive in both directions, they overlap
        return height_diff > 0 and horiz_diff > 0
