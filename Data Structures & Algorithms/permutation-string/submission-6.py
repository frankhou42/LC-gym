"""
we first construct a charFreq arr of len 26 for s1. Then we iterate through
s2 of len(s1) sized window to see for each possible window if there is match
to charFreq of s1
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charFreq = [0] * 26
        for c in s1:
            index = ord(c) - ord('a')
            charFreq[index] += 1
        
        l, r = 0, len(s1) - 1
        windowCharFreq = [0] * 26
        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            windowCharFreq[index] += 1
        
        while r < len(s2):
            if windowCharFreq == charFreq:
                return True
            if r != len(s2) - 1:
                windowCharFreq[ord(s2[l]) - ord('a')] -= 1
                #edge case at last window, r + 1 out of bounds, don't 
                windowCharFreq[ord(s2[r + 1]) - ord('a')] += 1
            l+=1
            r+=1

        return windowCharFreq == charFreq

#time O(n) space O(1)
        