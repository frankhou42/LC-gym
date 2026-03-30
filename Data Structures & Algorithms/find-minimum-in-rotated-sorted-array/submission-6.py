"""
Keep removing sorted halves; when what's left is sorted
or size 1, you've found the minimum
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            # if current range is sorted, leftmost is minimum
            if nums[l] < nums[r]:
                return nums[l]

            mid = (l + r) // 2

            # left side is sorted → min must be on right
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                # left side is not sorted → min is in [l ... mid]
                r = mid

        return nums[l]