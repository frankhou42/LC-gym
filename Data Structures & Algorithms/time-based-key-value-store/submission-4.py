"""
key is key of hashmap, val and timestamp is the value

keep getting mid point of array. If that mid point's timestamp is valid
then we keep going to the right to find the maximum timestamp taht is smaller
than the input val. If the mid point's timestamp is not valid, aka 
bigger than the timestamp) go to left side
"""
class TimeMap:

    def __init__(self):
        self.container = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.container[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.container[key]:
            return ""
        values = self.container[key]
        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r)//2

            #go to left section to find bigger timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
