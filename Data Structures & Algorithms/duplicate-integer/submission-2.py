class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for i in range(len(nums)):
            if nums[i] in new:
                return True
            new.append(nums[i])
        
        return False