class Solution:
    """
    At each position, we want to compare the smallest sum that can be created
    at the current position and the adjacent positions above
    [(i-1,j-1),(i-1,j),(i-1,j+1)] given that the j coordinate is within bounds.
    We can also do this in constant time by using the input matrix.

    Time: O(n*m)
    Space: O(1)
    """

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(1, rows):
            for j in range(0, cols):
                smallestSum = float("inf")
                # at each position, want to compare it to the 3 that are above
                # and adjacent
                if j - 1 >= 0:
                    smallestSum = min(smallestSum, matrix[i][j] + matrix[i - 1][j - 1])
                if j + 1 < cols:
                    smallestSum = min(smallestSum, matrix[i][j] + matrix[i - 1][j + 1])
                matrix[i][j] = min(matrix[i][j] + matrix[i - 1][j], smallestSum)

        return min(matrix[-1])
