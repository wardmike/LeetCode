# Prompt: https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseSingleWord(self, word: str):
        reverse = []
        for i in range(len(word)-1, -1, -1):
            reverse.append(word[i])
        return ''.join(reverse)
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')
        ssr = []
        for w in ss:
            ssr.append(self.reverseSingleWord(w))
        return ' '.join(ssr)
