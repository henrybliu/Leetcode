class Solution:
    '''
    Can do this in two passes. Use an array where the index is the number and
    the value is the number of occurrences.

    Time: O(n)
    Space: O(n)
    '''
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = [0 for _ in range(len(nums)+1)]

        for num in nums:
            counts[num]+=1

        missingNum = 0
        repeatedNum = 0
        for i in range(len(counts)):
            if counts[i]==0:
                missingNum = i
            elif counts[i]==2:
                repeatedNum = i

        return [repeatedNum, missingNum]
            

