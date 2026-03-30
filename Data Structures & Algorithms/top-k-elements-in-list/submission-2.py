"""
Trick: use bucket sort where array index is frequency and array
value is the number

We create an array that holds index as frequency and value is
the number by using a hashmap the contains frequency of each number
We do this since we can't order hashmap.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        arr = [[] for _ in range(len(nums) + 1)] 
        #maximum freq in len(nums), multiple nums can have same freq
        #[[]]* len(nums) creates the same list repeatedly
        #+1 in case of freq = 0

        for num, freq in freqMap.items():
            arr[freq].append(num)

        res = []
        for i in range(len(arr) - 1, -1, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

#time O(n), #space O(n)