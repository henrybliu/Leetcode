class Solution:
    '''
    Realization is that at each step (3 or greater steps), you sum up the ways
    to reach the step right before and the step 2 before. This is because you
    are able to reach your current step from those two steps by either climbing
    1 or 2 steps.

    Time: O(n)
    Space: O(1)
    '''
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        left = 2
        twoLeft = 1

        for i in range(3, n+1):
            res = left + twoLeft
            twoLeft = left
            left = res
            
        return res