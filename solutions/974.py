from collections import defaultdict


class Solution:
    """
    A key realization is that two sums that have the same remainder when
    divided by k means that there exists some multiple of k between them. This
    is valid subarray that should be couted.

    Time: O(n)
    Space: O(n)
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        res = 0

        remainders = defaultdict(int)
        remainders[0] = 1

        for num in nums:
            currSum += num

            if currSum % k in remainders:
                res += remainders[currSum % k]

            remainders[currSum % k] += 1

        return res
