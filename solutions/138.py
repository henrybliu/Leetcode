"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    """
    Use a hashmap to store the new nodes that are created for each original
    node.

    Time: O(n)
    Space: O(n)
    """

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        mapping = {}

        # create the mapping of the original nodes to the new nodes
        curr = head
        while curr != None:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        # connect next and random
        curr = head
        while curr != None:
            newNode = mapping[curr]
            if curr.next == None:
                newNode.next = None
            else:
                newNode.next = mapping[curr.next]

            if curr.random == None:
                newNode.random = None
            else:
                newNode.random = mapping[curr.random]
            curr = curr.next

        return mapping[head]
