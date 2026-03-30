"""
Goal: Go through every valid window by moving r ptr, if window
is not valid, move l ptr until window is valid again, update maxSubstring
as we go through each valid window

(window length - max frequency c) <= k determines validity
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        maxSubstring = 0
        maxCharFreq = 0
        for r in range(len(s)):
            #check window validity
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            #find maxCharFreq in window
            maxCharFreq = max(hashmap[s[r]], maxCharFreq)
            #invalid case:
            while r - l + 1 - maxCharFreq > k:
                if hashmap[s[l]] > 0:
                    hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                l += 1
            #valid case:
            maxSubstring = max(r - l + 1, maxSubstring)
        return maxSubstring

