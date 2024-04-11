class Solution:
    """ """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(idx, arr, currSum):
            if currSum == target:
                res.append(arr.copy())
                return

            if idx >= len(candidates) or currSum > target:
                return

            # take
            arr.append(candidates[idx])
            backtrack(idx + 1, arr, currSum + candidates[idx])

            # don't take
            arr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx + 1, arr, currSum)

            return

        backtrack(0, [], 0)
        return res
