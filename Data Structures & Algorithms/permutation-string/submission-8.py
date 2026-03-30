"""
The  valid substring is 
(length of substring - mostFreqCharCount) <= k

build global hashmap and remove elements and find max as we go
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
                #first decrement hashmap then move l ptr
                #so that we don't forget to remove the first
                #element from hashmap
                hashmap[s[l]] -= 1
                l += 1
            
            maxSubstring = max(maxSubstring, r - l + 1)
        
        return maxSubstring
            