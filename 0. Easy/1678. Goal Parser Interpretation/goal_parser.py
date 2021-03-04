# Prompt: https://leetcode.com/problems/goal-parser-interpretation/
# Runtime: 20 ms, faster than 48.96% of Python online submissions for Goal Parser Interpretation.
# Memory Usage: 13.7 MB, less than 8.51% of Python online submissions for Goal Parser Interpretation.


import re

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        command = re.sub("\(\)", "o", command)
        command = re.sub("\(al\)", "al", command)
        
        return command
