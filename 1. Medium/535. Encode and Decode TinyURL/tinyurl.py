# Prompt: https://leetcode.com/problems/encode-and-decode-tinyurl/
# Runtime: 12 ms, faster than 97.74% of Python online submissions for Encode and Decode TinyURL.
# Memory Usage: 13.2 MB, less than 97.74% of Python online submissions for Encode and Decode TinyURL.

class Codec:
    tinyUrls = {}
    nextId = int("111111", 16)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tinyUrl = hex(self.nextId)
        self.tinyUrls[tinyUrl] = longUrl
        self.nextId += 1
        return tinyUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.tinyUrls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
