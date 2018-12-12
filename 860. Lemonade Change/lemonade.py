# Prompt: https://leetcode.com/problems/lemonade-change/
class Solution:
    def lemonadeChange(self, bills):
        num5 = 0
        num10 = 0
        for bill in bills:
            if bill == 5:
                num5 += 1
            elif bill == 10:
                if num5 > 0:
                    num5 -= 1
                    num10 += 1
                else:
                    return False
            elif bill == 20:
                #try to give change of 10+5 first, as 5s are more valuable to keep
                if num10 > 0 and num5 > 0:
                    num5 -= 1
                    num10 -= 1
                elif num5 > 2:
                    num5 -= 3
                else:
                    return False
        return True
