class Solution:
    """
    This approach is O(n + logn). Make use of prefix sum to calculate the
    amount of chalk needed per index. We can also find the first index that
    runs out of chalk by using binary search since the prefix sum is in
    increasing order. We can also reduce the value of k to be the value of
    k % sum(chalk). This is because each full iteration through chalk provides
    the same value to be subtracted from k. Using the remainder helps to
    achieve a 1 pass solutoin for finding the student that runs out of chalk.
    """

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefixSum = [0]
        for i in range(len(chalk)):
            prefixSum.append(prefixSum[-1] + chalk[i])

        remainingChalk = k % prefixSum[-1]

        l = 0
        r = len(prefixSum) - 1
        while l < r:
            mid = l + (r - l) // 2

            if prefixSum[mid] > remainingChalk:
                r = mid
            else:
                l = mid + 1

        return r - 1


"""
THIS APPROACH IS O(2n)

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        roundSum = sum(chalk)
        remainingChalk = k % roundSum

        for i in range(len(chalk)):
            if remainingChalk < chalk[i]:
                return i
            else:
                remainingChalk -= chalk[i]
"""
