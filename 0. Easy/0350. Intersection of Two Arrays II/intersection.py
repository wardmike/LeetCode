# Prompt: https://leetcode.com/problems/intersection-of-two-arrays-ii

# Runtime: 32 ms, faster than 64.68% of Python online submissions for Intersection of Two Arrays II.
# Memory Usage: 11.9 MB, less than 5.37% of Python online submissions for Intersection of Two Arrays II.

class Solution(object):
    def intersect(self, nums1, nums2):
        bigger = nums1 if len(nums1) > len(nums2) else nums2
        smaller = nums2 if len(nums1) > len(nums2) else nums1
        smallerMap = {} # stores occurances of each number in the smaller array
        for elem in smaller:
            if elem in smallerMap:
                smallerMap[elem] += 1
            else:
                smallerMap[elem] = 1
        output = []
        for elem in bigger:
            if elem in smallerMap:
                output.append(elem)
                if smallerMap[elem] == 1:
                    del smallerMap[elem]
                else:
                    smallerMap[elem] -= 1
        return output
        
