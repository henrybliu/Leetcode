class Solution:
    '''
    We can use a dp array to calculate the minimum amount of time used so far.
    When having multiple balloons of the same color, we can take the balloon
    with the smaller time to remove and then update the current position in
    neededTime to the time that wasn't chosen. This essentially maintains the
    minimum times that we still have available - as if we were able to greedily
    pick balloons out of order instead of strictly left to right.

    An example is as follows:
    aaaa
    2134 

    The optimal solution would be to pick 1,2,3

    At index 1, we pick 1 as the minimum time and update neededTime to:
    2234

    At index 2, we can still pick from the times 2 and 3, so we pick 2:
    2234

    At index 3, we can pick from 3 and 4, so we pick 3:
    2234

    The total minimum time would then be 1+2+3 = 6. 

    TLDR: We are essentially maintaining the local minimum in O(1) by updating
    neededTime and greedily picking the smallest value and shifting the other
    minimum values that we haven't used yet for balloons of the same color.

    Time: O(n)
    Space: O(n) - can be updated to be O(1) since we are only ever referring to 2 values at a time
    '''
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        dp = [0 for _ in range(len(colors))]
        

        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                # dp[i] = min(neededTime[i], neededTime[i-1])
                if neededTime[i-1] < neededTime[i]:
                    dp[i] = neededTime[i-1]
                else:
                    dp[i] = neededTime[i]
                    neededTime[i] = neededTime[i-1]
            
            dp[i] += dp[i-1]

        return dp[len(colors)-1]