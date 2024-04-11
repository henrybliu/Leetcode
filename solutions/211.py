class WordDictionary:
    """
    Use a hashmap of hashmaps to create a trie data structure. A level that has
    '*' in the next level means that the current level forms a valid word.

    Time: O(n)
    Space: O(n*k)
    where n is the length of the longest word and k the number of words
    """

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        level = self.trie
        for l in word:
            if l not in level:
                level[l] = {}
            level = level[l]
        level["*"] = ""

    def search(self, word: str) -> bool:
        # if we i reaches len(word) return True
        def dfs(level, i):
            if "*" in level and i == len(word):
                return True

            if i >= len(word):
                return False

            if word[i] == ".":
                for n in level:
                    if dfs(level[n], i + 1):
                        return True
            if word[i] in level:
                if dfs(level[word[i]], i + 1):
                    return True
            return False

        return dfs(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
