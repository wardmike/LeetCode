# Prompt: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Runtime: 100 ms, faster than 6.17% of Python online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 13.8 MB, less than 46.65% of Python online submissions for The K Weakest Rows in a Matrix.


class Row(object):
    def __init__(self, num, soldiers):
        self.num = num
        self.sum = soldiers

class Solution(object):
    
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        rows = []
        for i, row in enumerate(mat):
            rows.append(Row(i, sum(row)))
            
        
        # simple bubble sort
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(rows)-1):
                if rows[i].sum > rows[i+1].sum or (rows[i].num == rows[i+1].num and rows[i].sum > rows[i+1].sum):
                    self.swap(rows, i, i+1)
                    swapped = True

        topK = []
        
        for i in range(k):
            topK.append(rows[i].num)
        
        return topK
