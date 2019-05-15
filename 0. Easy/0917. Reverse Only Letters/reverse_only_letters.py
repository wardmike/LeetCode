# Prompt: https://leetcode.com/problems/reverse-only-letters

# using two-pointer method, where each pointer will represent letters
# letters are swapped & then pointers are adjusted inwards to find the next letters

# Runtime: 16 ms, faster than 98.50% of Python online submissions for Reverse Only Letters.
# Memory Usage: 11.8 MB, less than 35.46% of Python online submissions for Reverse Only Letters.


class Solution(object):
    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    
    def reverseOnlyLetters(self, S):
        # two-pointer method
        S_list = list(S)
        begin_index = 0
        end_index = len(S_list) - 1
        while begin_index < end_index:
            if S_list[begin_index].isalpha() and S_list[end_index].isalpha():
                self.swap(S_list, begin_index, end_index)
                begin_index += 1
                end_index -= 1
            elif not S_list[begin_index].isalpha():
                begin_index += 1
            elif not S_list[end_index].isalpha():
                end_index -= 1
            else:
                break
        return ''.join(S_list)
            
        
