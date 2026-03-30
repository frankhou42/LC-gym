"""
Keep removing sorted halves to get pivot

compare left half including mid against right half

after removing all impossible sorted halves, the last
element if res
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            #pivot in right
            if nums[m] > nums[r]:
                l = m + 1
            #pivot in left
            else:
                r = m

        return nums[l]
