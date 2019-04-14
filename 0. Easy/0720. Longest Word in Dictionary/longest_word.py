# Prompt: https://leetcode.com/problems/longest-word-in-dictionary/
import functools

class Solution:
    # Custom sort function to sort primarily by size and then by
    # smallest lexicographical order
    def sort(self, a, b) -> int:
        if len(a) > len(b):
            return -1
        elif len(a) < len(b):
            return 1
        else:
            if a < b:
                return -1
            else:
                return 1
            
    def longestWord(self, words: List[str]) -> str:
        sortedWords = sorted(words, key=functools.cmp_to_key(self.sort))
        # we can pick the first one that has substrings match in "words"
        for word in sortedWords:
            eliminated = False #eliminate if substring isn't in "words"
            for i in range(len(word)):
                if word[:i+1] not in words:
                    eliminated = True
                    break
            if not eliminated:
                return word
        return ""
