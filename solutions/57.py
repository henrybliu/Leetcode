class Solution:
    '''
    This is the same as merge intervals except that we just need to add this
    new interval first.
    
    Time: O(nlogn)
    Space: O(n)
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:     
        #add the new interval to existing intervals   
        intervals.append(newInterval)
        intervals.sort()

        #merge remaining intervals
        res = []

        #maintain the left and right of what we have already "merged" or checked
        l = intervals[0][0]
        r = intervals[0][1]

        for i in range(1, len(intervals)):
            currL = intervals[i][0]
            currR = intervals[i][1]

            #there is overlap
            if currL <= r:
                r = max(r, currR)

            else:
                #there is no overlap, so add what we have merged
                res.append([l,r])
                l = currL
                r = currR

        res.append([l,r])

        return res
        