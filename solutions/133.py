"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    '''
    Use a hashmap to map the original nodes to the copied nodes. This will help
    prevent creating multiple copies of the same node. Then do BFS on the
    original graph to create the copies and each node's neighbors.
    
    Time: O(n)
    Space: O(n)

    where n is the number of nodes
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque()
        mapp = {} # original node -> copied node

        head = Node(node.val)
        q.append(node)
        mapp[node] = head
        
        # perform BFS on the orignal graph to create copies
        while q:
            curr = q.popleft()

            # create neighbor copies for the copy of the current node
            for neighbor in curr.neighbors:
                newNode = None
                if neighbor not in mapp:
                    newNode = Node(neighbor.val)
                    mapp[neighbor] = newNode
                    q.append(neighbor)
                else:
                    newNode = mapp[neighbor]
                
                mapp[curr].neighbors.append(newNode)

        return head