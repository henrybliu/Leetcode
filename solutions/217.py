class Solution:
    '''
    The length of unique numbers would be the same as the original list of
    numbers if there are no duplicates.

    Time: O(n)
    Space: O(n)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

