class Solution:
    '''
    After squaring the values, we can realize that the largest values will
    either be in the middle of nums or at the beginning -- if there are no
    negative values. Then using a two pointer approach, we create the resulting
    array from the back to the front, adding the larger of the two pointer's
    squared value.
    
    Time: O(n)
    Space: O(n)
    '''
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        resIdx = -1

        l = 0
        r = len(nums)-1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[resIdx]=(nums[l]**2)
                l+=1
            else:
                res[resIdx]=(nums[r]**2)
                r-=1
            resIdx-=1

        return res
