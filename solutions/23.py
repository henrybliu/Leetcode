# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution:
    """
    Create a queue that will hold all of the head nodes. Keep merging two lists at a time until there is only one remaining list.

    Time: O(k*n)
    Space: O(k*n)

    where k is the number of nodes in the longest linked list and n is the
    number of linked lists
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(t, b):
            dummy = ListNode()
            curr = dummy

            while t and b:
                if t.val < b.val:
                    curr.next = t
                    curr = curr.next
                    t = t.next
                else:
                    curr.next = b
                    curr = curr.next
                    b = b.next
            if t:
                curr.next = t
            if b:
                curr.next = b
            return dummy.next

        q = deque(lists)

        while len(q) >= 2:
            first = q.popleft()
            second = q.popleft()

            q.append(mergeTwo(first, second))

        if q:
            return q[0]
        else:
            return None
