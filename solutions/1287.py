from collections import Counter
class Solution:
    '''
    Use a Counter and then find which element occurrs 25% of the time.

    Time: O(n)
    Space: O(n)
    '''
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = Counter(arr)
        target = len(arr)//4

        for k,v in counts.items():
            if v > target:
                return k