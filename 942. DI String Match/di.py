# Prompt: https://leetcode.com/problems/di-string-match/
class Solution:
    def diStringMatch(self, S):
        result = [0]
        high = 1 #always higher than anything in result list
        low = -1 #always lower than anything in result list
        for s in S:
            if s == 'I':
                result.append(high)
                high += 1
            else:
                result.append(low)
                low -= 1
        #normalizing list to between values 0 and n
        to_add = abs(min(result))
        return [x+to_add for x in result]
