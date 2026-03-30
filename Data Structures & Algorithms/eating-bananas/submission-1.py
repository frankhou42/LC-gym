class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        #since trying find smallest, set to upper bound!
        optimalk = r

        #search for the most optimal eating speed from an array of all possible eating speed
        #optimal eating speed is the slowest eating speed while smaller or equal to limited hour
        #since ks is sorted we can binary serach the eating speed window
        while l <= r:
            m = (l+r)//2
            #check the hours requires for this eating speed
            totalh = 0
            for p in piles:
                #find total hrs for current mid pile we have
                totalh += math.ceil(p/m)

            #change window depending on totalh
            if totalh <= h:
                #update optimal if we find slower eating speed under hour restriction
                optimalk = m
                r = m - 1
            else:
                l = m + 1

        return optimalk