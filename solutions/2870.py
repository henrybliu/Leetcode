from collections import Counter

class Solution:
    '''
    We realize that for say we have 4 occurences:
    x x x x
    3 3 3 
        2 2

    When we take the first 3, and have 1 remainder, that 1 remainder can be added to an occurence that we took in the group of 3. This way, we prioritize removing groups of 3 first and then the remainders as groups of 2. 

    Time: O(n)
    Space: O(n)
    '''
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        operations = 0

        for v in counts.values():
            if v == 1:
                return -1
            
            # we can find the number of 3s that can fit in the number of occurrences
            operations += v//3

            # 2s are essentially a remainder and another occurrence that we misclassfied as a group of 3
            if v%3:
                operations +=1
            
        return operations
