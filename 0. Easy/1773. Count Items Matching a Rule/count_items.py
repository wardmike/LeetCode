# Prompt: https://leetcode.com/problems/count-items-matching-a-rule/
# Runtime: 212 ms, faster than 100.00% of Python online submissions for Count Items Matching a Rule.
# Memory Usage: 21 MB, less than 100.00% of Python online submissions for Count Items Matching a Rule.


class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        matched = 0
        
        for item in items:
            if ruleKey == "type":
                if ruleValue == item[0]:
                    matched += 1
            elif ruleKey == "color":
                if ruleValue == item[1]:
                    matched += 1
            elif ruleKey == "name":
                if ruleValue == item[2]:
                    matched += 1
        
        return matched
