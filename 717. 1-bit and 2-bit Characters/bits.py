# Prompt: https://leetcode.com/problems/1-bit-and-2-bit-characters/
class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        #loop through stopping on the first digit of each character
        while i < len(bits):
            #if we land on the last digit, it must be a 1-bit character
            if i == len(bits) - 1:
                return True
            i += 2 if bits[i] == 1 else 1
        return  False
