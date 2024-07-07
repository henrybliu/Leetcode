class Solution:
    """
    Notice that each pass in 1 direction takes n-1 moves. When moving left, we
    need to add 1 to offset and start counting at 1 (1-indexing). Whem moving
    right, we need to offset by 1 again to start counting 1 off from the right.

    """

    def passThePillow(self, n: int, time: int) -> int:
        # 1 direction is completed in n-1 moves
        direction = time // (n - 1)
        # we start at 1
        # add 1 to offset from the start and for 1-indexing
        remainder = (time % (n - 1)) + 1

        # if moving right
        if direction % 2 == 0:
            return remainder
        # if moving left
        else:
            # add 1 to offset again from the end when reversing directions
            return n - remainder + 1
