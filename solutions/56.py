class Solution:
    '''
    It is easiest to just sort the intervals. We want to maintain the left side
    of the intervals to be sorted as we iterate through the intervals.
    
    Time: O(nlogn)
    Space: O(n)
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        #keep track of the l and r of the interval that we are currently creating
        r = intervals[0][1]
        l = intervals[0][0]

        for i in range(1,len(intervals)):
            currLeft = intervals[i][0]
            currRight = intervals[i][1]

            #merge the interval
            if currLeft <= r:
                #the right part we keep track should be the maximum
                r = max(r, currRight)
            
            #don't need to merge
            else:
                res.append([l, r])
                l = currLeft
                r = currRight

        #add the last interval
        res.append([l,r])

        return res
