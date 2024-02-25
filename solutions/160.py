# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    For different length lists, we need to have both pointers be at the same
    "level". Rather than counting the length of each list, we can do so by
    moving the pointer to the end and resetting them to then point at the
    other list's head. A pointer traversing a shorter list will reach the end
    of the intersecting list first. By the time the pointer of the longer list
    is reset, both pointers will now be at the same level. When at the same
    level, we can then check if both pointers point at a shared node or None
    (where there is no intersection).

    Time: O(m+n)
    Space: O(1)
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a