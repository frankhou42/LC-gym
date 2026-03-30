class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        for c in s:
            hashmap_s[c] = hashmap_s.get(c, 0) + 1

        hashmap_t = {}
        for c in t:
            hashmap_t[c] = hashmap_t.get(c, 0) + 1
        
        return hashmap_t == hashmap_s

#time: O(max(n, m)) space: O(n + m)