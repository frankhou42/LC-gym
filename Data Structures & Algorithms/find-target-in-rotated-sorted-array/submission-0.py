class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2
            
            #binary search to correct result
            if nums[m] == target:
                return m
            
            #formula to check if m is in left portion
            if nums[l] <= nums[m]:
                #if not in between left and mid shrink window
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                #if betweeen, binary search
                else:
                    r = m - 1

            elif nums[m] <= nums[r]:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1



