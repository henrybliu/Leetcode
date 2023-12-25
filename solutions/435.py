class Solution:
    '''
    Count the number of intervals that we can keep -- this can be determined by
    the maximizing the number of intervals that end before the next start.

    Time: O(nlogn)
    Space: O(n)
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort by index 1 or end time
        intervals.sort(key = lambda x:x[1])
        
        latest = intervals[0][1]
        #count is 1 because we can keep the current interval with the earliest end time
        count = 1

        #want to count how many intervals that we can keep
        for i in range(1, len(intervals)):
            #if there is no overlap
            if latest <= intervals[i][0]:
                latest = intervals[i][1]
                count+=1

        #number of intervals needed to be dropped
        return len(intervals)-count
