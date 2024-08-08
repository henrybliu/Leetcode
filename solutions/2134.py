class Solution:
    """
    Idea is that we want a window the same size of the total number of ones. We
    then track the most number of ones that can exist in that window. This is
    because the number of swaps needed is the total number of ones minus the
    largest of number of ones that can exist in a window of that size.
    """

    def minSwaps(self, nums: List[int]) -> int:
        maxOnes = 0
        currOnes = 0

        totalOnes = sum(nums)
        l = 0

        for r in range(2 * len(nums)):
            if nums[r % len(nums)] == 1:
                currOnes += 1

            if r - l + 1 > totalOnes:
                currOnes -= nums[l % len(nums)]
                l += 1

            maxOnes = max(maxOnes, currOnes)

        return totalOnes - maxOnes
