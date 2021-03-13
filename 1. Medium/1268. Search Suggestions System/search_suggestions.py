# Prompt: https://leetcode.com/problems/search-suggestions-system/
# Runtime: 56 ms, faster than 96.62% of Python online submissions for Search Suggestions System.
# Memory Usage: 15.7 MB, less than 26.57% of Python online submissions for Search Suggestions System.


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort() # lexicographically sort
        output = []
        
        prefix = ""
        i = 0
        for letter in searchWord:
            prefix += letter
            
            toAdd = []
            
            # advance i to first search word that starts with prefix
            # because products is lexicographically sorted, i never has to retreat
            while i < len(products) and products[i][:len(prefix)] != prefix:
                i += 1
            
            if i < len(products):
                toAdd.append(products[i])
                
                # see if a second search word matches prefix (don't advance i)
                if i+1 < len(products) and products[i+1][:len(prefix)] == prefix:
                    toAdd.append(products[i+1])
                
                # see if a third search word matches prefix (don't advance i)
                if i+2 < len(products) and products[i+2][:len(prefix)] == prefix:
                    toAdd.append(products[i+2])
            
            
            output.append(toAdd)
            
        return output
