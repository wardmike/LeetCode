# Prompt: https://leetcode.com/problems/reverse-string
"""
 Notes: Do not return anything, modify s in-place instead.
"""
# Runtime: 176 ms, faster than 60.18% of Python3 online submissions for Reverse String.
# Memory Usage: 17.6 MB, less than 11.40% of Python3 online submissions for Reverse String.
class Solution:
    def swap(self, s: List[str], a: int, b: int):
        temp = s[a]
        s[a] = s[b]
        s[b] = temp
        
    def reverseString(self, s: List[str]) -> None:
        end = len(s) - 1
        begin = 0
        while end > begin:
            self.swap(s, begin, end)
            end -= 1
            begin += 1
        
