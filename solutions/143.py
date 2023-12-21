# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    We can reverse the second half of the linked list and then have a pointer
    point to the start of this second half of the linked list. We then
    alternate between adding from the head and the flipped pointer.
    
    Time: O(n)
    Space: O(1)
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid point in the linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #this is the middle of the list
        r = slow.next

        #want to create separation in the two lists
        slow.next = None

        #start reversing the second half of the linked list
        l = None
        while r:
            temp = r.next
            r.next = l
            l = r
            r = temp

        original = head
        original = original.next
        flipped = l
        curr = head
        while original and flipped:
            origNext = original.next
            flipNext = flipped.next
            curr.next = flipped
            curr = curr.next
            curr.next = original
            curr= curr.next
            flipped = flipNext
            original = origNext

        #add the remainder of the linked list
        if original:
            curr.next=original
        if flipped:
            curr.next=flipped
            

