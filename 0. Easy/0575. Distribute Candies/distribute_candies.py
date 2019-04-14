class Solution:
    def distributeCandies(self, candies):
        # find number of unique candies
        u = len(set(candies))
        # find amount of candies given to sister
        s = len(candies) / 2
        # the max unique candies given to the sister
        # is the minimum between the total unique
        # candies and the amount given to her
        return int(min(s, u))
        
