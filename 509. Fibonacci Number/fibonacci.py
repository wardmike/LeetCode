# Prompt: https://leetcode.com/problems/fibonacci-number/
class Solution:
    memoize = {
        0: 0,
        1: 1
    }
    def fib(self, N: 'int') -> 'int':
        if N in self.memoize:
            return self.memoize[N]
        else:
            N_val = self.fib(N-1) + self.fib(N-2)
            self.memoize[N] = N_val
            return N_val
