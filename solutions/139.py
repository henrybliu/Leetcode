class Solution:
    """
    Backtrack with memoization to try and break the current word only using
    words in wordDict.

    Time: O(n^2)
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}
        wordDict = set(wordDict)

        def dfs(idx, remainder):
            if idx >= len(s):
                return True

            if remainder in mem:
                return mem[remainder]

            currWord = ""
            # can optimize this here to use the min of len(s) and
            # max_length(word in wordDict) + idx
            for i in range(idx, len(s)):
                currWord += s[i]

                if currWord in wordDict:
                    if dfs(i + 1, s[i + 1 :]):
                        mem[remainder] = True
                        return True

            mem[remainder] = False
            return False

        return dfs(0, s)
