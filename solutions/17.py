from collections import deque

class Solution:
    '''
    Approach this iteratively by adding one number's letters at a time to all
    currently created combinations.

    Time: O(n*k)
    Space: O(n*k)

    where n is the number of digits and k the max number of letters
    corresponding to a number
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        if not digits:
            return []

        q = deque()
        q.append(('', 0)) # (currString, idx)
        
        res = []
        while q:
            currString, idx = q.popleft()

            if idx == len(digits):
                res.append(currString)

            else:
                num = digits[idx]

                for letter in mapp[num]:
                    q.append((currString + letter, idx+1))
            
        return res
