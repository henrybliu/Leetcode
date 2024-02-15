class Solution:
    '''
    We want to find the latest number that is less than the prefixSum. If yes,
    we want to include this number in the result. If not, we skip it and try
    the next number. We also sort the numbers to easily keep taking on smaller
    values, and to follow the problem example.

    Time: O(nlogn)
    Space: O(1)    
    '''
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        prevSum = 0

        for num in nums:
            if prevSum > num:
                res = prevSum + num
            prevSum += num

        return res

        
