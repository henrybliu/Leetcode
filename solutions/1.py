class Solution:
    '''
    Use a hashmap to store values that you have encountered. At each iteration,
    we should check if the another number that we have encountered can add to
    the sum.
    
    Time: O(n)
    Space: O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapping:
                return [i, mapping[diff]]
            mapping[nums[i]] = i
        

    