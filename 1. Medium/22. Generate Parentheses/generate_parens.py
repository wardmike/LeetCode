# Prompt: https://leetcode.com/problems/generate-parentheses/
# Runtime: 16 ms, faster than 94.64% of Python online submissions for Generate Parentheses.
# Memory Usage: 14 MB, less than 7.32% of Python online submissions for Generate Parentheses.

class Solution(object):
    def __init__(self):
        # holds possible combinations
        self.combos = []
    
    # adds all combinations of the next parenthesis
    def addParen(self, soFar, size, opens):
        """
        :type soFar: str
        :type size: int
        :type opens: int
        :rtype: None
        """
        if len(soFar) == size:
            # we've reached the size we want
            self.combos.append(soFar)
            return

        if len(soFar) == 0:
            # must always start with open
            self.addParen("(", size, 1)
        else:
            if opens < size / 2:
                # can't have more than half be open
                self.addParen(soFar + "(", size, opens+1)
            if opens > len(soFar) / 2:
                # can't close if there's not enough opens to close
                self.addParen(soFar + ")", size, opens) 
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.addParen("", n*2, 0)
        return self.combos
