class Solution:
    """
    Use a monotonic increasing stack so that when we encounter a minimum, we
    calculate the number of subarrays that exist using this local/max minimum.
    At the index of a minimum, we calculate the distance left where these
    numbers will all be greater than the current minimum and the distance right
    up to the index that we have explored so far. The number of subarrays is
    then the number of elements to the right times the number of elements to
    the left. The intuition for this is that the elements in the left would all
    include the subarrays on the right becuase they all include the current
    minimum. You then add the number of subarrays times the minimum to the
    result. For leftover elements in the stack, this occurrs because no smaller
    minimum was found. The number of elements for these subarrays on the right
    extends to the end of arr and left to the previous index on the stack.

    Time: O(n)
    Space: O(n)
    """

    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []  # (num, idx)
        res = 0
        mod = 10**9 + 7

        for i in range(len(arr)):
            num = arr[i]

            # compute the number of subarrays that can be created
            while stack and num < stack[-1][0]:
                prevNum, prevIdx = stack.pop()
                # how far left was the previous item before the popped element
                # - if there isn't a previous element on the stack - then it is
                # just the index + 1

                # consider
                # 5 3 1
                # by the time we pop 3 from the stack -- 5 is already gone, but
                # we know that 5 still uses 3 in its subarray

                # we also do +1 to include the current index
                left = prevIdx - stack[-1][1] if stack else prevIdx + 1
                right = i - prevIdx
                # consider
                # 1 2 3 4 1
                # l c     r
                res = (res + prevNum * left * right) % mod

            stack.append((num, i))

        # calculate the remaining number of subarrays where a new minimum was
        # not found
        for i in range(len(stack)):
            prevNum, prevIdx = stack[i]
            left = prevIdx - stack[i - 1][1] if i - 1 >= 0 else prevIdx + 1
            right = len(arr) - prevIdx
            res = (res + prevNum * left * right) % mod

        return res
