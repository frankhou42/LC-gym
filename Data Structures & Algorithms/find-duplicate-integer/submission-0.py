class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #start at index 0
        slow, fast = 0, 0
        #Find the intersection of fast and slow ptr (since there is a cycle)
        while True:
            #move slow and fast ptr to its next location
            slow = nums[slow] #go to the next index
            fast = nums[nums[fast]]#go to the next next index
            if slow == fast:
                break
        
        #Now set slow2 ptr at head, move slow2 and slow until the meet
        #the intersection is the dup
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow