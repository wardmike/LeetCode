# Prompt: https://leetcode.com/problems/finding-the-users-active-minutes/
# Runtime: 1516 ms, faster than 7.57% of Python online submissions for Finding the Users Active Minutes.
# Memory Usage: 22.5 MB, less than 52.52% of Python online submissions for Finding the Users Active Minutes.


class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        uams = {} # maps user id to minutes active
        
        for l in logs:
            user = l[0]
            time = l[1]
            
            if user in uams:
                if time not in uams[user]:
                    uams[user].append(time)
            else:
                uams[user] = [time]
        
        counts = {} # maps UAM to count of users with that UAM
        
        for u in uams:
            c = len(uams[u])
            
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        
        answer = []
        for i in range(1,k+1):
            if i in counts:
                answer.append(counts[i])
            else:
                answer.append(0)
            
        return answer
