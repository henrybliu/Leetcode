class Solution:
    '''
    Decide which half to search depending on which half is sorted in ascending
    order.

    Time: O(logn)
    Space: O(1)
    '''
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<r:
            mid = l + (r-l)//2

            #search the left half
            if nums[mid]<nums[r]:
                r = mid

            #search the right half
            else:
                l = mid+1

        return nums[l]