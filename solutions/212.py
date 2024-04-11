class Solution:
    """
    We backtrack at each position on the board to try and create the word that
    we are looking for. Make sure to remove from the visited set unsucessful
    finds so that next searches can also use that coordinate. Make sure to also
    remove '*' after a word has been found to indicate that it is no longer a
    valid word.

    Time: O(n^2)
    Space: O(n)

    For each position, we try at most all n other positions and store all n other positions in a recursive stack
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # create the trie
        trie = {}
        for word in words:
            level = trie
            for letter in word:
                if letter not in level:
                    level[letter] = {}
                level = level[letter]
            level["*"] = {}

        def backtrack(r, c, level, word):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] not in level
                or (r, c) in visited
            ):
                return

            # add the letter that we are on to the word
            word += board[r][c]

            # can delete words that were found by removing the "*" -- also to prevent duplicates
            if "*" in level[board[r][c]]:
                res.append(word)
                del level[board[r][c]]["*"]

            visited.add((r, c))
            for v, h in direction:
                backtrack(r + v, c + h, level[board[r][c]], word)
            visited.remove((r, c))

        res = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie, "")
        return res
