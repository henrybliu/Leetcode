from collections import defaultdict, Counter


class Solution:
    """
    We can first check if the board contains all of the necessary letters. Then
    for each valid tile, we start our recursive search to see if we can create
    the target word. We use a visited set to prevent revisiting coordinates
    that we have already visited.

    Time: O(2^(m*n))
    Space: O(m*n)
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # can check if the board even has all the letters necessary to create the word to be faster
        boardCount = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                boardCount[board[r][c]] += 1

        wordCount = Counter(word)

        for k in wordCount.keys():
            if k not in boardCount or wordCount[k] > boardCount[k]:
                return False

        def backtrack(r, c, i, used, currString):
            # out of bounds or that the current letter doesn't match the next letter
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or i >= len(word)
                or board[r][c] != word[i]
                or (r, c) in used
            ):
                return False

            currString += board[r][c]

            if currString == word:
                return True

            used.add((r, c))

            for v, h in directions:
                if backtrack(r + v, c + h, i + 1, used, currString):
                    return True

            # we want later searches to be able to use this coordinate if a previous search didn't yield true
            used.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                # if we are at a tile that can potentially return true
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0, set(), ""):
                        return True

        return False
