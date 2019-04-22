# Prompt: https://leetcode.com/problems/number-complement
# Runtime: 36 ms, faster than 89.62% of Python3 online submissions for Number Complement.
# Memory Usage: 13.2 MB, less than 5.55% of Python3 online submissions for Number Complement.
class Solution:
    def findComplement(self, num: int) -> int:
        binary = "{0:b}".format(num) # binary representation of number (no leading 0s)
        swapped = [] # list for easy mutation
        for i in binary:
            if i == "0":
                swapped.append("1")
            else:
                swapped.append("0")
        return int(('').join(swapped), 2) # convert list to string, then convert binary to int
