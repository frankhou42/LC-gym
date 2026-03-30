class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #put everything in hashset
        #check if already in, if so return false
        #after everything return true

        hashset = set()

        for i in range(0, len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        
        return False
         