# Prompt: https://leetcode.com/problems/score-of-parentheses/
# Runtime: 32 ms, faster than 8.00% of Python online submissions for Score of Parentheses.
# Memory Usage: 13.5 MB, less than 28.00% of Python online submissions for Score of Parentheses.

class Solution(object):
    
    # returns if a combination of parentheses is valid (all opening parens are closed)
    def isBalanced(self, S):
        """
        :type S: str
        :rtype: boolean
        """
        opens = 0
        for i, p in enumerate(S):
            if p == "(":
                opens += 1
            elif p == ")":
                opens -= 1
            if opens < 0:
                return False
        return True
    
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S == "()": # simplest unit
            return 1
        elif len(S) > 3 and S[:2] == "((" and S[-2:] == "))" and self.isBalanced(S[1:-1]): # S is in format (A)
            return 2 * self.scoreOfParentheses(S[1:-1])
        else: # S is in format A + B
            # find closing paren to match S[0]
            # div represents the split between A and B
            opens = 0
            div = 0
            for i, p in enumerate(S):
                if p == "(":
                    opens += 1
                elif p == ")":
                    opens -= 1
                    if opens == 0:
                        div = i + 1
                        break
            
            return self.scoreOfParentheses(S[:div]) + self.scoreOfParentheses(S[div:])
