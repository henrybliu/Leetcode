# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    A key point to recognize is that a sum of 0 exists when we see the same
    prefix sum. When we see the same prefix sum, we know that we can remove
    the nodes from the one after the first existence of the prefix sum to the
    next node after the current node.

    For example:

    1 2 -3 3 1

    has the prefix sum
    1 3 0 3 1

    We see 3 twice so we can remove the nodes that exist after the prefix sum
    of 3 and its later nodes up to and including the current prefix sum of 3
    (the second occurrence)
    """

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefixSumToNode = {}
        prefixSum = 0
        curr = dummy
        while curr:
            prefixSum += curr.val
            if prefixSum in prefixSumToNode:
                prev = prefixSumToNode[prefixSum]
                toRemove = prev.next

                # remove all of these prefix sums from the hashmap
                p = prefixSum + (toRemove.val if toRemove else 0)
                while p != prefixSum:
                    del prefixSumToNode[p]
                    toRemove = toRemove.next
                    p += toRemove.val if toRemove else 0
                # create a new connection from prev to curr.next
                prev.next = curr.next
            else:
                prefixSumToNode[prefixSum] = curr
            curr = curr.next
        return dummy.next
