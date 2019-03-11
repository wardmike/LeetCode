# Prompt: https://leetcode.com/problems/find-the-difference/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # convert to list so that letters can be removed easily
        ss = list(s)
        tt = list(t)
        for i in tt:
            if i not in ss:
                return i
            ss.remove(i)
        return ""
