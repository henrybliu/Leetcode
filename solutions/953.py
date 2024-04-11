class Solution:
    """
    For each word, we want to check that the previous word is alphabetically
    first. This is the case when, the has all letters has an earlier or the
    same lexographic order as the second word and if this is satisfied, then it
    should also be shorter in length.

    Time: O(n*k)
    Space: O(n*k)

    where n is the number of words and k the number of characters in the longest word
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        positions = defaultdict(int)
        for i in range(len(order)):
            positions[order[i]] = i

        # check 2 words at a time
        prevWord = words[0]

        for i in range(1, len(words)):
            currWord = words[i]
            isFirst = False
            # prevWord needs to be alphabetically first
            for j in range(min(len(prevWord), len(currWord))):

                alpha1 = positions[prevWord[j]]
                alpha2 = positions[currWord[j]]

                # current word comes before prevWord
                if alpha2 < alpha1:
                    return False

                # found that prevWord is lexographically first - no need to keep checking
                if alpha1 < alpha2:
                    isFirst = True
                    break

            # haven't found that prevWord comes first
            if not isFirst:
                # if current word is shorter, not in lexographical order
                if len(currWord) < len(prevWord):
                    return False

            prevWord = words[i]

        return True
