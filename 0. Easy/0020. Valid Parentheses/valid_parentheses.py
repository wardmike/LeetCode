class Solution:
    def isValid(self, s):
        op = ["(","[","{"]
        cp = [")","]","}"]
        pp = []
        for i in s:
            if i in op:
                pp.append(i)
            elif i in cp and len(pp) > 0:
                if i != cp[op.index(pp.pop())]:
                    return False
            else:
                return False
        return len(pp) == 0
