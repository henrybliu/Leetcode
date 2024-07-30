class Solution:
    """
    The key idea is to realize that there should never be an occurrence of "b"
    before "a". If we ever run across an instance of this, we should remove
    that.

    Time: O(n)
    Space: O(n)
    """

    def minimumDeletions(self, s: str) -> int:
        stack = []
        removals = 0
        for letter in s:
            if stack and letter == "a" and stack[-1] == "b":
                removals += 1
                stack.pop()
            else:
                stack.append(letter)

        return removals
