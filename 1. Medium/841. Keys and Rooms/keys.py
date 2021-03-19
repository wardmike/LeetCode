# Prompt: https://leetcode.com/problems/keys-and-rooms/
# Runtime: 52 ms, faster than 52.33% of Python online submissions for Keys and Rooms.
# Memory Usage: 14 MB, less than 81.00% of Python online submissions for Keys and Rooms.


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        
        keys = rooms[0]
        visited[0] = True
        
        while len(keys) != 0:
            newKeys = []
            for k in keys:
                newKeys += rooms[k]
                rooms[k] = []
                visited[k] = True
            keys = newKeys
        
        for v in visited:
            if v == False:
                return False
        return True
