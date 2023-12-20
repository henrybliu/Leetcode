class Solution:
    '''
    Want to find the 2 smallest chocolate prices in linear time -- do so in 2
    loops. Check if the leftover amount of money is valid.

    Time: O(n)
    Space: O(1)
    '''
    def buyChoco(self, prices: List[int], money: int) -> int:
        choc1 = float('inf')
        idx1 = 0

        for i in range(len(prices)):
            if prices[i] < choc1:
                choc1 = prices[i]
                idx1 = i

        choc2 = float('inf') 
        for i in range(len(prices)):
            if prices[i] <= choc2 and i != idx1:
                choc2 = prices[i]

        leftover = money - choc1 - choc2

        return leftover if leftover >= 0 else money

            