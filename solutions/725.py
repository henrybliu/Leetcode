# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Traverse the linked list to count the number of total nodes. Then use math
    to calculate the number of nodes per section with remainders as necessary.
    Remember to pad the resulting array with None if there aren't enough nodes
    to be distributed over k sections.
    """

    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        nodesPerSection = length // k
        remainder = length % k

        res = []
        curr = head
        while curr:
            distanceToTravel = nodesPerSection
            if remainder:
                distanceToTravel += 1
                remainder -= 1

            res.append(curr)
            prev = None
            for i in range(distanceToTravel):
                prev = curr
                curr = curr.next
            prev.next = None

        while len(res) < k:
            res.append(None)

        return res
