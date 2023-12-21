# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    Have a fast and slow pointer so that the fast pointer will eventually
    catch up to the slow pointer if there is a cycle.
    
    Time: O(logn)
    Space: O(1)
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False