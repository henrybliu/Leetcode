# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Use 2 pointers. One to set the linked list and one to explore the linked
    list. The set pointer only moves when the explore pointer's value isn't in
    nums.

    """

    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        res.next = head

        nums = set(nums)

        prev = res
        curr = head

        while curr:
            if curr.val not in nums:
                prev.next = curr
                prev = curr

            curr = curr.next

        # this is necessary in case we have deleted a nodes and reached the end
        # of the linked list
        prev.next = None

        return res.next
