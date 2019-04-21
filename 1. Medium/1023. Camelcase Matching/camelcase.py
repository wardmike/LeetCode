# Prompt: https://leetcode.com/problems/camelcase-matching
# Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Camelcase Matching.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Camelcase Matching.
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        for query in queries:
            i_pattern = 0 # index as we loop through the pattern
            fitPattern = True
            for i in query:
                if i_pattern < len(pattern) and i == pattern[i_pattern]:
                    i_pattern += 1
                elif i.islower():
                    # we won't actually add lowercase letter to save time; just continue
                    continue
                else: # breaks the pattern
                    fitPattern = False
                    break
            if i_pattern != len(pattern): # we didn't get through all of "pattern"
                fitPattern = False
            result.append(fitPattern)
        return result
