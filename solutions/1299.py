class Solution:
    """
    Loop through the array backwards while keep tracking of the largest element
    encountered thus far.

    Time: O(n)
    Space: O(1)
    """

    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = currMax
            currMax = max(currMax, temp)
        return arr
