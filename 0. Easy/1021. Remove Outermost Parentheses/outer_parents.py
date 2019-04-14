# Prompt: https://leetcode.com/problems/remove-outermost-parentheses
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        output = []
        nest = 0 # nest level
        for i in range(len(S)):
            if S[i] == '(':
                if nest != 0:
                     # add if it's not an outer paren
                    output.append(S[i])
                nest += 1
            elif S[i] == ')':
                nest -= 1
                if nest != 0:
                    # add if it's not an outer paren
                    output.append(S[i])
        return ''.join(output)
