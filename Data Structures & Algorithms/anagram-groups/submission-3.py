class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a hashmap that has an array of a-z as key and has the string itself as the value
        
        dictionary = defaultdict(list)#tells default value, use type

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            dictionary[tuple(arr)].append(s)
            #keys can't be arr, has to be a tuple
        
        return dictionary.values()

            