# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Can use fast and slow pointers where the fast pointer moves twice as fast.
    If the past pointer moves twice as fast, that means that when it reaches
    the end of the linked list, the slow pointer would in the middle.

    Time: O(n)
    Space: O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
