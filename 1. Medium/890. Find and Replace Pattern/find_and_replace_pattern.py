# Prompt: https://leetcode.com/problems/find-and-replace-pattern/
# Runtime: 24 ms, faster than 37.86% of Python online submissions for Find and Replace Pattern.
# Memory Usage: 13.5 MB, less than 36.43% of Python online submissions for Find and Replace Pattern.

class Solution(object):
    
    # finds a unique code for the word pattern
    def findWordCode(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        letter_map = {}
        next_code = 0
        
        code = []
        for letter in word:
            if letter in letter_map:
                code.append(letter_map[letter])
            else:
                letter_map[letter] = next_code
                code.append(next_code)
                next_code += 1
        return code            
    
        
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pattern_code = self.findWordCode(pattern)
        matches = []
        
        for word in words:
            word_code = self.findWordCode(word)
            
            if word_code == pattern_code:
                matches.append(word)
        
        return matches
