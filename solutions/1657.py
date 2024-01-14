from collections import Counter

class Solution:
    '''
    An important realization is that both word1 and word2 need to be of the
    same length and contain the same type of characters. Both operations also
    allow you to create any target word, so long that the target word has the
    same frequencies of letters present in the start word, ie. operation1
    allows you to freely reorder the string and operation2 allows you to freely
    reassign a letter's frequency.

    For example:
    word1 = cabbba -> a:2, b:3, c:1
    word2 = abbccc -> a:1, b:2, c:3 

    Starting from word1, we can swap all occurrences of a <-> c:
    acbbbc

    Now, we can swap all occurrences of b <-> c:
    abcccb

    The first operation allows us to create word2 automatically. 

    We could've also started the swapping with some other pair of letters, but
    we will eventually arrive at the same solution. This is because we can
    perform either operation an unlimited number of times.

    Time: O(nlogn) -- this can be reduced to O(n) by just having an array where
    the index is the number of occurrences
    Space: O(n)
    '''
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        counts1 = Counter(word1)
        counts2 = Counter(word2)

        occurrences1 = list(counts1.values())
        occurrences2 = list(counts2.values())

        occurrences1.sort()
        occurrences2.sort()

        return occurrences1 == occurrences2
