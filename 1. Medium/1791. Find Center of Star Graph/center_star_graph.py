# Prompt: https://leetcode.com/problems/find-center-of-star-graph/
# Runtime: 672 ms, faster than 88.49% of Python online submissions for Find Center of Star Graph.
# Memory Usage: 52.6 MB, less than 38.10% of Python online submissions for Find Center of Star Graph.


class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # the center node is the only one that 
        # will appear in more than one edge
        
        # we also know that edges will have at least
        # two entries and each entry has exactly two ints
        
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
