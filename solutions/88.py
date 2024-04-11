class Solution:
    """
    In nums1, swap the values that we care and don't care about (m and n
    respectively). This way, we can update nums1, with the lower of the two
    lists' values while not overwriting the values in nums1 that we need to
    compare.

    Time: O(m+n)
    Space: O(1)
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:m], nums1[n:] = nums1[n:], nums1[:m]

        p1 = n
        p2 = 0

        for i in range(len(nums1)):
            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 += 1
                else:
                    nums1[i] = nums2[p2]
                    p2 += 1

            elif p1 < len(nums1):
                nums1[i] = nums1[p1]
                p1 += 1

            else:
                nums1[i] = nums2[p2]
                p2 += 1
