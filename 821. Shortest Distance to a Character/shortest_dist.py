# Prompt: https://leetcode.com/problems/shortest-distance-to-a-character/
class Solution:
    # after we find a C, we backtrack and update distances from previous letters
    def backtrack(self, distances: list, dist: int, current: int):
        count = 1
        for i in range(current-1, int(current-dist-1), -1):
            # only update if it's decreasing number (some might be closer to the previous C)
            if distances[i] > count or distances[i] == -1:
                distances[i] = count
            count += 1
            
    def shortestToChar(self, S: str, C: str) -> List[int]:
        distances = []
        prev = None # index of the C found previous to this one
        current = None # index of the last C found so far
        for i in range(len(S)):
            if S[i] == C:
                if prev == None:
                    prev = 0 - i # negative val makes toBacktrack go to beginning
                else:
                    prev = current
                current = i
                distances.append(0) # for the C
                toBacktrack = (current-prev)/2
                self.backtrack(distances, toBacktrack, current)
            elif current == None:
                # placeholder to be overwitten (we haven't found the first C yet)
                distances.append(-1)
            else:
                # distance from previous C
                distances.append(i - current)
        return distances
