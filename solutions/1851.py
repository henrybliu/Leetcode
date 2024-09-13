import heapq


class Solution:
    """
    For each query, we want to consider the valid intervals -- sorting the
    intervals by size will help to prioritize and more quickly identify the
    smallest interval.

    Sort the intervals by start time and the queries in increasing order so
    that we can consider intervals in a chronologically increasing manner. This
    means that queries that are past an interval's start and end time would no
    longer be considered (also in future queries).

    Use a min heap to prioritize candidate intervals with the smallest size.
    """

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(query, i) for i, query in enumerate(queries)]
        queries.sort()

        res = {}
        intervalIdx = 0
        heap = []
        res = [0 for _ in range(len(queries))]

        for query, queryIdx in queries:
            while intervalIdx < len(intervals) and intervals[intervalIdx][0] <= query:
                heapq.heappush(
                    heap,
                    (
                        intervals[intervalIdx][1] - intervals[intervalIdx][0] + 1,
                        intervals[intervalIdx][1],
                    ),
                )
                intervalIdx += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            res[queryIdx] = heap[0][0] if heap else -1

        return res
