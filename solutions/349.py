class Solution:
    """
    Use two sets to compute their intersection.

    Time: O(n)
    Space: O(n)
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        common = set()

        for num in nums1:
            if num in nums2:
                common.add(num)

        for num in nums2:
            if num in nums1:
                common.add(num)

        return list(common)
