class Solution:
    '''
    Only need to loop through the length of the shortest word. Compare each
    letter of the smallest word with the other words to create the longest
    prefix.

    Time: O(n)
    Space: O(n)
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        smallest  = strs[0]

        for word in strs:
            if len(word) < len(smallest):
                smallest = word
            if word == "":
                return ""

        for i in range(len(smallest)):
            for word in strs:
                if word[i] != smallest[i]:
                    return smallest[:i]

        return smallest