# Prompt: https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = -1
        for i in range(1, len(A)-1):
            #check if it's bigger than A[i-1]
            if A[i] > A[i-1] and A[i] > A[i+1]:
                #check if a peak is already set
                if peak is not -1:
                    return None
                else:
                    peak = i
        if peak is not -1:
            return peak
        else:
            return None
