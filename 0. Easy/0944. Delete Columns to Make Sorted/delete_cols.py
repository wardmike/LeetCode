# Prompt: https://leetcode.com/problems/delete-columns-to-make-sorted
"""
 Notes: each column is separate; values in one col won't affect deletion of another
"""
# Runtime: 160 ms, faster than 54.05% of Python3 online submissions for Delete Columns to Make Sorted.
# Memory Usage: 13.6 MB, less than 8.18% of Python3 online submissions for Delete Columns to Make Sorted.
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        d = 0 # min cols needed to delete
        for i in range(len(A[0])):
            prev = A[0][i]
            for j in range(1, len(A)):
                if prev > A[j][i]:
                    d += 1
                    break
                prev = A[j][i]
        return d
        
