# Prompt: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
# Runtime: 1160 ms, faster than 73.96% of Python online submissions for Restore the Array From Adjacent Pairs.
# Memory Usage: 68.4 MB, less than 86.11% of Python online submissions for Restore the Array From Adjacent Pairs.


class Solution(object):
    
    def findUnique(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        
        nums = set()
        
        for pair in adjacentPairs:
            one = pair[0]
            two = pair[1]
            if one in nums:
                nums.remove(one)
            else:
                nums.add(one)
            
            if two in nums:
                nums.remove(two)
            else:
                nums.add(two)
            
        return list(nums)
    
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        
        # find two unique numbers; they're going to be first and last
        unique = self.findUnique(adjacentPairs)
        
        valMap = {} # maps nums to pairs they occur in
        
        for i, pair in enumerate(adjacentPairs):
            one = pair[0]
            two = pair[1]
            if one in valMap:
                valMap[one].append(i)
            else:
                valMap[one] = [i]
                
            if two in valMap:
                valMap[two].append(i)
            else:
                valMap[two] = [i]
                
        elem = unique[0]
        currentPairId = -1
        nums = [elem]
        
        while elem != None:
            if elem not in valMap or elem == unique[1]: # we're at the last one
                elem = None
                return nums
            ids = valMap[elem]
            del valMap[elem]
            nextPairId = -1
            for i in ids:
                if i != currentPairId:
                    nextPairId = i
            nextPair = adjacentPairs[nextPairId]
            currentPairId = nextPairId
            
            for n in nextPair:
                if n != elem:
                    elem = n
                    nums.append(elem)
                    break
        
        
        return nums
