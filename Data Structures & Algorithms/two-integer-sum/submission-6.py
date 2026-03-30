class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in dictionary:
                #return the diff prev stored and its index and curr index
                return [dictionary[diff], i]
            else:
                #if not add to dict with num:index
                dictionary[nums[i]] = i
            
        