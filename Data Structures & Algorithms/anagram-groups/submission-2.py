class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmp dict = [count[tuple] : list[str]]
        dictionary = defaultdict(list) #edge case

        #use for each loop cuz we want each element directly
        for s in strs:
            #count[a-z] 26 len make sure avg O(1) iteration
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1 #use ord to get ASCII, c is any char

            dictionary[tuple(count)].append(s)
            #added str to its key of count

        return dictionary.values()

            


        
