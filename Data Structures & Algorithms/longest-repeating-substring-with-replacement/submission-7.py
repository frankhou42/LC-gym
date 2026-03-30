"""
The  valid substring is 
(length of substring - mostFreqCharCount) <= k

build global hashmap and remove elements and find max as we go

[abaa] k = 0

hashmap = {
    a:1
    b:0
}

mostFreq = 1
maxSubstring = 1
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        mostFreq = 0
        maxSubstring = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            mostFreq = max(mostFreq, hashmap[s[r]])
            while (r - l + 1 - mostFreq) > k:
                hashmap[s[l]] -= 1
                l += 1
            
            maxSubstring = max(maxSubstring, r - l + 1)
        
        return maxSubstring
            