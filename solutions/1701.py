class Solution:
    """
    For each customer, we want to compute the new time it would take to
    complete their order. However, if the next customer's arrival time is
    greater than the current time, then we will have the new current time be
    this customer's arrival time plus their prep time. Keep a running sum of
    each customer's wait time to quickly compute the average wait time.

    Time: O(n)
    Space: O(1)
    """

    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currTime = customers[0][0]
        currSum = 0

        for arrivalTime, prepTime in customers:
            currTime = (
                arrivalTime + prepTime
                if arrivalTime > currTime
                else currTime + prepTime
            )
            currSum += currTime - arrivalTime

        return currSum / len(customers)
