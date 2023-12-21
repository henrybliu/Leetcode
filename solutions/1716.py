class Solution:
    '''
    At each week, we increase the starting amount by 1, then for each day, we
    add 1 to the starting amount.

    Time: O(n)
    Space: O(1)
    '''
    def totalMoney(self, n: int) -> int:
        total = 0
        prev = 0
        toAdd = 0

        for i in range(n):
            # you have cycled through 1 week
            if i % 7 == 0:
                # restart the amount to start paying at
                start = prev +1
                # update the previous monday's pay
                prev = start
                # start paying wtih this amount
                toAdd = start

            total += toAdd
            toAdd +=1


        return total