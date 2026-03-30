class TimeMap:

    def __init__(self):
        self.con = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #create empty list if not exist
        if key not in self.con:
            self.con[key] = []
        
        #add value, timestamp list to list
        self.con[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.con.get(key, []) 
        #if key doesn't exist give empty list which just return "" for res 
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r)//2
            #timestamps are in increasing order
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
                                          
