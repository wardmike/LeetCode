# Prompt: https://leetcode.com/problems/sum-of-even-numbers-after-queries
# Runtime: 184 ms, faster than 36.30% of Python3 online submissions for Sum of Even Numbers After Queries.
# Memory Usage: 17.5 MB, less than 5.56% of Python3 online submissions for Sum of Even Numbers After Queries.
class Solution:
    def getSumEven(self, A: List[int]):
        sumEven = 0
        for num in A:
            if num % 2 == 0:
                sumEven += num
        return sumEven
    
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sumEven = self.getSumEven(A)
        for query in queries:
            query_index = query[1]
            query_add = query[0]
            if query_index < len(A):
                # if it's even, remove it (might become odd); this is quicker than checking
                if A[query_index] % 2 == 0:
                    sumEven -= A[query_index]
                A[query[1]] += query[0]
                # if it's even, add it (might have become even); this is quicker than checking
                if A[query_index] % 2 == 0:
                    sumEven += A[query_index]
            result.append(sumEven)
        return result
        
