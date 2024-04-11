from collections import defaultdict


class Solution:
    """
    Need to create words by just parsing out the alphanumeric parts of the
    paragraph and converting them to lowercase.

    Time: O(n)
    Space: O(n)
    where n is the length of the paragraph
    """

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        ignore = set(["'", ".", ",", "!", "?"])
        counts = defaultdict(int)
        paragraph = paragraph.lower()

        res = ""
        resCount = 0

        parsedWord = ""
        for i in range(len(paragraph)):
            if paragraph[i].isalpha():
                parsedWord += paragraph[i]
            else:
                if parsedWord and parsedWord not in banned:
                    counts[parsedWord] += 1
                    if counts[parsedWord] > resCount:
                        resCount = counts[parsedWord]
                        res = parsedWord
                parsedWord = ""

        # final check
        if parsedWord and parsedWord not in banned:
            counts[parsedWord] += 1
            if counts[parsedWord] > resCount:
                resCount = counts[parsedWord]
                res = parsedWord
        return res
