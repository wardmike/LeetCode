# Prompt: https://leetcode.com/problems/goat-latin/
# Runtime: 12 ms, faster than 94.17% of Python online submissions for Goat Latin.
# Memory Usage: 13.6 MB, less than 45.95% of Python online submissions for Goat Latin.


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
        sentence = ""
        words = S.split(" ")
        for i, word in enumerate(words):
            newWord = ""
            if word[0] in vowels:
                newWord = word + "ma"
            else:
                newWord = word[1:] + word[0] + "ma"
            
            for j in range(i+1):
                newWord += "a"
                
            sentence += newWord + " "
                
            
        return sentence[:-1] # remove space at end
