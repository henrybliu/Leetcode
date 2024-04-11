class Solution:
    """
    At each index, we can choose to take or not to take.

    Time: O(n^2)
    Space: O(n^2)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, arr):
            if idx == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[idx])
            backtrack(idx + 1, arr)
            arr.pop()
            backtrack(idx + 1, arr)

            return

        backtrack(0, [])
        return res
