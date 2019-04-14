# Prompt: https://leetcode.com/problems/length-of-last-word/
# Edge cases: no words at all (no last word) or a bunch of
# empty spaces at end of input string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenLastWord = 0 #returns this 0 in case of no last word
        for i in reversed(s):
            if i == ' ':
                # check for the case that the spaces are all at the end
                if lenLastWord > 0:
                    return lenLastWord
            else:
                lenLastWord += 1
        return lenLastWord
        
