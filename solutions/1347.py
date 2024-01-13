from collections import Counter

class Solution:
    '''
    Create two counts of each strings number of characters if s has a greater
    count of a letter, then we need to change letters of t to become s. If t
    has a greater number of a letter than s, that means that s also has a
    greater number of a different letter. To prevent double counting, we only
    count when s has a larger count of a letter than t.

    Time: O(n)
    Space: O(n)
    '''
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        tCount = Counter(t)

        replacements = 0

        for k,v in sCount.items():
            diff = v - tCount[k]
            if diff > 0:
                replacements += diff

        return replacements
            