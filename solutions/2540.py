class Solution:
    '''
    Use a 2 pointer approach. Move the pointer that is pointing to a smaller
    value to try and catch up to the larger pointer's value. This will ensure
    that we return the smallest common number.

    Time: O(n)
    Space: O(1)
    '''
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]

            elif nums1[ptr1] < nums2[ptr2]:
                ptr1+=1

            else:
                ptr2+=1

        return -1