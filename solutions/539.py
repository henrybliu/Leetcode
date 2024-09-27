class Solution:
    """
    Treat this as a cyclic array. Compute the min time between any 2 times and
    then check the time difference between the first and last time that passes
    through midnight (simulating the cyclic nature of a clock)
    """

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        res = float("inf")

        def convertToMinutes(time):
            hour, minute = time.split(":")
            return (int(hour) * 60) + int(minute)

        def timeDiff(t1, t2):
            return t2 - t1

        # convert all times to minutes
        for i in range(len(timePoints)):
            timePoints[i] = convertToMinutes(timePoints[i])

        # compare the time difference between 2 times
        for i in range(1, len(timePoints)):
            res = min(res, timeDiff(timePoints[i - 1], timePoints[i]))

        # check the difference from the last time to the first time -- passing through midnight
        diffToMidnight = timeDiff(timePoints[-1], convertToMinutes("24:00"))
        diffFromMidnight = timeDiff(0, timePoints[0])

        return min(res, diffFromMidnight + diffToMidnight)
