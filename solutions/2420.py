class Solution:
    """
    Use a monotonic stack to keep track of the counts of values that are in
    non-decreasing/increasing order to the left/right of an index. From left to
    right non-decreasing order is the same as non-increasing order from right
    to left.

    """

    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        leftSide = [False for _ in range(len(nums))]
        rightSide = [False for _ in range(len(nums))]

        # maintain non-increasing order on the left side
        stack = []
        for i in range(len(nums)):
            if len(stack) >= k:
                leftSide[i] = True

            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] <= stack[-1]:
                    stack.append(nums[i])
                else:
                    stack = [nums[i]]

        # maintain non-decreasing order on the right side -- which also means
        # non-increasing going from right to left
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if len(stack) >= k:
                rightSide[i] = True

            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] <= stack[-1]:
                    stack.append(nums[i])
                else:
                    stack = [nums[i]]

        res = []
        for i in range(len(nums)):
            if leftSide[i] and rightSide[i]:
                res.append(i)

        return res
