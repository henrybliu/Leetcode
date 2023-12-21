# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    When adding the nodes, make sure to keep track of the carry amount. Make
    sure to add the leftover carry amount (if any) at the end.

    Time: O(n)
    Space: O(n)
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = add//10
            add -= carry*10
            head.val = add
            if l1.next and l2.next:
                head.next = ListNode()
                head = head.next
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            head.next= ListNode()
            head=head.next
        while l1:
            add = l1.val + carry
            carry = add//10
            add -= carry*10
            head.val = add
            if l1.next:
                head.next=ListNode()
                head = head.next
            l1 = l1.next
        while l2:
            add = l2.val + carry
            carry = add//10
            add -= carry*10
            head.val = add
            if l2.next:
                head.next=ListNode()
                head = head.next
            l2 = l2.next
        if carry > 0:
            head.next = ListNode()
            head = head.next
            head.val = carry
        return dummy



    