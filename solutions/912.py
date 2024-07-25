class Solution:
    """
    Implement merge sort. Need to consider the base case where we merge a
    populated array with an array of nothing.

    For example:
    [1 2 3]
    can split into
    [1] [2, 3]
    then
    [],[1]

    Time: O(nlogn) -- O(logn) for each split (divide by 2 at each recursion)
    and O(n) for each merge
    Space: O(n)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        # base cases
        if not nums:
            return []

        if len(nums) == 1:
            return [nums[0]]

        # split nums into 2
        mid = len(nums) // 2
        leftArr = self.sortArray(nums[:mid])
        rightArr = self.sortArray(nums[mid:])

        # merge and create the new sorting
        newArr = []
        leftIdx = 0
        rightIdx = 0

        while leftIdx < len(leftArr) and rightIdx < len(rightArr):
            if leftArr[leftIdx] < rightArr[rightIdx]:
                newArr.append(leftArr[leftIdx])
                leftIdx += 1
            else:
                newArr.append(rightArr[rightIdx])
                rightIdx += 1

        newArr += leftArr[leftIdx:]
        newArr += rightArr[rightIdx:]

        return newArr
