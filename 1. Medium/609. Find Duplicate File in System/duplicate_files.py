# Prompt: https://leetcode.com/problems/find-duplicate-file-in-system/
# Runtime: 80 ms, faster than 84.73% of Python online submissions for Find Duplicate File in System.
# Memory Usage: 29.8 MB, less than 45.04% of Python online submissions for Find Duplicate File in System.


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        fileMap = {} # maps content (key) to filepath (val)
        
        for p in paths:
            path = p.split(" ")
            directory = path[0]
            files = path[1:]
            
            for f in files:
                ff = f.split("(")
                filename = ff[0]
                content = ff[1][:-1] # remove close paren

                filepath = directory + "/" + filename
                if content in fileMap:
                    fileMap[content].append(filepath)
                else:
                    fileMap[content] = [filepath]
                    
        output = []
        for key in fileMap:
            # only add if there are duplicates
            if len(fileMap[key]) > 1:
                output.append(fileMap[key])
        
        return output
