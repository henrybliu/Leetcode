class Solution:
    """
    Can use the prefix sum and to then compute the smallest sum in nums. The
    result would then just be 1 plus the smallest prefix sum if the prefix sum
    is ever less than 1, we will return the absolute value of that plus 1.
    Otherwise, we can return 1.

    """

    def minStartValue(self, nums: List[int]) -> int:
        smallestSum = float("inf")
        currSum = 0

        for num in nums:
            currSum += num
            smallestSum = min(smallestSum, currSum)

        if smallestSum < 1:
            return abs(smallestSum) + 1

        return 1
