# Prompt: https://leetcode.com/problems/rle-iterator/
# Runtime: 28 ms, faster than 49.43% of Python online submissions for RLE Iterator.
# Memory Usage: 13.8 MB, less than 98.85% of Python online submissions for RLE Iterator.


class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.index = 0
        self.done = False
        self.sequence = []
        self.frequencies = {} # maps index of self.sequence to frequency
        
        for i in range(0, len(A) / 2):
            freq = A[i*2]
            elem = A[(i*2)+1]
            self.sequence.append(elem)
            self.frequencies[i] = freq
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if self.done:
            return -1
        
        while n > 0:
            freq = self.frequencies[self.index]
            if freq > n:
                self.frequencies[self.index] -= n
                n = 0
            elif freq == n:
                self.frequencies[self.index] = 0
                n = 0
                self.index += 1
                return self.sequence[self.index - 1]
            else:
                n -= freq
                self.index += 1
                if self.index > len(self.sequence) - 1:
                        self.done = True
                        return -1
                
                while self.frequencies[self.index] == 0:
                    self.index += 1
                    if self.index > len(self.sequence) - 1:
                        self.done = True
                        return -1
                
        
        return self.sequence[self.index]
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
