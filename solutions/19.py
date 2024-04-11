# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    First create a gap of size n between the fast and slow pointers. When the
    fast pointer reaches the end of the linked list, the left pointer should be
    pointing at the node to be removed. We should also create a dummy node that
    points to the current head node in case we need to remove the head node.

    Time: O(n)
    Space: O(1)
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        prev = res

        r = head

        for i in range(n):
            r = r.next

        l = head

        while r:
            r = r.next
            prev = l
            l = l.next

        prev.next = l.next

        return res.next
