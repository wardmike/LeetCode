# Prompt: https://leetcode.com/problems/rabbits-in-forest/
# Runtime: 32 ms, faster than 67.92% of Python online submissions for Rabbits in Forest.
# Memory Usage: 13.6 MB, less than 62.26% of Python online submissions for Rabbits in Forest.


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        
        uniqueColors = {} # maps counts to occurrances of the count
        total = 0
        
        for answer in answers:
            if answer is 0:
                # each rabbit that answers 0 is unique; they're all different colors
                total += 1
            elif answer in uniqueColors:
                uniqueColors[answer] += 1
                if uniqueColors[answer] > answer:
                    # we've found all bunnies of this color, so we'll add to total
                    # and reset in case this number is used for a different color
                    total += answer + 1
                    del uniqueColors[answer]
            else:
                uniqueColors[answer] = 1
        
        for colorCount in uniqueColors:
            total += colorCount + 1 # add one for the rabbit giving the answer
        
        return total
