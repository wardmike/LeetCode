# Prompt: https://leetcode.com/problems/fizz-buzz

# Runtime: 60 ms, faster than 27.94% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 14.2 MB, less than 5.17% of Python3 online submissions for Fizz Buzz.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            if output == "":
                output = str(i)
            result.append(output)
        return result
