class Solution:
    """
    When going through the gas stations, a key realization is that if we ever
    encounter a point where the total cost exceeds the total amount of gas,
    then none of indices to the left of this point, will work. The current
    point also wouldn't work because if the total is below zero, then the
    current station had a cost that was greater than gas.The solution must
    therefore be to the right still.

    Time: O(n)
    Space: O(1)
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        starting = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                # skip current index bc current index decreased it
                starting = i + 1

        return starting
