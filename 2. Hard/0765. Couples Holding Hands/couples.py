# Prompt: https://leetcode.com/problems/couples-holding-hands
# Runtime: 60 ms, faster than 12.69% of Python3 online submissions for Couples Holding Hands.
# Memory Usage: 13.2 MB, less than 8.70% of Python3 online submissions for Couples Holding Hands.
class Solution:
    # swaps elems at indices a and b in row
    def swap(self, row, a, b):
        temp = row[a]
        row[a] = row[b]
        row[b] = temp
        
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps = 0
        # checking every even-index person & moving their partner to them
        for i in range(0, len(row), 2):
            if int(row[i] / 2) != int(row[i+1] / 2):
                # find the partner to this person
                for j in range(i+2, len(row)):
                    if int(row[j] / 2) == int(row[i] / 2):
                        self.swap(row, i+1, j)
                        swaps += 1
        return swaps
