class Solution:
    '''
    Create a set of the the unique numbers and only try creating its
    consequtive sequence if no smaller number that belongs in the consecutive
    sequence exists.

    Time: O(n)
    Space: O(n)
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in nums:
                nextNum = num+1
                while nextNum in nums:
                    nextNum+=1
                longest = max(longest, nextNum-num)

        return longest