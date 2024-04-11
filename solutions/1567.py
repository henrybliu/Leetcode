class Solution:
    """
    There are some key realizations to be made:

    Case 1: We encounter a postive number
    - this means that we add 1 to the current positive length and to the
    negative length because the sign of the current product will not change
    - but if the negLen is currently 0, we can't add 1 because there is nothing
    to be multiplied with

    Case 2: We encounter a negative number
    - this means that we add 1 to the opposite lengths
    - if posLen is currently 0, we can add 1 to the resulting negLen
    - if negLen is currently 0, we can't add 1 to the posLen because there is
    no number to be multiplied to result in a positive number

    Case 3: We encounter 0
    - the product can no longer be negative or positive, so we reset posLen and
    negLen to 0

    Time: O(n)
    Space: O(n)
    """

    def getMaxLen(self, nums: List[int]) -> int:
        posLen = 0
        negLen = 0
        maxLen = 0

        for num in nums:
            if num > 0:
                posLen += 1
                negLen = negLen + 1 if negLen else 0
            elif num < 0:
                # can do this in one line to eliminate need for temp variables
                posLen, negLen = negLen + 1 if negLen else 0, posLen + 1
            else:
                negLen = 0
                posLen = 0

            maxLen = max(maxLen, posLen)
        return maxLen
