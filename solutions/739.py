class Solution:
    """
    Maintain a monotonic stack that will keep track of the index of the
    original day in question. When we find a day that is warmer, then keep
    popping from the list

    Time: O(n)
    Space: O(n)

    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            temp, day = temperatures[i], i

            if not stack:
                stack.append((temp, day))
            else:
                while stack and temp > stack[-1][0]:
                    prevTemp, prevDay = stack.pop()
                    res[prevDay] = day - prevDay

                stack.append((temp, day))

        return res
