class Solution:
    '''
    At each position, we can take and stay at the same index, or we cannot take
    and move on to the next index.
    
    Time: O(2^n)
    Space: O(2^n)
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, arr, currSum):
            if currSum == target:
                res.append(arr.copy())
                return

            if currSum > target:
                return

            if idx >= len(candidates):
                return

            # take
            arr.append(candidates[idx])
            backtrack(idx, arr, currSum + candidates[idx])

            # don't take
            arr.pop()
            backtrack(idx+1, arr, currSum)
            return

        backtrack(0,[],0)
        return res