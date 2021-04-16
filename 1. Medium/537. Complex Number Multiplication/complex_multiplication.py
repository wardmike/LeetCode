# Prompt: https://leetcode.com/problems/complex-number-multiplication/
# Runtime: 12 ms, faster than 96.67% of Python online submissions for Complex Number Multiplication.
# Memory Usage: 13.6 MB, less than 18.33% of Python online submissions for Complex Number Multiplication.


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        aArr = a.split('+')
        bArr = b.split('+')
        
        aReal = int(aArr[0])
        aImag = int(aArr[1][:-1]) # strip 'i' off
        
        bReal = int(bArr[0])
        bImag = int(bArr[1][:-1])
        
        # use foil method
        first = aReal * bReal
        outer = aReal * bImag
        inner = aImag * bReal
        last = aImag * bImag
        
        answerReal = first - last # last is negative because i^2 = -1
        answerImag = outer + inner
        
        return str(answerReal) + "+" + str(answerImag) + "i"
