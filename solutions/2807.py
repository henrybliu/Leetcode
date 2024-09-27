# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    There is a special algorithm for computing the GCF in O(logn) time.
    """

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        pairs = {}

        def findGCF(larger, smaller):
            if (larger, smaller) in pairs:
                return pairs[(larger, smaller)]

            # Euclidean's algorithm -- this is O(logn)
            if larger % smaller == 0:
                pairs[(larger, smaller)] = smaller
                return smaller

            gcf = findGCF(smaller, larger % smaller)
            pairs[(larger, smaller)] = gcf
            return gcf

        prevNode = head
        currNode = head.next

        while currNode:
            nextNode = currNode.next

            smaller = min(prevNode.val, currNode.val)
            larger = max(prevNode.val, currNode.val)
            gcf = findGCF(larger, smaller)

            newNode = ListNode(gcf)

            prevNode.next = newNode
            newNode.next = currNode

            prevNode = currNode
            currNode = nextNode

        return head
