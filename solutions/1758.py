class Solution:
    '''
    Can use a map to quickly switch the value that we are comparing to. Need to
    check both for when starting with 1 and starting with 0.
    
    Time: O(n)
    Space: O(1)
    '''
    def minOperations(self, s: str) -> int:
        mapp = {'1':'0', '0':'1'}

        def changes(val):
            count = 0
            for i in range(len(s)):
                if s[i] != val:
                    count+=1
                val = mapp[val]
            return count

        return min(changes('0'), changes('1'))
            