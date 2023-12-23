class Solution:
    '''
    We want to create all the possible permutations and pass on the remaining
    numbers to pick from.
    
    Time: O(2^n)
    Space: O(2^n)
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, arr):
            if not arr:
                res.append(perm.copy())
                return

            # want to create all of the different permutations
            for i in range(len(arr)):
                # want to left shift all by 1
                newArr = arr[i:] + arr[:i]
                
                perm.append(newArr[0])
                backtrack(perm, newArr[1:])
                perm.pop()
            return

        backtrack([], nums)
        return res