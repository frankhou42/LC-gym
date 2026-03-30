class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        # to have O(1) access of for loop
        # to remove duplicate numbers for no additional check
        res = 0
        for num in nums:
            #set is can not be looped with index
            counter = 0
            #find start
            #start is any number that doesn't have number b4 it 
            #if there is number after it it doesn't matter
            # also if there is only one number that is always a one number sequence
            if (num - 1 not in nums):
                counter += 1
                #count the length of sequence for the start
                
                # num + counter as we want to keep updating the counter's length
                # we keep checking if the next element of num is in the arr
                while num + counter in nums:
                    counter += 1
                
                
              
                res = max(res, counter)
        
        return res