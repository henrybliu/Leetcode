class Solution:
    '''
    We can use DP by understanding that the current target with the current
    number of dice rolls is the sum of all of the combinations that create the
    current target value -1 at the previous dice roll. This is because adding 1
    to all of the previous dice roll combinations means that we have rolled one
    more dice and that the current target is now 1 more than before.
    
    Time: O(n*m*k)
    Space: O(n*m)

    where n is the number of dice rolls, k is the number of faces, and m is the target value
    '''
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7

        # case were no such target is achievable
        if n * k < target:
            return 0

        dp = [[0 for _ in range(target+1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            # this is the target
            for j in range(i, min(i * k, target) + 1):
                # want to add the previous counts at the previous number of dice rolls
                for p in range(1, min(k, j) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) %  mod

        return dp[-1][-1]