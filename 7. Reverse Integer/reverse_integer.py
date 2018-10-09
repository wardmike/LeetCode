class Solution:
    def reverse(self, x):
        y = int(str(abs(x))[::-1])
        if x < 0: y = -y
        if y > 2**31 - 1 or y < -2**31:
            return 0
        return y
