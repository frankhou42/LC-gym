class TimeMap:

    def __init__(self):
        self.container = defaultdict(list)
  

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.container[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
      
      res = ""
      arr = self.container[key]
      if not arr:
        return ""
      
      l = 0
      r = len(arr) - 1
      
      while l <= r:
        mid = (l + r) // 2
        if arr[mid][1] <= timestamp:
          res = arr[mid][0]
          l = mid + 1
        else:
          r = mid - 1
          
      return res
      