# Prompt: https://leetcode.com/problems/intersection-of-two-arrays/

# Runtime: 44 ms, faster than 36.06% of Python online submissions for Intersection of Two Arrays.
# Memory Usage: 11.9 MB, less than 5.86% of Python online submissions for Intersection of Two Arrays.

class Solution(object):
    def intersection(self, nums1, nums2):
        bigger = nums1 if len(nums1) > len(nums2) else nums2
        smaller = nums2 if len(nums1) > len(nums2) else nums1
        # turn smaller list into a set
        smaller = set(smaller)
        # loop through bigger list & see if any in there are in smaller set
        output = []
        for elem in bigger:
            if elem in smaller:
                output.append(elem)
                smaller.remove(elem)
        return output
