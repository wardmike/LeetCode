# Prompt: https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        #sort by square of distance to origin (doing the square-root is extraneous as order will be the same)
        points_sorted = sorted(points, key=lambda k: k[0]**2 + k[1]**2)
        #pick first K in sorted list
        return points_sorted[:K]
