# Prompt: https://leetcode.com/problems/sort-characters-by-frequency/
# Runtime: 280 ms, faster than 10.45% of Python online submissions for Sort Characters By Frequency.
# Memory Usage: 16.6 MB, less than 40.72% of Python online submissions for Sort Characters By Frequency.

class Solution(object):
    def __init__(self):
        # map of character to frequency
        self.freq = {}
    
    
    def moreFrequent(self, a, b):
        return -1 if self.freq[a] > self.freq[b] else 1
    
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # populate map
        for char in s:
            if char in self.freq:
                self.freq[char] += 1
            else:
                self.freq[char] = 1
                
        # make each frequency unique by adding a fraction based on unicode val of character
        # this will ensure characterss with equal frequencies are "clumped" together with
        # their own type by sort function
        for i, n in self.freq.items():
            self.freq[i] = n + (ord(i) / 1000.0)
        
        # sort and format as string
        return ''.join(sorted(s, cmp=self.moreFrequent))
