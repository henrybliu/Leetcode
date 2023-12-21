class Solution:
    '''
    We can use 4 different for-loops to have a linear time complexity of
    computing the largest, second largest, smallest, and second smallest
    values.

    Time: O(n)
    Space: O(1)
    '''
    def maxProductDifference(self, nums: List[int]) -> int:
        # find the two largest and two smallest values

        maxVal = float('-inf')
        maxIdx = 0

        for i in range(len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxIdx = i

        nextLargestVal = float('-inf')
        for i in range(len(nums)):
            if nums[i] >= nextLargestVal and i != maxIdx:
                nextLargestVal = nums[i]


        smallestVal = float('inf')
        smallestIdx = 0

        for i in range(len(nums)):
            if nums[i] < smallestVal:
                smallestVal = nums[i]
                smallestIdx = i

        nextSmallestVal = float('inf')
        for i in range(len(nums)):
            if nums[i] <= nextSmallestVal and i != smallestIdx:
                nextSmallestVal = nums[i]

        return (maxVal * nextLargestVal)-(smallestVal * nextSmallestVal)