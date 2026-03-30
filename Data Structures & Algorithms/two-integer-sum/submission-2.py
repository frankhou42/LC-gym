class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {};

        #build hashmap while looping through the arr of {num:index}

        #when there is a repeat value we can just update to the new index
        # since its only 2 values, we can just 

        for i in range(len(nums)):
            diff = target - nums[i]

            #return dictionary immediately when diff is found
            if diff in dictionary:
                # return the first value which is stored in the dict and then return the later value that we are loop on
                return [dictionary[diff], i]
            
            dictionary[nums[i]] = i
        