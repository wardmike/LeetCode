# Prompt: https://leetcode.com/problems/validate-stack-sequences/
# Runtime: 56 ms, faster than 68.30% of Python online submissions for Validate Stack Sequences.
# Memory Usage: 13.4 MB, less than 91.98% of Python online submissions for Validate Stack Sequences.


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        popIndex = 0
        
        for p in pushed:
            stack.append(p)
            
            # pop off as many as possible
            while len(stack) > 0 and popped[popIndex] == stack[-1]:
                stack.pop()
                popIndex += 1
                # we've gone through entire "popped" list
                if popIndex > len(popped) - 1:
                    return True
        
        # check if we've gone through entire "popped" list
        return popIndex > len(popped) - 1
