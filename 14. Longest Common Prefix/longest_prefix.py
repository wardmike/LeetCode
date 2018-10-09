class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        j = len(strs[0])
        # find the shortest word
        for word in strs:
            if len(word) < j:
                j = len(word)
        for i in range(0, j):
            for w in range(0, len(strs)-1):
                if strs[w][i] != strs[w+1][i]:
                    return strs[0][:i]
        return strs[0][:j]
