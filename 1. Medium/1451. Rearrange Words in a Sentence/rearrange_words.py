# Prompt: https://leetcode.com/problems/rearrange-words-in-a-sentence/
# Runtime: 144 ms, faster than 17.44% of Python online submissions for Rearrange Words in a Sentence.
# Memory Usage: 16.7 MB, less than 47.67% of Python online submissions for Rearrange Words in a Sentence.


class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        
        lenMap = {} # maps lengths to lists of words
        
        for word in text.split(" "):
            if len(word) in lenMap:
                lenMap[len(word)].append(word.lower())
            else:
                lenMap[len(word)] = [word.lower()]
                
        result = ""
        
        for l in sorted(lenMap.keys()):
            for word in lenMap[l]:
                result += word + " "
        
        return result[:-1].capitalize()
