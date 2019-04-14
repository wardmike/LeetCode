class Solution:
    def hammingDistance(self, x, y):
        xx = bin(x)[2:].zfill(32)
        yy = bin(y)[2:].zfill(32)
        diff = 0
        for i in range(len(xx)):
            if xx[i] != yy[i]:
                diff += 1
        return diff
