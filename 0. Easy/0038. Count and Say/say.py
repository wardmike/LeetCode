# Prompt: https://leetcode.com/problems/count-and-say/
# This might be optimized with DP, but I think Leetcode re-runs all the code on every test case (DP was slower).
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1" # item in squence
        for i in range(1, n):
            ss = [] # next s
            num = s[0] # previous num
            count = 1 # count of similar consequative previous nums 
            for j in range(1, len(s)):
                # check if it's the same as the one before
                # can't be added to ss until j+1, because next one might be the same
                if s[j] == num:
                    count += 1
                else:
                    ss.append(str(count))
                    ss.append(str(num))
                    num = s[j]
                    count = 1
            if count > 0: # append for the last one
                ss.append(str(count))
                ss.append(str(num))
            s = ''.join(ss) # set s to ss
        return s
                
