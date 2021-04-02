# Prompt: https://leetcode.com/problems/design-browser-history/
# Runtime: 332 ms, faster than 24.17% of Python online submissions for Design Browser History.
# Memory Usage: 16.5 MB, less than 34.44% of Python online submissions for Design Browser History.


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.index = 0
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # clear forward history
        self.history = self.history[:self.index+1]
        # add new site
        self.history.append(url)
        self.index += 1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.index -= steps
        if self.index < 0:
            self.index = 0
        
        if len(self.history) == 0:
            return ""
        else:
            print(self.history)
            return self.history[self.index]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.index += steps
        if self.index > len(self.history) - 1:
            self.index = len(self.history) - 1
        
        if len(self.history) == 0:
            return ""
        else:
            return self.history[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
