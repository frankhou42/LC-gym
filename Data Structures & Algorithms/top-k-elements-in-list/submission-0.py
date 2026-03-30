class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        count = [[] for i in range(len(nums) + 1)] 
        #each bucket has a list in case there's multiple nums
        #count must be size of len + 1 since we include the 0 so that we can reach index of the desired length

        #make num:freq dict
        for num in nums:
            dictionary[num] = 1 + dictionary.get(num,0)
            
        #populate buckets
        for num, freq in dictionary.items():
            count[freq].append(num)
        
        res = []
        #loop through buckets from back (most freq)
        for i in range(len(nums), 0, -1): #stop is exclusive
            curr_bucket = count[i]
            #loop through each element in bucket and append
            for num in curr_bucket:
                res.append(num)
                if (len(res) == k):
                    return res

             


