# Prompt: https://leetcode.com/problems/flood-fill

# Notes: this solution uses a recursive algorithm to change the color on each pixel & then check all neighbors (neighbor who called will be viisted but will already be changed & recursion will stop there; I tried preventing re-visiting the pixels, but that took longer due to the checks)

# Runtime: 68 ms, faster than 51.48% of Python3 online submissions for Flood Fill.
# Memory Usage: 13.2 MB, less than 6.33% of Python3 online submissions for Flood Fill.

class Solution:
    def fillPixelRecursive(self, image: List[List[int]], r: int, c: int, origColor: int, newColor: int):
        if image[r][c] == origColor:
            image[r][c] = newColor
            # only try directions if current pixel is origColor
            if c > 0:
                self.fillPixelRecursive(image, r, c-1, origColor, newColor)
            if c < len(image[0]) - 1:
                self.fillPixelRecursive(image, r, c+1, origColor, newColor)
            if r > 0:
                self.fillPixelRecursive(image, r-1, c, origColor, newColor)
            if r < len(image) - 1:
                self.fillPixelRecursive(image, r+1, c, origColor, newColor)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if sc < 0 or sr < 0 or sc >= len(image[0]) or sr >= len(image):
            return image
        origColor = image[sr][sc]
        if origColor == newColor:
            return image
        # modifies image in-place
        self.fillPixelRecursive(image, sr, sc, origColor, newColor)
        return image
        
