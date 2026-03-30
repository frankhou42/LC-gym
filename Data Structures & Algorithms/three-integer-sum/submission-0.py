class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #avoid iteration over same num to do 2 sum
            #if see consecutive dup, skip to avoid dup res
            #i > 0 so thatwe don't compare the last element and first element
            if (i > 0 and a == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if (total > 0):
                    r -= 1
                elif (total < 0):
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    l+=1

                    #used to skip dup when doing two sum
                    #by moving start ptr to no dup, the while
                    #loop will automatically move the right ptr
                    #to the correct position
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
