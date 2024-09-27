class Solution:
    """
    Put each row into its own subgroup first. Then for each subgroup create the
    spaces as necessary. Make sure to check if the row only has one word or if
    it is the last row for proper text justification.
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        groups = []
        currGroup = []
        currWordsLength = 0

        for word in words:
            numWords = len(currGroup) + 1
            minSpaces = numWords - 1
            newWordsLength = currWordsLength + minSpaces + len(word)

            if newWordsLength > maxWidth:
                groups.append((currGroup, currWordsLength))
                currWordsLength = len(word)
                currGroup = [word]
            else:
                currGroup.append(word)
                currWordsLength += len(word)

        groups.append((currGroup, currWordsLength))
        res = []

        for idx, (group, wordsLength) in enumerate(groups):
            currString = ""
            # if the row only has one word, we just add the spaces to the end
            if len(group) == 1:
                currString = group[0]
                addSpaces = " " * (maxWidth - len(currString))
                currString += addSpaces
            # for creating the last row
            elif idx == len(groups) - 1:
                for i, word in enumerate(group):
                    currString += word
                    # only add spaces after the word if it isn't the last one
                    if i != len(group) - 1:
                        currString += " "
                addSpaces = " " * (maxWidth - len(currString))
                currString += addSpaces

            else:
                # find the number of space groupings that exists and distribute the spaces evenly
                spaceGroups = len(group) - 1
                diff = maxWidth - wordsLength
                spacesPerGroup = diff // spaceGroups
                remainder = diff % spaceGroups

                for i, word in enumerate(group):
                    currString += word

                    addSpaces = " " * spacesPerGroup
                    if remainder:
                        addSpaces += " "
                        remainder -= 1

                    if i != len(group) - 1:
                        currString += addSpaces

            res.append(currString)
        return res
