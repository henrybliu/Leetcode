class Solution:
    '''
    Idea is to try and create valid palindromes and then backtrack on the
    remainder of s.

    Time: O(2^n)
    Space: O(2^n)
    '''
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palin = [] # the current palindrome being created

        def backtrack(idx):
            if idx >= len(s):
                res.append(palin.copy())

            for i in range(idx, len(s)):
                # try creating palindromes starting from the current index
                test = s[idx:i+1]
                if test == test[::-1]:
                    palin.append(test)
                    backtrack(i+1)
                    palin.pop()

        backtrack(0)
        return res