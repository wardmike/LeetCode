class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for move in moves:
            if move is "U":
                y += 1
            elif move is "D":
                y -= 1
            elif move is "R":
                x += 1
            elif move is "L":
                x -= 1
        return x is 0 and y is 0
        
