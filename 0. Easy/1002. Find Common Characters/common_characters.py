# Prompt: https://leetcode.com/problems/find-common-characters/submissions/
import copy

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        #change strings to lists (since strings aren't mutable)
        input_lists = []
        for a in A:
            input_lists.append(list(a))
        output = []
        #deep copy so it'll still traverse all letters after we remove from the first word
        first_word = copy.deepcopy(input_lists[0])
        for c in first_word:
            found_in_all = True #letter was found in all words
            for lst in input_lists:
                if c not in lst:
                    found_in_all = False
                    break
            if found_in_all:
                output.append(c)
                #remove from all lists (makes counting easier)
                for lst in input_lists:
                    lst.remove(c)
        return output
