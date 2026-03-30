class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
         
        while l <= r:
            m = (l + r)//2
            #if m is in right portion we want to serach towards the left
            #if m in left portion we want to seaarch towards the right
            #when we find a sorted portion we would just return the leftmost value as
            #we find min as we have the correct direction to search
            
            #if sorted portion just return leftmost
            if nums[l] < nums[r]:
                return min(res, nums[l])#incase underflow to left section
            
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
        return res


