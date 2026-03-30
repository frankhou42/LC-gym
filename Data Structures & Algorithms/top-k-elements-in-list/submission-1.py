class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first build num freq hashmap then
        #use bucket sort where we use an array of nums size for maximum len(nums) frequency for each num and each element is the number 

        #in the end just loop from back to front to k elements

        res = []
        arr = [[] for _ in range(len(nums) + 1)]
        #first bucket is always empty so we can't use 0 the hightest frequency is len(nums) + 1  
        #each bucket can have multiple nums since nums can have same freq
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1 # add one since we just seen a num freq
            #hashmap.get gets value of a key, the second param is the default value if key doesn't exists
        
        #.item to get tuple of key and value use two iterators to get key and value
        for key, value in hashmap.items():
            arr[value].append(key)

        for i in range(len(nums), 0, -1) :
            for num in arr[i]:
                #if empty don't append anything
                res.append(num)
                if len(res) == k:
                    return res


        #Summary:
        # each bucket has an array of number of numbers of that index frequency
        # we have a bucket array of len(nums)+1 since 0 doesn't count and thats the highest frequency
        # hashmap.get() method is same as hashmap[key], the 0 is default and we add 1
        # because we seen one
        # Essentially create num freq hashmap and make bucket sort and print from back 
        # and append all val from bucket
        

                
