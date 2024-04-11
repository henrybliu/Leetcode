# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Have a trailing pointer that will be pointed to and a make sure to store
    the next node before updating its next pointer!

    Time: O(n)
    Space: O(1)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast = head
        slow = None

        while fast:
            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp

        return slow
