from collections import defaultdict
class Solution:
    '''
    We can use a counter and check that the count for each letter is evenly
    divisible by the number of words. This is because the same number of a
    letter should exist in all words.

    Time: O(n*k)
    Space: O(n*k)

    where n is the number of words and k is the length of the longest word
    '''
    def makeEqual(self, words: List[str]) -> bool:
        numStrings = len(words)
        count = defaultdict(int)

        for word in words:
            for letter in word:
                count[letter]+=1

        # the number of letters should be evenly divisble by numStrings so that every word has this letter

        for k,v in count.items():
            if v % numStrings != 0:
                return False

        return True
