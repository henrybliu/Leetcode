class Solution:
    '''
    Sort the list of numbers to prevent duplicates. When backtracking, we don't
    backtrack on the same index if the numbers are the same -- preventing
    duplicate subsets. This prevents duplicate branches that start with the
    same number.

    Time: O(2^n)
    Space: O(2^n)
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #can sort to skip through repeating numbers
        nums.sort()
        res = []
        curr = []
        
        def backtrack(idx):
            if idx >= len(nums):
                res.append(curr.copy())
                return

            # take
            curr.append(nums[idx])
            backtrack(idx+1)

            # don't take and skip over repeated numbers
            curr.pop()
            while (idx+1) < len(nums) and nums[idx]==nums[idx+1]:
                idx+=1
            backtrack(idx+1)
            return

        backtrack(0)
        return res

