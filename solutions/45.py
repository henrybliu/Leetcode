class Solution:
    """
    At each position, we want to consider all of the next positions that we can
    arrive at. From there, we then one to update our next range to include the
    furthest position that we can arrive at.

    Time: O(n^2)
    Space: O(1)
    """

    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        jumps = 0

        while r < len(nums) - 1:
            furthest = 0

            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])

            l = r + 1
            r = furthest
            jumps += 1

        return jumps
