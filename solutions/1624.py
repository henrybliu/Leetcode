class Solution:
    '''
    Use a hashmap to keep track of the eariest occurrence of all letters. This
    accounts for inputs such as 'abcabba' where the largest substring is
    between the first and last 'a'.

    Time: O(n)
    Space: O(n)
    '''
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # want to keep track of the first index that a letter occurs at
        earliest = {}
        # intialize res to be -1 for the case when no duplicates are found
        res = -1

        for i,v in enumerate(s):
            if v not in earliest:
                earliest[v] = i
            else:
                duplicate = True
                res = max(res, i - earliest[v]-1)
              
        return res