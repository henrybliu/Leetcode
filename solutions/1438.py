from collections import deque


class Solution:
    """
    Use two monotonoic deques to keep track of the max and min values that we
    have encountered so far in our current (sliding) window. We use a monotonic
    deque for:

    -   max values
        To keep track of the next largest max values in case we decide to shrink our window

    - min values
        To keep track of the next smallest min values in case we decide to shrink our window

    Our window is shrunk when the max and min values encountered exceeds the limit
    """

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # monotonically increasing to keep track of the next largest element
        # in the current window
        maxQ = deque()
        # monotonically decreasing to keep track of the next smallest element
        # in the current window
        minQ = deque()
        res = 0
        l = 0
        for r, num in enumerate(nums):
            # if the num is bigger than the last in maxQ, want to replace maxQ
            # with that num so that it is the largest elem in the current
            # window
            while maxQ and num > maxQ[-1]:
                maxQ.pop()

            # if the num is smaller than the last in minQ, want to replace minQ
            # with that num so that it is the smalleset elem in the current
            # window
            while minQ and num < minQ[-1]:
                minQ.pop()

            # add the num to both deques
            minQ.append(num)
            maxQ.append(num)

            # check that the min and max values are within the limit
            while maxQ[0] - minQ[0] > limit:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                if nums[l] == minQ[0]:
                    minQ.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res
