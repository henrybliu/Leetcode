# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Use three pointers to keep track of the left, middle, and right node
    values. Use this to check for critical points. Use 2 other variables to
    track the first and most recent critical points. These variables will be
    used to track the min and max distance between critical points.

    Time: O(n)
    Space: O(1)
    """

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDist = float("inf")
        maxDist = float("-inf")

        if not head or not head.next:
            return [-1, -1]

        left = head
        curr = head.next
        right = head.next.next
        currIdx = 1
        firstCriticalPoint = -1
        prevCriticalPoint = -1

        while right:
            if (curr.val < left.val and curr.val < right.val) or (
                curr.val > left.val and curr.val > right.val
            ):
                if firstCriticalPoint == -1:
                    firstCriticalPoint = currIdx
                    prevCriticalPiont = currIdx

                if currIdx != firstCriticalPoint and currIdx != prevCriticalPoint:
                    minDist = min(minDist, currIdx - prevCriticalPoint)
                    maxDist = max(maxDist, currIdx - firstCriticalPoint)

                prevCriticalPoint = currIdx

            left = curr
            curr = right
            currIdx += 1
            right = right.next

        if minDist == float("inf") or maxDist == float("-inf"):
            return [-1, -1]

        return [minDist, maxDist]
