# Prompt: https://leetcode.com/problems/group-anagrams/
# Runtime: 76 ms, faster than 95.59% of Python online submissions for Group Anagrams.
# Memory Usage: 17.3 MB, less than 84.13% of Python online submissions for Group Anagrams.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # map alphabetical order (key) to anagrams found in strs (values)
        anagrams = {}
        
        for s in strs:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        
        return anagrams.values()
