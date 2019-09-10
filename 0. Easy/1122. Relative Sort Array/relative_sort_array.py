# Prompt: https://leetcode.com/problems/relative-sort-array
"""
loop through arr2 and append each element to a new list as many times as it
appears in arr1, then loop through arr1 and add any element not appearing in
arr2 to another list. sort that list and add to the end of the first list
"""
# Runtime: 48 ms, faster than 47.01% of Python3 online submissions for Relative Sort Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Relative Sort Array.
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final = []
        overflow = []
        for e2 in arr2:
            for _ in range(arr1.count(e2)):
                # this works only because elems in arr2 are discrete
                final.append(e2)
        # find elems in arr1 that aren't in arr2
        for e1 in arr1:
            if e1 not in arr2:
                overflow.append(e1)
        return final + sorted(overflow)
