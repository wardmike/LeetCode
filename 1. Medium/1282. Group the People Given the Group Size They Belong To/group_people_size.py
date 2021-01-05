# Prompt: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Runtime: 68 ms, faster than 27.42% of Python online submissions for Group the People Given the Group Size They Belong To.
# Memory Usage: 13.6 MB, less than 71.94% of Python online submissions for Group the People Given the Group Size They Belong To.

class Solution(object):
    # split "arr" into mini-arrays of length "size"
    def splitArray(self, arr, size):
        """
        :type arr: List[int]
        :type size: int
        :rtype: List[List[int]]
        """
        final = []
        temp = []
        for i, val in enumerate(arr):
            temp.append(val)
            if (i+1) % size == 0:
                final.append(temp)
                temp = []
        return final
    
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups = {}
        for i, size in enumerate(groupSizes):
            if size in groups:
                groups[size].append(i)
            else:
                groups[size] = [i]
                
        # split duplicates (ex: 6 people assigned to groups of 3)
        fixedGroups = []
        for size in groups:
            if len(groups[size]) > size:
                splits = self.splitArray(groups[size], size)
                fixedGroups = fixedGroups + splits
            else:
                fixedGroups.append(groups[size])
        
        return fixedGroups
