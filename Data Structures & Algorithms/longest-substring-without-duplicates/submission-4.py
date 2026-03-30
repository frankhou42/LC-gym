"""
keep a set of unique characters, 
we keep iterating throughthe arr, if we see dup we keep
moving l ptr and remove elements from set to 
shrink the window size until no dup
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        longest = 0
        substring = set()
        for r in range(len(s)):
            #see dup shrink window from left
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            
            longest = max(longest, r - l + 1)
            substring.add(s[r])


        return longest
            