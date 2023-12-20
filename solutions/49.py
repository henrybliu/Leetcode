from collections import defaultdict
class Solution:
    '''
    Can create an array indexed by lowercase ASCII values starting from 'a' to
    represent the key and group similar words by this key.

    Time: O(n*k)
    Space: O(n*k)
    where n is the number of words and k is the length of the longest word
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        for word in strs:
            alpha = [0 for _ in range(26)]
            for c in word:
                alpha[ord(c)-ord('a')]+=1
            groups[tuple(alpha)].append(word)

        res = []
        for g in groups.values():
            res.append(g)

        return res

