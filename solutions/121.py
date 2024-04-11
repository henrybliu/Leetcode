class Solution:
    """
    At each index we keep track of the minimum purchase and the maximum profit
    made thus far.

    Time: O(n)
    Space: O(n)
    """

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float("inf")

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit
