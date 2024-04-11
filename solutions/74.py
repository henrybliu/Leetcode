class Solution:
    """
    Perform binary search twice to locate the row and column.

    Time: O(logn)
    Space: O(1)
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # perform binary search to find the row
        searchRow = 0
        t = 0
        b = rows - 1

        while t <= b:
            mid = (t + b) // 2
            if matrix[mid][cols - 1] >= target:
                searchRow = mid
                b = mid - 1
            else:
                t = mid + 1

        # perform binary search within the row
        l = 0
        r = cols - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[searchRow][mid] == target:
                return True
            elif matrix[searchRow][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
