# Prompt: https://leetcode.com/problems/number-of-recent-calls/
class RecentCounter:
    """ this is a brute-force solution that is only faster than
    1% of submissions. I will try to improve the performance """
    def __init__(self):
        self.log = [] #each element will be the time of its ping
    
    def update_log(self, t : 'int'):
        #go through the log and remove entries over 3000 ms ago
        i = 0
        while (i < len(self.log)):
            if self.log[i] + 3000 < t:
                del self.log[i]
            else:
                i += 1

    def ping(self, t: 'int') -> 'int':
        self.log.append(t)
        self.update_log(t)
        return len(self.log)
