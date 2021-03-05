# Prompt: https://leetcode.com/problems/partition-labels/
# Runtime: 24 ms, faster than 89.42% of Python online submissions for Partition Labels.
# Memory Usage: 13.6 MB, less than 37.33% of Python online submissions for Partition Labels.


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        lastPos = {} # maps letters last position they appear
        
        partitionEnds = []
        
        for i, s in enumerate(S):
            lastPos[s] = i # overwrites previous one
        
        currentPartitionEnd = 0
        for i, s in enumerate(S):
            if i > currentPartitionEnd:
                # save end of partition
                partitionEnds.append(currentPartitionEnd)
                # next partition must go until at least the last occurrence
                # of its first letter
                currentPartitionEnd = lastPos[s]
            else:
                if lastPos[s] > currentPartitionEnd:
                    # since each letter can only occur in one partition, this
                    # partition must go until at least this letter's last occurrence
                    currentPartitionEnd = lastPos[s]
        
        partitions = []
        lastPartitionEnd = -1
        for p in partitionEnds:
            partitions.append(p - lastPartitionEnd)
            lastPartitionEnd = p
        
        partitions.append(len(S) - 1 - lastPartitionEnd)
        
        return partitions
