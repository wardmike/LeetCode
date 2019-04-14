# Prompt: https://leetcode.com/problems/keyboard-row/
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # make rows
        row_1 = "qwertyuiop"
        row_2 = "asdfghjkl"
        row_3 = "zxcvbnm"
        good = []
        for w in words:
            word = w.lower()
            # set to False when a letter is not in that row
            r1 = True
            r2 = True
            r3 = True
            for l in word:
                if l not in row_1:
                    r1 = False
                if l not in row_2:
                    r2 = False
                if l not in row_3:
                    r3 = False
            if r1 or r2 or r3: #at least one row hasn't been eliminated
                good.append(w)
        return good
