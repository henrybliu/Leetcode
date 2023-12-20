from collections import defaultdict

class TimeMap:
    '''
    get() can be optimized with binary search on the times for each key.

    Time: O(1) for set() and O(logn) for get()
    Space: O(n)
    '''

    def __init__(self):
        self.keyToTime = defaultdict(list)
        self.keyTimeToVal = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToTime[key].append(timestamp)
        self.keyTimeToVal[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        # if the key doesn't exist or the timestamp is too early
        if key not in self.keyToTime or timestamp < self.keyToTime[key][0]:
            return ""
        print(key, timestamp)
        greatestTime = self.binarySearch(self.keyToTime[key], timestamp)
        return self.keyTimeToVal[(key, greatestTime)]

    def binarySearch(self, timestamps, maxTime):
        # array of timestamps with the largest time being <= maxTime

        l = 0
        r = len(timestamps)-1
        highest = 0

        while l <= r:
            mid = l+(r-l)//2
            
            if timestamps[mid] == maxTime:
                return timestamps[mid]
            elif timestamps[mid] < maxTime:
                highest = timestamps[mid]
                l = mid+1
            else:
                r = mid-1
        
        return highest


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)