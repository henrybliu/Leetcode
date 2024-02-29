class Solution:
    '''
    We can count the number of subarrays that can be created at each position
    of the nums array. If the current product is greater than or equal to k, 
    then we need to keep dividing from the current product while decreasing the
    number of subarrays that can be created at the current position and 
    incrementing the left pointer to shrink the window size

    Example:

    10  5   2   6

    the number of subarrays that can be created
    at each position: 

    1   2   3   4

    If a current product were to be larger or equal to k, then we would shrink
    the number of subarrays that can be created thus far. Shrinking the number
    of subarrays that can be created in earlier positions of the nums array
    will also affect the number of subarrays that can be created in later parts
    of the array because both subarrays should exclude the earlier parts of the
    array.

    Time: O(n)
    Space: O(1)
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        currProduct = 1
        l = 0
        numSubArrays = 0

        for r in range(len(nums)):
            currProduct *= nums[r]
            numSubArrays +=1

            while currProduct >= k and l <= r:
                currProduct = currProduct // nums[l]
                l+=1
                numSubArrays -= 1

            count += numSubArrays

        return count