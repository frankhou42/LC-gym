class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary seach need to have a sorted array

        l, r = 0, len(nums) - 1
        while l <= r: #keep searching as long as there is element between l and r inclusive
        #this means that we keep searching as long as there is element in the l and r window rnage, we continue to try to find the element.
            m = (l + r)//2
            if target == nums[m]:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1 #since m is not equal to tgt can be dismissed
        return -1