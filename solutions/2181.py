# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Whenever we encounter a node with value 0, add the accumulated sum to the
    created linked list.

    Time: O(n)
    Space: O(n)
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        add = head.next
        curr = add
        currSum = 0

        while curr:
            if curr.val == 0:
                add.val = currSum
                currSum = 0
                # if the end of the linked list has been reached, the next
                # value should be None
                if curr.next:
                    add = add.next
                else:
                    add.next = None

            else:
                currSum += curr.val

            curr = curr.next

        return head.next
