class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        #initiate the first window comparision by initiating the window hashmap and hasmap of s1
        for i in range (len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        #find the initial number of matches
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        #move R and L to iterate through s2 sliding window
        #essentially the window will be s1 long but
        #it will have a l ptr that is one less than the window
        #as we have to remove the element we just passed by from
        #the array
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            #add the character to the hasmap
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
                #matrches only gets decrement if it previously is a match and now isn't a match
                #just cause two values aren't the same doesn't mean one less match
                #they can previously be 2 and 1 and now its 3 and 1, the number of matches is still the same
                #so we don't decrement based on if the two values are the same we only decrement if
                #previously was a match and because new chagnes now isn't a match

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26