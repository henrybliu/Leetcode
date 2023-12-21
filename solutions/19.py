# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Want create a gap of size n between the fast and slow pointers. When the
    fast pointer reaches, the end, we can remove the node at the slow pointer.
    
    Time: O(n)
    Space: O(1)
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        l = head
        r = head

        #create a gap of size n
        for i in range(n):
            r = r.next

        #move l to the node that needs to be removed
        while r:
            r = r.next
            prev = l
            l = l.next

        #remove the node at l
        prev.next = l.next

        return dummy.next        
